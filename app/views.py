import git
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

class HomePageView(TemplateView):
    template_name = "home.html"

class NewsPageView(TemplateView):
    template_name = "news.html"

@csrf_exempt
def webhook(request):
    if request.method == "POST":
        repo = git.Repo("/home/jonathanblade/django-project")
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse("Updated PythonAnywhere successfully")
    else:
        return HttpResponse("Wrong event type")