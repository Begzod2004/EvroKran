from django.core.exceptions import ValidationError
from django.db import models
import phonenumbers
from django_phonenumbers import helper
from django_phonenumbers.form import fields


class PhoneNumberField(models.Field):
    def validate(self, value, model_instance):
        helper.validate_phone_number(value, ValidationError)

    def pre_save(self, model_instance, add):
        field = model_instance.__getattribute__(self.attname)  # type: fields.PhoneNumber
        if field is not None:
            value = phonenumbers.parse(field.phone_number, field.region_code)
            value = phonenumbers.format_number(value, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            model_instance.__setattr__(self.attname, value)
            return value
        return None

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return helper.PhoneNumber()
        return helper.PhoneNumber().from_string(_string=value)

    def to_python(self, value):
        if type(value) is helper.PhoneNumber:
            return value
        if type(value) is str:
            return helper.PhoneNumber().from_string(_string=value)

    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        defaults = {'form_class': fields.PhoneNumberField}
        defaults.update(kwargs)
        return super().formfield(**defaults)

    def db_type(self, connection):
        return 'char(%s)' % (self.max_length if self.max_length else str(100),)
