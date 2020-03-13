from django.contrib.auth import login, authenticate
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

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('core:login')
        return super().get(request, *args, **kwargs)


# User list
# - - - - - - - - - - - - - - - - - - - -
class UsersView(ListView):
    model = UUIDUser
    template_name = 'core/list.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('core:dashboard')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['object_list'] = UUIDUser.objects.filter(active=True)
        kwargs['type'] = "Active"
        return super(UsersView, self).get_context_data(**kwargs)


# User deleted list
class UsersDeletedView(UsersView):

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['object_list'] = UUIDUser.objects.filter(active=False)
        kwargs['type'] = "Inactive"
        return super(UsersDeletedView, self).get_context_data(**kwargs)


# User create
# - - - - - - - - - - - - - - - - - - - -
class UserCreateView(CreateView):
    model = UUIDUser
    template_name = 'core/form.html'
    success_url = reverse_lazy('core:login')
    form_class = UUIDUserForm

    def post(self, request, *args, **kwargs):
        form = UUIDUserForm(request.POST.copy())
        if form.is_valid():
            instance = form.save()
            instance.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('core:dashboard')
        return super().post(request, *args, **kwargs)


# User edit
# - - - - - - - - - - - - - - - - - - - -
class UserEditView(UpdateView):
    model = UUIDUser
    template_name = 'core/update.html'
    success_url = reverse_lazy('core:list')
    form_class = UUIDUserForm

    def get(self, request, *args, **kwargs):
        if kwargs['pk'] != request.user.id:
            return redirect('core:dashboard')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        instance = request.user
        form = UUIDUserForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('core:dashboard')
        return super().post(request, *args, **kwargs)


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
    user.active = False
    user.save()
    return redirect('core:dashboard')


# User active
# - - - - - - - - - - - - - - - - - - - -
def user_active_view(request, pk):
    if not request.user.is_staff and request.user.id != pk:
        return redirect('core:dashboard')
    user = UUIDUser.objects.get(id=pk)
    user.active = True
    user.save()
    return redirect('core:dashboard')
