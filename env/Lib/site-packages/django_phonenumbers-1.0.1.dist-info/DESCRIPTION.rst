Installation
============

::

    run  pip install django_phonenumbers

Configure settings.py
======================

::

     Add django_phonenumbers to INSTALLED_APPS

manage.py
=========

::

     run manage.py collectstatic

settings.py
===========


.. code:: python

        PHONE_NUMBER_REGION = 'GE'  
        PHONE_NUMBERS_FORMATS_BY_REGION = {
            'GE': {
                'pattern': '(\\d{3})(\\d{2})(\\d{2})(\\d{2})', 'format': '\\1 \\2-\\3-\\4', 'prefix_format': '+%s (%s)'
            },
            'US': {
                'pattern': '(\\d{3})(\\d{3})(\\d{4})', 'format': '\\1 \\2-\\3', 'prefix_format': '+%s (%s)'
            },
        }


Template example
================

.. code:: html

    {% load croppingtools_extra %}
    <li>
                {{ number.phone_number }}
                // {{ number.phone_number.region_code }}
                // {{ number.phone_number.country_code }}
                // {{ number.phone_number.phone_number }}
                <div>
                    {% load phone_numbers_extra %}
                    <h4>Filter
                        <small>{{ number.phone_number|phone_number_format }}</small>
                    </h4>
                    <h4>Simple tag
                        <small>
                            {% phone_number number.phone_number pattern='(\\d{3})(\\d{3})(\\d{3})' number_format='\\1 \\2-\\3' prefix_format='+%s (%s)' %}
                        </small>
                    </h4>
                </div>
    </li>



