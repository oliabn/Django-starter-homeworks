# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView

from .forms import AuthorizationForm, UserAuthorizationForm


def thanks(request):
    """Page of successful authorization"""
    return HttpResponse('<p>Authorization was successful</p>')


class AuthorizationFormView(FormView):
    """
    User authorization by user_name, email, password
    The AuthorizationForm class is not related to the model,
    only View of Authorization Form
    """

    template_name = "task2/authorization_form.html"
    form_class = AuthorizationForm
    success_url = "thanks/"

    def get(self, request, *args, **kwargs):
        # print(request.GET)
        return super().get(request,  *args, **kwargs)


class UserAuthorizationFormView(FormView):
    """
    User authorization by email, password
    The UserAuthorizationForm class is related to the User model,
    View of Authorization Form
    """

    form_class = UserAuthorizationForm
    template_name = "task2/authorization_form.html"
    success_url = "thanks/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
