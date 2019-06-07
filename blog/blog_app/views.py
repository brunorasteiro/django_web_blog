from django.shortcuts import render
from django.views import generic
from blog_app.models import Autor, Postagem, Comentario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.urls import reverse    
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

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


#@login_required
class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    fields = ['conteudo']
    
    def get_context_data(self, **kwargs):
        context = super(ComentarioCreateView, self).get_context_data(**kwargs)
        context['postagem'] = get_object_or_404(Postagem, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        form.instance.autor = self.request.user.autor_set.first()
        form.instance.post = get_object_or_404(Postagem, pk = self.kwargs['pk'])
        return super(ComentarioCreateView, self).form_valid(form)

    def get_success_url(self): 
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk'],})