import json
from phonenumbers.phonenumberutil import NumberParseException, PhoneNumberType
import phonenumbers


class PhoneNumber:
    def __init__(self, country_code=None, region_code=None, phone_number=None):
        """
        :type country_code: str
        :type region_code: str
        :type phone_number: str
        """
        self.country_code = country_code
        self.google_phone_number = None
        self.region_code = region_code
        self.phone_number = phone_number

    def __repr__(self):
        return '%s %s' % (
            self.country_code, self.phone_number
        )

    def __str__(self):
        return self.__repr__()

    def from_string(self, _string):
        """
        :type _string:str
        """
        self.country_code, self.phone_number = _string.strip().split(' ', maxsplit=1)
        self.region_code = phonenumbers.region_code_for_country_code(int(self.country_code))
        return self

    def from_json(self, _json):
        value = json.loads(_json)
        self.region_code = value.get('regionCode')
        self.phone_number = value.get('phoneNumber')
        self.country_code = phonenumbers.country_code_for_region(self.region_code)
        return self

    def to_json(self):
        return '{"regionCode":"%s","countryCode":"%s","phoneNumber":"%s"}' % (
            phonenumbers.region_code_for_country_code(int(self.country_code)),
            self.country_code, self.phone_number
        )


def validate_phone_number(value, validation_error_class):
    """
    :type value:fields.PhoneNumber
    :return:
    """
    assert type(value) is PhoneNumber, "%s instance was supplied instead of PhoneNumber " % (type(value),)
    try:
        value.region_code = phonenumbers.region_code_for_country_code(int(value.country_code))
        value.google_phone_number = phonenumbers.parse(value.phone_number, value.region_code)
        value.country_code = value.google_phone_number.country_code
        if not phonenumbers.is_valid_number(value.google_phone_number):
            fixed = phonenumbers.format_number(phonenumbers.example_number_for_type(
                value.region_code,
                PhoneNumberType.FIXED_LINE
            ), phonenumbers.PhoneNumberFormat.NATIONAL)
            mobile = phonenumbers.format_number(phonenumbers.example_number_for_type(
                value.region_code,
                PhoneNumberType.MOBILE
            ), phonenumbers.PhoneNumberFormat.NATIONAL)
            raise validation_error_class(
                'Invalid number. format example are: ' +
                'for fixed line  %(fixed_example)s, for mobile %(mobile_example)s',
                code='invalid',
                params={
                    'fixed_example': fixed if fixed else 'no example',
                    'mobile_example': mobile if mobile else 'no example'
                }
            )
    except NumberParseException as ex:
        raise validation_error_class(str(ex))
    except validation_error_class as ex:
        raise ex
    return value
