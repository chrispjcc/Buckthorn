from django.utils.datetime_safe import datetime
from core.models import Term, Year

def getCurrentTerm():
    try:
        out = Term.objects.get(startDate__lte=datetime.now(),endDate__gte=datetime.now())
        try:
            return out.michaelmas
        except models.Michaelmas.DoesNotExist:
            pass

        try:
            return out.hilary
        except models.Hilary.DoesNotExist:
            pass

        try:
            return out.trinity
        except models.Trinity.DoesNotExist:
            pass

    except Term.DoesNotExist:
        pass

    return None

def getCurrentYear():
    try:
        return Year.objects.get(michaelmas__startDate__lte=datetime.now(),trinity__endDate__gte=datetime.now())
    except Year.DoesNotExist:
        return None
