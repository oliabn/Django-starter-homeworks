from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormView

from .forms import *
from .models import *


class ReviewAddingFormView(FormView):
    """
    Review Adding FormView.
    The (form_class=) ReviewAddingForm class is
    related to the Review model.
    """

    form_class = ReviewAddingForm
    template_name = "task4/review_adding.html"
    success_url = reverse_lazy("add_review")

    def form_valid(self, form):
        # save to Review table
        form.save()
        return super().form_valid(form)


def show_review(request, review_pk):
    """Creating pages from Review instances."""

    # get Review instance from model Review with pk=review_id
    review = get_object_or_404(Review, pk=review_pk)

    # send the review to render the page with it
    context = {'review': review, }
    return render(request, 'task4/review.html', context=context)
