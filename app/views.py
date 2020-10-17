from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class NewsPageView(TemplateView):
    template_name = "news.html"