from django.shortcuts import render

# Create your views here.
from blog_app.models import Autor, Postagem, Comentario

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_autores = Autor.objects.all().count()
    num_posts = Postagem.objects.all().count()
    num_coments = Comentario.objects.all().count()
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_autores': num_autores,
        'num_posts': num_posts,
        'num_coments': num_coments,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views import generic

class PostagensListView(generic.ListView):
    model = Postagem
    paginate_by = 5

    # context_object_name = 'postagem_list'   # your own name for the list as a template variable
    # template_name = 'blog_app/postagem_list.html'  # Specify your own template name/location
    
class PostDetailView(generic.DetailView):
    model = Postagem

class AutorListView(generic.ListView):
    model = Autor

class AutorDetailView(generic.DetailView):
    model = Autor
