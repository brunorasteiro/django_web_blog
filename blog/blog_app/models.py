from django.db import models

class Autor(models.Model):

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    

    # Metadata
    class Meta: 
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return self.my_field_name

class Postagem(models.Model):

    # Fields
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    datahora = models.DateTimeField(auto_now_add=True)
    conteudo = models.CharField(max_length=500, help_text='Escreva sua postagem')
    

    # Metadata
    class Meta: 
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return self.conteudo


class Comentario(models.Model):

    # Fields
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    datahora = models.DateTimeField(auto_now_add=True)
    conteudo = models.CharField(max_length=500, help_text='Escreva seu comentario')
    

    # Metadata
    class Meta: 
        ordering = ['-datahora']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return self.couteudo

