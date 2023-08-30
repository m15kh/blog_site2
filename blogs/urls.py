from django.urls import path
from .views import PostViewList

urlpatterns = [
    path("", PostViewList.as_view(), name = "list_posts" )
    
]
