from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'bible_cross_reference_database/index.html'


class AboutView(generic.TemplateView):
    template_name = 'bible_cross_reference_database/about.html'
