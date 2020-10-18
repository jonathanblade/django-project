import git
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

class HomePageView(TemplateView):
    template_name = "home.html"

class EducationPageView(TemplateView):
    template_name = "education.html"

@csrf_exempt
def webhook(request):
    if request.method == "POST":
        repo = git.Repo("/home/jonathanblade/django-project")
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)