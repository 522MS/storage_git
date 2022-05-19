from .views import FileListView, FileCreateView, FileDetailView, FileDeleteView, SearchResultsView

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "mainapp"

urlpatterns = [
    path("", FileListView.as_view(), name="files"),
    path("file/create", FileCreateView.as_view(), name="file_create"),
    path("file/read/<int:pk>/", FileDetailView.as_view(), name="file_read"),
    path("file/delete/<int:pk>/", FileDeleteView.as_view(), name="file_delete"),
    path("search/", SearchResultsView.as_view(), name="search"),
]

