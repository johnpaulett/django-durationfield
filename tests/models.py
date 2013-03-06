import datetime
from django.db import models
from durationfield.db.models.fields.duration import DurationField

DEFAULT_DURATION = datetime.timedelta(days=730)


class TestModel(models.Model):
    duration_field = DurationField()


class TestNullableModel(models.Model):
    duration_field = DurationField(null=True, blank=True)


class TestDefaultModel(models.Model):
    duration_field = DurationField(default=DEFAULT_DURATION)
