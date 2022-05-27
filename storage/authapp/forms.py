from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import StorageUser


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = StorageUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = StorageUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = StorageUser
        fields = ('is_superuser', 'username', 'first_name', 'email', 'age', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()
