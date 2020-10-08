from django.urls import path, re_path
from .views import FileView, FileGetAllView, FileGetView

urlpatterns = [
    path('upload', FileView.as_view(), name='file-upload'),
    path('fetch', FileGetView.as_view(), name='file-fetch'),
    path('fetchall', FileGetAllView.as_view(), name='file-fetchall')
]
