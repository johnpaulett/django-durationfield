# -*- coding: utf-8 -*-
from django.forms.util import flatatt
from django.forms.widgets import TextInput
from django.utils.translation import ugettext
from django.utils.encoding import StrAndUnicode, force_unicode
from django.utils.safestring import mark_safe
from django.utils import datetime_safe
try:
    from django.utils import formats
except ImportError:
    # For Django 1.1 compatibility
    from durationfield.utils import compat as formats
from datetime import timedelta
from durationfield.utils.timestring import from_timedelta
from urlparse import urljoin
 
#-            output.append(u'<li><label%s>%s %s</label></li>' % (label_for, rendered_cb, option_label))
#+            output.append(u'<li>%(cb)s<label%(for)s>%(label)s</label></li>' % {"for": label_for, "label": option_label, "cb": rendered_cb})


class DurationInput(TextInput):
    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            if isinstance(value, int) or isinstance(value, long): # Database backends serving different types
                value = from_timedelta(timedelta(microseconds=value))
            final_attrs['value'] = force_unicode(formats.localize_input(value))
        return mark_safe(u'<input%s />' % flatatt(final_attrs))
 
