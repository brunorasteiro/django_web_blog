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
    context_object_name = 'postagem_list'   # your own name for the list as a template variable
    template_name = 'blog_app/postagem_list.html'  # Specify your own template name/location
    # queryset = Postagem.objects.all()[:5] # Get 5 books containing the title war
    # TODO: show 5 per page

class PostDetailView(generic.DetailView):
    model = Postagem
    # 


    
