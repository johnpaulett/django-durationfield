from django.test import TestCase
from django.core import serializers
from durationfield.tests.models import TestModel, TestNullableModel
from durationfield.utils import timestring
from datetime import timedelta
    
class DurationFieldTests(TestCase):

    def setUp(self):
        self.test_data = (
            [u"8h", timedelta(microseconds=28800000000L)],
            [u"6w 3d 18h 30min 23s 10ms 150us", timedelta(microseconds=3954623010150L)],
        )
        
        self.month_year_test_data = (
            u"1y 7m 6w 3d 18h 30min 23s 10ms 150us",
        )
        
        return super(DurationFieldTests, self).setUp()
    
    def testTimedeltaRoundtrip(self):
        for value in self.test_data:
            time = timestring.to_timedelta(value[0])
            new_value = timestring.from_timedelta(time)
            self.assertEquals(value[0], new_value)
            
    def testUnitNormalization(self):
        self.assertEquals(timestring.from_timedelta(timestring.to_timedelta("1000us")), "1ms")
        self.assertEquals(timestring.from_timedelta(timestring.to_timedelta("1000ms")), "1s")
        self.assertEquals(timestring.from_timedelta(timestring.to_timedelta("60s")), "1min")
        self.assertEquals(timestring.from_timedelta(timestring.to_timedelta("60min")), "1h")
        self.assertEquals(timestring.from_timedelta(timestring.to_timedelta("24h")), "1d")
        self.assertEquals(timestring.from_timedelta(timestring.to_timedelta("7d")), "1w")
        
    
    def testDataStability(self):
        """
        Data should remain the same when taking a round trip to and from the db
        """
        for value in self.test_data:
            model_test = TestModel()
            model_test.duration_field = timestring.to_timedelta(value[0])
            model_test.save()
            model_test = TestModel.objects.get(id__exact=model_test.id)
            self.assertEquals(value[1], model_test.duration_field)
            model_test.delete()
   
    def testDefaultValue(self):
        """
        Default value should be empty and fetchable
        """
        model_test = TestNullableModel()
        model_test.save()
        model_test = TestNullableModel.objects.get(id__exact=model_test.id)
        self.assertEquals(None, model_test.duration_field)
        model_test.delete()

    def testApplicationType(self):
        """
        Timedeltas should be returned to the applciation
        """
        model_test = TestModel()
        td = timedelta(microseconds=1234567890)
        model_test.duration_field = td
        model_test.save()
        model_test = TestModel.objects.get(id__exact=model_test.id)
        self.assertEquals(td, model_test.duration_field)
        model_test.delete()
        
        # Test with strings
        model_test = TestModel()
        td = "8d"
        model_test.duration_field = td
        model_test.save()
        model_test = TestModel.objects.get(id__exact=model_test.id)
        self.assertEquals(timedelta(days=8), model_test.duration_field)
        model_test.delete()
        
        # Test with long
        model_test = TestModel()
        td = 28800000000L
        model_test.duration_field = td
        model_test.save()
        model_test = TestModel.objects.get(id__exact=model_test.id)
        self.assertEquals(timedelta(microseconds=td), model_test.duration_field)
        model_test.delete()
    
    def testForm(self):
        model_test = TestModel()
        model_test.duration_field = timestring.to_timedelta("3d 8h 56s")
        model_test.save()
        model_test = TestModel.objects.get(id__exact=1)
        
        #form = DurationField()
        #self.assertContains("input", str)










