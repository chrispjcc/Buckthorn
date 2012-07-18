from django.db import models
from django.utils.datetime_safe import datetime

class Term(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    CODE_CHOICES = (
        ('MT','Michaelmas'),
        ('HT','Hilary'),
        ('TT','Trinity'),
    )
    code = models.CharField(max_length=2,choices=CODE_CHOICES)
    year = models.IntegerField()

    def __unicode__(self):
        return u'%s%s' % (self.code, self.year)

    @staticmethod
    def getCurrentTerm():
        return Term.objects.get(startDate__lte=datetime.now(),endDate__gte=datetime.now())
