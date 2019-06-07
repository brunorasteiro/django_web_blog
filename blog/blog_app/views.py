from django.shortcuts import render

# Create your views here.
from blog_app.models import Autor, Postagem, Comentario

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_autores = Autor.objects.all().count()
    num_posts = Postagem.objects.all().count()
    num_coments = Comentario.objects.all().count()
    
    context = {
        'num_autores': num_autores,
        'num_posts': num_posts,
        'num_coments': num_coments,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views import generic

class PostagensView(generic.ListView):
    model = Postagem