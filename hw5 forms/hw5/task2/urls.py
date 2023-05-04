from django.urls import path
from .views import *

urlpatterns = [
    # Authorization forms
    # http://127.0.0.1:8000/task2/authorization_form/
    path('authorization_form/', AuthorizationFormView.as_view(), name='authorization_form'),
    # http://127.0.0.1:8000/task2/user_authorization_form/
    path('user_authorization_form/', UserAuthorizationFormView.as_view(), name='user_authorization_form'),

    # Successful authorization
    path('authorization_form/thanks/', thanks),
    path('user_authorization_form/thanks/', thanks),
]