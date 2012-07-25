"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import datetime
import core
from core.models import Trinity, Hilary, Michaelmas, Year, Course, Module, LectureSeries, Lecturer, Student, Lecture

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
        self.course = Course.objects.create(name = 'Test Course', number_of_years = 4)
        self.module = Module.objects.create(name = 'Test Module', course = self.course)
        self.lecturer = Lecturer.objects.create(name = 'John Lecturer')
        self.student = Student.objects.create(name = 'Bobby Student', course = self.course, finish_year = 2013)
        self.lecture_series = LectureSeries.objects.create(name = 'Test Lectures', module = self.module, lecturer = self.lecturer)
        self.lecture = Lecture.objects.create(series = self.lecture_series, date = today, start_time = datetime.time(10,00,00), end_time = datetime.time(11,00,00))

    def test_get_current_term(self):
        self.assertEqual(self.hilary, core.getCurrentTerm())

    def test_michaelmas_name(self):
        self.assertEqual(unicode(self.michaelmas), u'Michaelmas ' + unicode(self.year.start_year()))

    def test_hilary_name(self):
        self.assertEqual(unicode(self.hilary), u'Hilary ' + unicode(self.year.end_year()))

    def test_trinity_name(self):
        self.assertEqual(unicode(self.trinity), u'Trinity ' + unicode(self.year.end_year()))

    def test_get_current_year(self):
        self.assertEqual(self.year, core.getCurrentYear())

    def test_student_name(self):
        self.assertEqual(unicode(self.student), u'Bobby Student')

    def test_lecturer_name(self):
        self.assertEqual(unicode(self.lecturer), u'John Lecturer')