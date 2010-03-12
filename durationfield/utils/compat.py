def localize_input(value, default=None):
    """
    A hacky backport of Django's 1.2 formats function. Doesn't attempt to localize Date.
    See: http://code.djangoproject.com/browser/django/trunk/django/utils/formats.py
    """
    return value
