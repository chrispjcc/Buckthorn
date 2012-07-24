from django.db import models
from django.utils.datetime_safe import datetime

def generate_years():
    def tuplify(x): return (x,str(x) + '-' + str(x+1))   # str(x) if needed
    current_year = datetime.now().year
    return map(tuplify, range(2010, current_year + 1))  # range(1,4) gives [1,2,3]

class Year(models.Model):
    ''' Resource used for years tuple:
    http://stackoverflow.com/questions/1517474/only-showing-year-in-django-admin-a-yearfield-instead-of-datefield'''
    year = models.IntegerField(unique=True,choices = generate_years())

    def start_year(self):
        return self.year

    def end_year(self):
        return self.year + 1

    def __unicode__(self):
        return u'%s-%s' % (self.year, self.year + 1)


class Term(models.Model):

    startDate = models.DateField()
    endDate = models.DateField()

class Michaelmas(Term):
    year = models.OneToOneField(Year,related_name='michaelmas')

    def __unicode__(self):
        return u'%s %s' % ('Michaelmas', self.year.start_year())

class Hilary(Term):
    year = models.OneToOneField(Year,related_name='hilary')

    def __unicode__(self):
        return u'%s %s' % ('Hilary', self.year.end_year())

class Trinity(Term):
    year = models.OneToOneField(Year,related_name='trinity')

    def __unicode__(self):
        return u'%s %s' % ('Trinity', self.year.end_year())

