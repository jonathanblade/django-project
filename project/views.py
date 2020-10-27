import git
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.decorators.csrf import csrf_exempt
from publications.models import Publication

class HomePageView(TemplateView):
    template_name = "home.html"

class EducationPageView(TemplateView):
    template_name = "education.html"

class PublicationsPageView(ListView):
    template_name = "publications.html"
    model = Publication
    ordering = ["-year"]
    
@csrf_exempt
def webhook(request):
    if request.method == "POST":
        repo = git.Repo("/home/jonathanblade/django-project")
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)