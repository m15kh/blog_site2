from typing import Any

from django.http import HttpRequest, HttpResponse
from .forms import CustomUserCreationForm 
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    def __init__(self,*arg,  **kwargs: Any) -> None:
        super().__init__(**kwargs)
        print(arg)
        print()
        print(kwargs)


    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'