# -*- coding: utf-8 -*-
from django.forms.util import flatatt
from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
try:
    from django.utils import formats
except ImportError:
    # For Django 1.1 compatibility
    from durationfield.utils import compat as formats
from datetime import timedelta


class DurationInput(TextInput):
    def render(self, name, value, attrs=None):
        """
        output.append(u'<li>%(cb)s<label%(for)s>%(label)s</label></li>' % {"for": label_for, "label": option_label, "cb": rendered_cb})
        """
        if value is None: value = u''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != u'':
            # Only add the 'value' attribute if a value is non-empty.
            if isinstance(value, int) or isinstance(value, long): # Database backends serving different types
                value = timedelta(microseconds=value)

            # Otherwise, we've got a timedelta already

            final_attrs['value'] = force_unicode(formats.localize_input(value))
        return mark_safe(u'<input%s />' % flatatt(final_attrs))

