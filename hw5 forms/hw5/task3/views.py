from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormView

from .forms import *
from .models import *


class ArticleAddingFormView(FormView):
    """
    Article Adding FormView.
    The (form_class=) ArticleAddingForm class
    is related to the Article model.
    """

    form_class = ArticleAddingForm
    template_name = "task3/article_adding.html"
    # success_url = reverse("article", kwargs={"article_slug": "auth"})
    success_url = reverse_lazy("add_article")

    def form_valid(self, form):
        # save to Article table
        form.save()
        return super().form_valid(form)


def show_post(request, article_slug):
    """Creating pages from Article instances."""

    # get Article instance from model Article with slug=article_slug
    article = get_object_or_404(Article, slug=article_slug)

    # send the article to render the page with it
    context = {'article': article, }
    return render(request, 'task3/article.html', context=context)
