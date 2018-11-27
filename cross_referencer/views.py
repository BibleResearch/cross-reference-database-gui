from django.urls import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect

from .models import CrossReference
from .utility import create_bible_reference


class CrossReferenceListView(ListView):
    model = CrossReference
    # TODO: do I need pagination?
    paginate_by = 100  # if pagination is desired

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context


class CrossReferenceCreateView(CreateView):
    model = CrossReference
    fields = ['classification', 'explanation', 'sources']

    def post(self, request, **kwargs):
        if request.POST.get('startingPassage') and request.POST.get('destinationPassage'):
            return self.save(request.POST)
        else:
            # TODO: add an error message here...
            return HttpResponseRedirect(reverse('cross_referencer:list'))

    def save(self, posted_data):
        # TODO: add normalization of passages here...
        starting_reference = create_bible_reference(posted_data.get('startingPassage'))
        destination_reference = create_bible_reference(posted_data.get('destinationPassage'))

        classification = posted_data.get('classification')
        explanation = posted_data.get('explanation')
        sources = posted_data.get('sources')

        new_reference = CrossReference(classification=classification, explanation=explanation, sources=sources, start=starting_reference, destination=destination_reference)
        new_reference.save()
        return HttpResponseRedirect(reverse('cross_referencer:details', args=(new_reference.id,)))


class CrossReferenceDetailView(DetailView):
    model = CrossReference

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CrossReferenceEditView(UpdateView):
    model = CrossReference
    fields = ['name']
    # TODO: not sure if I need this
    # template_name_suffix = '_update_form'


class CrossReferenceDeleteView(DeleteView):
    model = CrossReference
    success_url = reverse_lazy('list')
