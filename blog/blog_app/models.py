from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Autor(models.Model):

    # Fields
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=500, help_text="Insira sua biografia aqui.")
    
    # Metadata
    class Meta:
        ordering = ["usuario"]

    def get_absolute_url(self):
        """
        Return the url to for a blog-author
        """
        return reverse('blogs-by-author', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.usuario.username


class Postagem(models.Model):

    # Fields
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    titulo = models.CharField(max_length=100, help_text='Escreva o título da postagem')    
    datahora = models.DateTimeField(auto_now_add=True)
    conteudo = models.CharField(max_length=1000, help_text='Escreva sua postagem')
    
    # Metadata
    class Meta: 
        ordering = ['-datahora']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return self.titulo


class Comentario(models.Model):

    # Fields
    post = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    datahora = models.DateTimeField(auto_now_add=True)
    conteudo = models.CharField(max_length=1000, help_text='Escreva seu comentario')
    
    # Metadata
    class Meta: 
        ordering = ['datahora']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return self.conteudo if len(self.conteudo) <= 75 else self.conteudo[:72]  + '...'

