from django import template
from django.conf import settings
from phonenumbers import NumberFormat
import phonenumbers
from django_phonenumbers.helper import PhoneNumber

register = template.Library()


@register.filter()
def phone_number_format(number, region_code=None):
    if type(number) is str:
        if region_code is None:
            return number
        try:
            new_number = phonenumbers.parse(number, region_code)
        except:
            return number

    elif type(number) is PhoneNumber:
        try:
            region_code = number.region_code
            new_number = phonenumbers.parse(number.phone_number, number.region_code)
        except:
            return number

    if hasattr(settings, 'PHONE_NUMBERS_FORMATS_BY_REGION'):
        region_pattern = settings.PHONE_NUMBERS_FORMATS_BY_REGION.get(region_code, None)
        if region_pattern is None:
            return phonenumbers.format_number(new_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        else:
            try:
                new_number_format = NumberFormat(
                    pattern=region_pattern.get('pattern'),
                    format=region_pattern.get('format')
                )
                new_number_format._mutable = True
                new_number_format.national_prefix_formatting_rule = region_pattern.get('prefix_format') % (
                    new_number.country_code, '$FG'
                )

                new_number_formats = [new_number_format]
                return phonenumbers.format_by_pattern(
                    new_number,
                    phonenumbers.PhoneNumberFormat.NATIONAL,
                    new_number_formats
                )
            except:
                return phonenumbers.format_number(new_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    return phonenumbers.format_number(new_number, phonenumbers.PhoneNumberFormat.NATIONAL)


@register.simple_tag()
def phone_number(number, region_code=None, pattern=None, number_format=None, prefix_format=None):
    """
        for number +995595119925
        pattern="(\\d{3})(\\d{2})(\\d{2})(\\d{2})", format="\\1 \\2-\\3-\\4"
        result 595 11-99-25
    """
    if pattern is None or number_format is None or prefix_format is None:
        return number
    if type(number) is PhoneNumber:
        try:
            number = phonenumbers.parse(number.phone_number, number.region_code)
        except:
            return number
    elif type(number) is str:
        if region_code is None:
            return number
        try:
            number = phonenumbers.parse(number, region_code)
        except:
            return number

    new_number_format = NumberFormat(pattern=pattern, format=number_format)
    new_number_format._mutable = True
    new_number_format.national_prefix_formatting_rule = prefix_format % (number.country_code, '$FG')
    new_number_formats = [new_number_format]
    return phonenumbers.format_by_pattern(
        number,
        phonenumbers.PhoneNumberFormat.NATIONAL,
        new_number_formats
    )
