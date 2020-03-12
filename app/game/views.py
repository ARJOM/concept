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
        kwargs['type'] = "Active"
        return super(ConceptsView, self).get_context_data(**kwargs)


# Concept deleted list
class ConceptsDeletedView(ConceptsView):

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['object_list'] = Concept.objects.filter(active=False)
        kwargs['type'] = "Inactive"
        return super(ConceptsDeletedView, self).get_context_data(**kwargs)


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


# Concept activate
# - - - - - - - - - - - - - - - - - - - -
def concept_activate_view(request, pk):
    if not request.user.is_staff:
        return redirect('core:dashboard')
    concept = Concept.objects.get(id=pk)
    concept.active = True
    concept.save()
    return redirect('game:concept-list')


# Items list
# - - - - - - - - - - - - - - - - - - - -
class ItemsView(ListView):
    model = Item
    template_name = 'game/item/list.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('core:dashboard')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['object_list'] = Item.objects.filter(active=True)
        kwargs['type'] = "Active"
        return super(ItemsView, self).get_context_data(**kwargs)


# Items deleted list
# - - - - - - - - - - - - - - - - - - - -
class ItemsDeletedView(ItemsView):

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['object_list'] = Item.objects.filter(active=False)
        kwargs['type'] = "Inactive"
        return super(ItemsDeletedView, self).get_context_data(**kwargs)


# Item register
# - - - - - - - - - - - - - - - - - - - -
class ItemCreateView(CreateView):
    model = Item
    template_name = 'game/item/form.html'
    fields = ['name']

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('core:dashboard')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['concepts'] = Concept.objects.all()
        return super(ItemCreateView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        # Creating a instance of item
        item = Item()
        # Setting the name by the form
        item.name = request.POST.get('name')
        item.save()
        # Going through concepts and checking if they are marked
        concepts = []
        for concept in Concept.objects.all():
            con = request.POST.get(concept.name)
            if con is not None:
                c = Concept.objects.get(id=con)
                c.save()
                concepts.append(c)
        # Setting concepts in Item instance
        item.concepts.set(concepts)
        item.save()
        return redirect('game:item-list')


# Item edit
# - - - - - - - - - - - - - - - - - - - -
class ItemEditView(UpdateView):
    model = Item
    template_name = 'game/item/update.html'
    success_url = reverse_lazy('game:item-list')
    fields = ['name', 'concepts']

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('core:dashboard')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['concepts'] = Concept.objects.all()
        kwargs['marked'] = Item.objects.get(id=self.object.id).concepts.filter()
        return super(ItemEditView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        item = self.get_object()
        if item.name != request.POST.get('name'):
            item.name = request.POST.get('name')
            item.save()
        # Going through concepts and checking if they are marked
        concepts = []
        for concept in Concept.objects.all():
            con = request.POST.get(concept.name)
            if con is not None:
                c = Concept.objects.get(id=con)
                c.save()
                concepts.append(c)
        # Setting concepts in Item instance
        item.concepts.set(concepts)
        item.save()
        return redirect('game:item-list')


# Concept delete
# - - - - - - - - - - - - - - - - - - - -
def item_delete_view(request, pk):
    if not request.user.is_staff:
        return redirect('core:dashboard')
    item = Item.objects.get(id=pk)
    item.active = False
    item.save()
    return redirect('game:item-list')


# Concept activate
# - - - - - - - - - - - - - - - - - - - -
def item_activate_view(request, pk):
    if not request.user.is_staff:
        return redirect('core:dashboard')
    item = Item.objects.get(id=pk)
    item.active = True
    item.save()
    return redirect('game:item-list')
