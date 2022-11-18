//flag-icon flag-icon-ge
//NS_DJANGO_PHONE_NUMBER.JQuery= $.noConflict();
NS_DJANGO_PHONE_NUMBER.guid = function () {
    function uniqId() {
        return new Date().getTime() % (Math.random() * 100);
    }

    function s4() {
        return Math.floor(uniqId() * 0x10000)
            .toString(16)
            .substring(1);
    }

    return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
        s4() + '-' + s4() + s4() + s4();
};
NS_DJANGO_PHONE_NUMBER.ValueObject = function (regionCode, phoneNumber) {
    this.regionCode = regionCode;
    this.phoneNumber = phoneNumber;
};

$(function () {
    NS_DJANGO_PHONE_NUMBER.initialize();
});

NS_DJANGO_PHONE_NUMBER.initialize = function () {
    $('.PhoneNumberField').each(
        function (index, item) {
            var parent = $(item).parent()[0];
            $(parent).append(NS_DJANGO_PHONE_NUMBER.getContainer(item, NS_DJANGO_PHONE_NUMBER.guid()));
        }
    );
};
NS_DJANGO_PHONE_NUMBER.getContainer = function (item, guid) {
    //create container
    var $container = $(document.createElement('div'));
    $container.attr('data-guid', guid);
    $container.css('display', 'inline-block');
    var $item = $(item);
    $item.attr('data-control-guid', guid);
    $item.attr('type', 'hidden');
    $item.css('display', 'none');

    //create flag object with first country flag
    var $flag = $(document.createElement('span'));
    NS_DJANGO_PHONE_NUMBER.changeFlag($flag, NS_DJANGO_PHONE_NUMBER.ISO_3116_1_COUNTRY_CODE_LIST[0].Code);
    $container.append($flag);

    //create country code list  with first country selected
    var $select = $(document.createElement('select'));
    $select.attr('data-parent-guid', guid);
    $select.attr('class', 'pn-input country-code');
    for (var i = 0; i < NS_DJANGO_PHONE_NUMBER.ISO_3116_1_COUNTRY_CODE_LIST.length; i++) {
        var $option = $(document.createElement('option'));
        $option.html(NS_DJANGO_PHONE_NUMBER.ISO_3116_1_COUNTRY_CODE_LIST[i].Name);
        $option.val(NS_DJANGO_PHONE_NUMBER.ISO_3116_1_COUNTRY_CODE_LIST[i].Code);
        $select.append($option);
    }
    $select.on('change', NS_DJANGO_PHONE_NUMBER.onregionCodeChange);
    $container.append($select);

    //initialize visible control
    var $input = $(document.createElement('input'));
    $input.attr('class', 'pn-input');
    $input.attr('data-parent-guid', guid);
    $input.on('keyup', NS_DJANGO_PHONE_NUMBER.onPhoneNumberChange);

    console.log('initial', $(item).val());
    try {
        //initialize control with existing
        var initial = JSON.parse($(item).val());
        $input.val(initial.phoneNumber);
        $select.val(initial.regionCode);
        NS_DJANGO_PHONE_NUMBER.changeFlag($flag, initial.regionCode);

    } catch (ex) {
        //initialize control with first country code
        var default_region = $(item).attr('default_region_code');
        var region_code = NS_DJANGO_PHONE_NUMBER.ISO_3116_1_COUNTRY_CODE_LIST[0].Code;
        if (default_region !== 'None') {
            region_code = default_region;
            NS_DJANGO_PHONE_NUMBER.changeFlag($flag, region_code);
            $select.val(default_region);
        }
        var valueObject = new NS_DJANGO_PHONE_NUMBER.ValueObject(region_code);
        $(item).val(JSON.stringify(valueObject));
    }


    $container.append($input);
    return $container;
};
NS_DJANGO_PHONE_NUMBER.onregionCodeChange = function (event) {
    var $container = $('[data-guid="' + $(this).attr('data-parent-guid') + '"]');
    var $control = $('[data-control-guid="' + $(this).attr('data-parent-guid') + '"]');
    var $flag = $($container.find('.flag-icon')[0]);
    var $selected = $(this).find(":selected");
    //update control
    var regionCode = $selected.val();
    var valueObject = JSON.parse($control.val());
    valueObject.regionCode = regionCode;
    $control.val(JSON.stringify(valueObject));

    //update flag
    NS_DJANGO_PHONE_NUMBER.changeFlag($flag, regionCode);
};
NS_DJANGO_PHONE_NUMBER.onPhoneNumberChange = function (event) {
    var $control = $('[data-control-guid="' + $(this).attr('data-parent-guid') + '"]');
    //update control
    var valueObject = JSON.parse($control.val());
    valueObject.phoneNumber = $(this).val();
    $control.val(JSON.stringify(valueObject));
};
NS_DJANGO_PHONE_NUMBER.changeFlag = function (flag, regionCode) {
    var $flag = $(flag);
    $flag.attr(
        'class',
        'flag-icon flag-icon-' + regionCode.toLowerCase()
    );
};