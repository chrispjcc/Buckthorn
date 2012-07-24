from django.http import HttpResponse
from django.template.context import Context
from django.template.loader import get_template
import core

def home(request):
    template = get_template('main_page.html')
    variables = Context({
        'head_title' : 'PJCC Webpage',
        'page_title' : 'Welcome to the PJCC site.',
        'term_text' : 'The current term is: ' + (core.getCurrentTerm() and unicode(core.getCurrentTerm()) or 'None'),
        'year_text' : 'The current year is: ' + (core.getCurrentYear() and unicode(core.getCurrentYear()) or 'None'),
        })
    output = template.render(variables)
    return HttpResponse(output)