from django.urls import path
from .views import homepage
app_name = 'website'

urlpatterns = [
    path('', homepage, name='home'),
]
