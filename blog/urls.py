from . import views
from django.urls import path


app_name = "blog"

urlpatterns = [
  path("blog/", views.PostListView.as_view(), name="post_list"),
  path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
   
  
]