from django.test import TestCase
from django.core import serializers
from durationfield.tests.models import (
    TestModel,
    TestNullableModel,
    TestDefaultModel,
    DEFAULT_DURATION
)
from durationfield.utils import timestring
from datetime import timedelta

class DurationFieldTests(TestCase):

    def setUp(self):
        self.test_tds = [
            timedelta(hours=1), # No days, no micro, single-digit hour
            timedelta(hours=10), # double-digit hour
            timedelta(hours=10, minutes=35, seconds=1),
            timedelta(days=1), # Day, no micro
            timedelta(days=1, microseconds=1), # Day, with micro
            timedelta(days=10), # Days, no micro
            timedelta(days=10, microseconds=1), # Days, with micro
        ]

        return super(DurationFieldTests, self).setUp()

    def _delta_to_microseconds(self, td):
        """
        Get the tota number of microseconds in a timedelta, normalizing days and
        seconds to microseconds.
        """
        SECONDS_TO_US = 1000 * 1000
        MINUTES_TO_US = SECONDS_TO_US * 60
        HOURS_TO_US = MINUTES_TO_US * 60
        DAYS_TO_US = HOURS_TO_US * 24

        td_in_ms = td.days * DAYS_TO_US + td.seconds * SECONDS_TO_US + td.microseconds
        self.assertEqual(timedelta(microseconds=td_in_ms), td)

        return td_in_ms

    def testTimedeltaStrRoundtrip(self):
        for td in self.test_tds:
            td_str = str(td)
            td_from_str = timestring.str_to_timedelta(td_str)
            self.assertEquals(td_from_str, td)

    def testDbRoundTrip(self):
        """
        Data should remain the same when taking a round trip to and from the db
        """
        models = [TestModel, TestNullableModel, TestDefaultModel]

        for td in self.test_tds:
            for ModelClass in models:
                tm = ModelClass()
                tm.duration_field = td
                tm.save()

                tm_saved = ModelClass.objects.get(pk=tm.pk)
                self.assertEqual(tm_saved.duration_field, tm.duration_field)

    def testDefaultValue(self):
        """
        Default value should be empty and fetchable
        """
        model_test = TestNullableModel()
        model_test.save()
        model_test_saved = TestNullableModel.objects.get(pk=model_test.pk)

        self.assertEquals(model_test.duration_field, None)
        self.assertEquals(model_test_saved.duration_field, None)

    def testDefaultGiven(self):
        """
        Default value should use the default argument
        """
        model_test = TestDefaultModel()
        model_test.save()

        model_test_saved = TestDefaultModel.objects.get(pk=model_test.pk)
        self.assertEquals(model_test.duration_field, DEFAULT_DURATION)
        self.assertEquals(model_test_saved.duration_field, DEFAULT_DURATION)

    def testApplicationType(self):
        """
        Timedeltas should be returned to the applciation
        """
        for td in self.test_tds:
            model_test = TestModel()
            model_test.duration_field = td
            model_test.save()
            model_test = TestModel.objects.get(pk=model_test.pk)
            self.assertEquals(td, model_test.duration_field)

            # Test with strings
            model_test = TestModel()
            model_test.duration_field = str(td)
            model_test.save()
            model_test = TestModel.objects.get(pk=model_test.pk)
            self.assertEquals(td, model_test.duration_field)

            td_in_ms = self._delta_to_microseconds(td)

            # Test with int
            model_test = TestModel()
            model_test.duration_field = td_in_ms
            model_test.save()
            model_test = TestModel.objects.get(pk=model_test.pk)
            self.assertEquals(td, model_test.duration_field)

            # Test with long
            model_test = TestModel()
            model_test.duration_field = long(td_in_ms)
            model_test.save()
            model_test = TestModel.objects.get(pk=model_test.pk)
            self.assertEquals(td, model_test.duration_field)

    #def testForm(self):
        #model_test = TestModel()
        #model_test.duration_field = timestring.to_timedelta("3d 8h 56s")
        #model_test.save()
        #model_test = TestModel.objects.get(id__exact=1)

        ##form = DurationField()
        ##self.assertContains("input", str)





