from . import views
from django.urls import path


app_name = "apis"

urlpatterns = [
  path("apis/", views.SearchKeyView.as_view(), name="search_key"),
  
   
  
]