from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Concept, Item, Game


# Concept list
# - - - - - - - - - - - - - - - - - - - -
class ConceptsView(ListView):

    model = Concept
    template_name = 'game/concept/list.html'


# Concept create
# - - - - - - - - - - - - - - - - - - - -
class ConceptCreateView(CreateView):

    model = Concept
    template_name = 'game/concept/form.html'
    success_url = reverse_lazy('game:concept-list')
    fields = ['name']


# Concept edit
# - - - - - - - - - - - - - - - - - - - -
class ConceptEditView(UpdateView):

    model = Concept
    template_name = 'game/concept/update.html'
    success_url = reverse_lazy('game:concept-list')
    fields = ['name']


# Concept delete
# - - - - - - - - - - - - - - - - - - - -
def concept_delete_view(request, pk):

    concept = Concept.objects.get(id=pk)
    concept.delete()
    return redirect('game:concept-list')
