from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class DashboardView(TemplateView):
    template_name = "dashboard.html"

class Error404View(TemplateView):
    template_name = "page_404.html"
