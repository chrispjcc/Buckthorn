from django.http import HttpResponse
from django.template.context import Context
from django.template.loader import get_template
import dates

def home(request):
    template = get_template('main_page.html')
    variables = Context({
        'head_title' : 'PJCC Webpage',
        'page_title' : 'Welcome to the PJCC site.',
        'term_text' : 'The current term is: ' + (dates.getCurrentTerm() and unicode(dates.getCurrentTerm()) or 'None'),
        'year_text' : 'The current year is: ' + (dates.getCurrentYear() and unicode(dates.getCurrentYear()) or 'None'),
        })
    output = template.render(variables)
    return HttpResponse(output)