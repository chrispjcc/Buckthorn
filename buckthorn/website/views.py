from django.http import HttpResponse
from django.template.context import Context
from django.template.loader import get_template
from terms.models import Term

def home(request):
    template = get_template('main_page.html')
    variables = Context({
        'head_title' : 'PJCC Webpage',
        'page_title' : 'Welcome to the PJCC site.',
        'page_body' : 'The current term is: ' + (Term.getCurrentTerm() and unicode(Term.getCurrentTerm()) or 'None'),
        })
    output = template.render(variables)
    return HttpResponse(output)