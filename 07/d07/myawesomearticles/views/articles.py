from django.views.generic import ListView
from ..models import Article

class ArticlesView(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all().order_by('-created')
