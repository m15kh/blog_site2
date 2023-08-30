from django.urls import path
from .views import PostViewList, DetailPost

app_name = 'blog'

urlpatterns = [
    path("", PostViewList.as_view(), name = "list_posts" ),
    path("<int:pk>/", DetailPost.as_view(), name = "detail_post" )
]
