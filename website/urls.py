from django.urls import path
from .views import homepage, testpage
app_name = 'website'

urlpatterns = [
    path('', homepage, name='home'),
    path('test/', testpage, name='test'),

]
