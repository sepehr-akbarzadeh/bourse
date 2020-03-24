from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _

class NewsView(TemplateView):
    template_name = 'pages/news/posts.html'
    page_name = _('اخبار')

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)

        return context

class SingleNewsView(TemplateView):
    template_name = 'pages/news/post.html'
    page_name = _('خبر')

    def get_context_data(self, **kwargs):
        context = super(SingleNewsView, self).get_context_data(**kwargs)

        return context