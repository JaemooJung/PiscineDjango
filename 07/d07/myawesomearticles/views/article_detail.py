from django.views.generic import DetailView
from ..models import Article, UserFavoriteArticle
from ..forms import UserFavoriteArticleForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = UserFavoriteArticleForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.article = self.get_object()
            form.save()
            return redirect('article_detail', pk=self.get_object().pk)
        else:
            return self.get(request)