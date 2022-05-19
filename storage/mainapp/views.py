from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from .forms import FileEditForm
from .models import Document


class SearchResultsView(ListView):
    model = Document
    template_name = 'mainapp/files.html'
    context_object_name = 'objects'

    def get_queryset(self):
        query = self.request.GET.get('q')
        try:
            object_list = Document.objects.filter(id=query)
        except:
            object_list = Document.objects.filter(Q(uploadedFile=query) | Q(title=query))
        return object_list


class FileListView(ListView):
    model = Document
    template_name = 'mainapp/files.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FileListView, self).get_context_data()
        context['title'] = 'Документ'
        return context

    def get_queryset(self):
        return Document.objects.order_by('title')


class FileDetailView(DetailView):
    model = Document
    template_name = 'mainapp/file_read.html'
    context_object_name = 'file'


class FileCreateView(CreateView):
    model = Document
    template_name = 'mainapp/file_create.html'
    form_class = FileEditForm

    def get_success_url(self):
        success_url = reverse_lazy('mainapp:files')
        return success_url


class FileDeleteView(DeleteView):
    model = Document
    template_name = 'mainapp/file_delete.html'
    success_url = reverse_lazy('mainapp:files')
    context_object_name = 'file'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
