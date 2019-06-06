from django.contrib import admin
from .models import Autor, Postagem, Comentario

# Register your models here.
admin.site.register(Autor)
#admin.site.register(Postagem)
admin.site.register(Comentario)


class ComentariosInline(admin.TabularInline):
    model = Comentario
    max_num = 0

# Register the PostagemAdmin class with the associated model
@admin.register(Postagem)
# Define the admin class
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'datahora')
    inlines = [ComentariosInline]

