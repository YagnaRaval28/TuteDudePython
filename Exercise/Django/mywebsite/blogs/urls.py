from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_page),
    path('posts',views.blogposts),
    path('posts/<slug:blog>',views.blog_post,name="blog-post"),
    
]
