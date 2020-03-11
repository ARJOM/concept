from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import UUIDUser
from .forms import UUIDUserForm


# Dashboard
# - - - - - - - - - - - - - - - - - - - -
class DashboardView(TemplateView):
    template_name = 'dashboard.html'


# User list
# - - - - - - - - - - - - - - - - - - - -
class UsersView(ListView):
    model = UUIDUser
    template_name = 'core/list.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('core:dashboard')
        return super().get(request, *args, **kwargs)


# User create
# - - - - - - - - - - - - - - - - - - - -
class UserCreateView(CreateView):
    model = UUIDUser
    template_name = 'core/form.html'
    success_url = reverse_lazy('core:login')
    form_class = UUIDUserForm


# User edit
# - - - - - - - - - - - - - - - - - - - -
class UserEditView(UpdateView):
    model = UUIDUser
    template_name = 'core/update.html'
    success_url = reverse_lazy('core:list')
    form_class = UUIDUserForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff and kwargs['pk'] != request.user.id:
            return redirect('core:dashboard')
        return super().get(request, *args, **kwargs)


# User detail
# - - - - - - - - - - - - - - - - - - - -
class UserDetailView(DetailView):
    model = UUIDUser
    template_name = 'core/detail.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff and kwargs['pk'] != request.user.id:
            return redirect('core:dashboard')
        return super().get(request, *args, **kwargs)


# User delete
# - - - - - - - - - - - - - - - - - - - -
def user_delete_view(request, pk):
    if not request.user.is_staff and request.user.id != pk:
        return redirect('core:dashboard')
    user = UUIDUser.objects.get(id=pk)
    user.delete()
    return redirect('core:dashboard')
