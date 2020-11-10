"""webshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.notes_home, name='notes_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NotesDetailView.as_view(), name='notes_detail'),
                        # track dynamic parameters <>
                        # notes/1 , notes/2
    path('<int:pk>/update', views.NotesUpdateView.as_view(), name='notes_update'),
    path('<int:pk>/delete', views.NotesDeleteView.as_view(), name='notes_delete'),
    path('<int:pk>/model_form_upload', views.NotesDetailView.as_view(), name='model_form_upload')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)