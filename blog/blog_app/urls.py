from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('autores/', views.AutorListView.as_view(), name='autores'),
    path('autor/<int:pk>', views.AutorDetailView.as_view(), name='autor-detail'),

    path('postagens/', views.PostagensListView.as_view(), name='postagens'),
    path('postagem/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),

    path('postagem/<int:pk>/comentar/', views.ComentarioCreateView.as_view(), name='comentario-create'),
]