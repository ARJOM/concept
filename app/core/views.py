from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import UUIDUser
from .forms import UUIDUserForm

# User list
# - - - - - - - - - - - - - - - - - - - -
class UsersView(ListView):
    model = UUIDUser
    template_name = 'core/list.html'


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
    success_url = reverse_lazy('/')
    fields = ['username', 'email', 'password']


# User detail
class UserDetailView(DetailView):
    model = UUIDUser
    template_name = 'core/detail.html'
