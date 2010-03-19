from django.db import models
from durationfield.db.models.fields.duration import DurationField

class TestModel(models.Model):
    duration_field = DurationField()

class TestNullableModel(models.Model):
    duration_field = DurationField(null=True, blank=True)