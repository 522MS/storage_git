from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from authapp.forms import UserLoginForm, UserRegisterForm, ShopUserEditForm
from authapp.models import StorageUser


def login(request):
    title = 'вход'

    login_form = UserLoginForm(data=request.POST)

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    context = {
        'title': title,
        'login_form': login_form,
    }

    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


class Register(CreateView):
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm

    def get_success_url(self):
        success_url = reverse_lazy('mainapp:files')
        return success_url


class UsersListView(ListView):
    model = StorageUser
    template_name = 'authapp/user_read.html'
    context_object_name = 'objects'


class UserUpdateView(UpdateView):
    model = StorageUser
    form_class = ShopUserEditForm
    template_name = 'authapp/user_update.html'
    success_url = reverse_lazy('admin_staff:users')


class UserDeleteView(DeleteView):
    model = StorageUser
    template_name = 'authapp/user_delete.html'
    success_url = reverse_lazy('authapp:user_read')

