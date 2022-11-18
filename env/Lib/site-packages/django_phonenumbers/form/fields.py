import phonenumbers
from django import forms
from django_phonenumbers.widgets import PhoneNumberWidget
from django_phonenumbers.helper import PhoneNumber, validate_phone_number


class PhoneNumberField(forms.Field):
    def __init__(self, *args, **kwargs):
        kwargs.update(
            {
                'widget': PhoneNumberWidget()
            }
        )
        super().__init__(*args, **kwargs)

    def prepare_value(self, value):
        """
        :type value: PhoneNumber
        :rtype: str
        """
        if type(value) is PhoneNumber:
            return value.to_json()
        elif type(value) is str:
            return value
        else:
            return None

    def to_python(self, value):
        """Normalize data to a list of strings."""

        # Return an empty list if no input was given.
        if not value:
            return None
        return PhoneNumber().from_json(_json=value)

    def validate(self, value: 'PhoneNumber'):
        """Check if value consists only of valid phone numbers."""
        return validate_phone_number(value, forms.ValidationError)

    def clean(self, value):
        value = self.to_python(value)  # type: PhoneFieldParameter
        value = self.validate(value)
        return str(PhoneNumber(
            region_code=value.region_code,
            country_code=value.country_code,
            phone_number=phonenumbers.format_number(value.google_phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        ))
