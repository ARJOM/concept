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

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('core:dashboard')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['object_list'] = Concept.objects.filter(active=True)
        return super(ConceptsView, self).get_context_data(**kwargs)


# Concept create
# - - - - - - - - - - - - - - - - - - - -
class ConceptCreateView(CreateView):
    model = Concept
    template_name = 'game/concept/form.html'
    success_url = reverse_lazy('game:concept-list')
    fields = ['name']

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('core:dashboard')
        return super().get(request, *args, **kwargs)


# Concept edit
# - - - - - - - - - - - - - - - - - - - -
class ConceptEditView(UpdateView):
    model = Concept
    template_name = 'game/concept/update.html'
    success_url = reverse_lazy('game:concept-list')
    fields = ['name']

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('core:dashboard')
        return super().get(request, *args, **kwargs)


# Concept delete
# - - - - - - - - - - - - - - - - - - - -
def concept_delete_view(request, pk):
    if not request.user.is_staff:
        return redirect('core:dashboard')
    concept = Concept.objects.get(id=pk)
    concept.active = False
    concept.save()
    return redirect('game:concept-list')
