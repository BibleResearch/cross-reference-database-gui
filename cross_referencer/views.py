from django.urls import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect

from .models import CrossReference
from .utility import create_bible_reference, normalize_bible_passage


class CrossReferenceListView(ListView):
    model = CrossReference


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
    fields = ['classification', 'explanation', 'sources']
    template_name_suffix = '_update_form'

    def get_success_url(self, **kwargs):
        return reverse('cross_referencer:details', args=(self.object.id,))

    def post(self, request, **kwargs):
        return self.save(request.POST, kwargs['pk'])

    def save(self, posted_data, object_id):
        # get all of the fields from the posted data
        starting_reference = posted_data.get('startingPassage')
        destination_reference = posted_data.get('destinationPassage')
        classification = posted_data.get('classification')
        explanation = posted_data.get('explanation')
        sources = posted_data.get('sources')

        # get a queryset with the current object - I am intentionally getting queryset rather than the object itself so that I can use the `update` function below
        current_object = CrossReference.objects.filter(pk=object_id)

        # update the metadata for the cross reference
        current_object.update(classification=classification, explanation=explanation, sources=sources)

        # if the start of the cross reference has changed, update it
        if normalize_bible_passage(starting_reference) != current_object[0].start:
            new_start = create_bible_reference(starting_reference)
            current_object.update(start=new_start)

        # if the destination of the cross reference has changed, update it
        if normalize_bible_passage(destination_reference) != current_object[0].destination:
            new_destination = create_bible_reference(destination_reference)
            current_object.update(destination=new_destination)

        return HttpResponseRedirect(reverse('cross_referencer:details', args=(current_object[0].id,)))


class CrossReferenceDeleteView(DeleteView):
    model = CrossReference
    success_url = reverse_lazy('cross_referencer:list')
