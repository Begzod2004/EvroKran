from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.exceptions import ImproperlyConfigured

from django.forms.widgets import TextInput


class PhoneNumberWidget(TextInput):
    def __init__(self, *args, **kwargs):
        default_region = settings.PHONE_NUMBER_REGION if hasattr(
            settings,
            'PHONE_NUMBER_REGION'
        ) else None
        kwargs.update(
            {
                'attrs': {
                    'class': 'PhoneNumberField pn-input',
                    'default_region_code': default_region
                }
            }
        )
        super().__init__(*args, **kwargs)

    class Media:
        try:
            css = {
                'all': (
                    'django_phonenumbers/flag-icon-css-master/css/flag-icon.min.css',
                    'django_phonenumbers/css/style.css'
                ),
            }

            js = (
                static('django_phonenumbers/js/jquery-2.1.4.min.js'),
                static('django_phonenumbers/js/iso_3166_1_country_code_list.js'),
                static('django_phonenumbers/js/__init__.js'),
            )

        except AttributeError:
            raise ImproperlyConfigured("error")
