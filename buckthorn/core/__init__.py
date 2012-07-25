import datetime
from core.models import Term, Year

def getCurrentTerm():
    try:
        out = Term.objects.get(startDate__lte=datetime.date.today(),endDate__gte=datetime.date.today())
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
        return Year.objects.get(michaelmas__startDate__lte=datetime.date.today(),trinity__endDate__gte=datetime.date.today())
    except Year.DoesNotExist:
        return None
