from django import forms

from mainapp.models import Document


class FileEditForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('uploadedFile',)
