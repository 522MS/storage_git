from django import forms

from mainapp.models import Document


class FileEditForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('uploadedFile',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style'] = 'width: auto'
