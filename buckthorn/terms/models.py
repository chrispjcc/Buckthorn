from django.db import models

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
        return None
