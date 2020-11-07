import git
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.decorators.csrf import csrf_exempt
from publications.models import Publication

class Home(TemplateView):
    template_name = 'home.html'

class Education(TemplateView):
    template_name = 'education.html'

class Publications(ListView):
    template_name = 'publications.html'
    model = Publication
    context_object_name = 'publications'
    ordering = ['-year']
    
@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        repo = git.Repo('/home/jonathanblade/django-project')
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)