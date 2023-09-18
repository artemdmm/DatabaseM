from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.TracksDetailView.as_view(), name='track-detail'),
]
