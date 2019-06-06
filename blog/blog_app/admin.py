from django.contrib import admin
from .models import Autor, Postagem, Comentario

# Register your models here.
admin.site.register(Autor)
admin.site.register(Postagem)
admin.site.register(Comentario)