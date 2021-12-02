from django.views.generic import DetailView, ListView
from django.shortcuts import render


from .models import Post
class PostListView(ListView):
  model = Post

class PostDetailView(DetailView):
  model = Post


def home_view(request, *args, **kwargs):
  return render(request, "home.html",{})
# Create your views here.


def policy_view(request, *args, **kwargs):
  return render(request, "policy.html", {})

