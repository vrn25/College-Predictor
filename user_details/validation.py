from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_zero(value):
    if value == 0:
        raise ValidationError(
            _('%(value)s cannot be 0'),
            params={'value': value},
        )




