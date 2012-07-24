"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import datetime
from core.models import Year, Michaelmas, Hilary, Trinity

class SimpleTest(TestCase):
    def setUp(self):
        today = datetime.date.today()
        self.year = Year.objects.create(year = today.year)
        self.michaelmas = Michaelmas.objects.create(startDate = today-datetime.timedelta(3),
            endDate = today - datetime.timedelta(2),
            year = self.year)
        self.hilary = Hilary.objects.create(startDate = today - datetime.timedelta(1),
            endDate = today + datetime.timedelta(1),
            year = self.year)
        self.trinity = Trinity.objects.create(startDate = today + datetime.timedelta(2),
            endDate = today + datetime.timedelta(3),
            year = self.year)

    def test_get_current_term(self):
            self.assertEqual(self.hilary, dates.getCurrentTerm())

    def test_get_current_year(self):
        self.assertEqual(self.year, dates.getCurrentYear())
