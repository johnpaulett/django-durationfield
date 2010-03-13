from django.forms.fields import Field
from django.core.exceptions import ValidationError
from durationfield.utils.timestring import to_timedelta
from django.utils.translation import ugettext_lazy as _
from widgets import DurationInput


class DurationField(Field):
    widget = DurationInput
    default_error_messages = {
        'invalid': u'Enter a valid duration.',
        'max_value': _(u'Ensure this value is less than or equal to %(limit_value)s.'),
        'min_value': _(u'Ensure this value is greater than or equal to %(limit_value)s.'),
    }
 
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        super(DurationField, self).__init__(*args, **kwargs)

        if max_value is not None:
            self.validators.append(validators.MaxValueValidator(max_value))
        if min_value is not None:
            self.validators.append(validators.MinValueValidator(min_value))

    def clean(self, value):
        """
        Validates max_value and min_value.
        Returns a datetime.timedelta object.
        """
        try:
            return to_timedelta(value)
        except ValueError, e:
            raise ValidationError(e)

        if self.max_value is not None and value > self.max_value:
            raise ValidationError(self.error_messages['max_value'] % {'max': self.max_value})

        if self.min_value is not None and value < self.min_value:
            raise ValidationError(self.error_messages['min_value'] % {'min': self.min_value})

        return value

    def to_python(self, value):
        try:
            return to_timedelta(value)
        except ValueError, e:
            raise ValidationError(e)

