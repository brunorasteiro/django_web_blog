from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postagens/', views.PostagensView.as_view(), name='postagens'),
    path('postagem/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
]