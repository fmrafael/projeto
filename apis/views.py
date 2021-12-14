from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SearchKeyForm, WhatsappForm
import requests
from blog.models import Post
from django.http import HttpResponseRedirect


post = Post.objects.get(pk=9)

class SearchKeyView(TemplateView):
  template_name = 'apis/search_key.html'
  
  def get(self, request):
    form = SearchKeyForm()
    return render(request, self.template_name, {'form':form, 'post':post})

  def post(self, request):
    form = SearchKeyForm(request.POST)
    if form.is_valid():
      search_key = form.cleaned_data['search_key']

      url = "https://keywords4.p.rapidapi.com/google-topLevel-10-keywords"
      headers = {
      'content-type': "application/json",
      'x-rapidapi-host': "keywords4.p.rapidapi.com",
      'x-rapidapi-key': "C4e4A0veUwpEi3lQDOLNgWYX59sUBN86"     }

      querystring = {"search":search_key,"country":"br"}
      try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()['googleGuggestedKeywords']
        return render(request, self.template_name, {'form':form, 'response':response, 'post':post})

      except Exception:
        return HttpResponseRedirect(self.request.path_info)
    
class WhatsappView(TemplateView):
  template_name = 'apis/whatsapp.html'
  post = Post.objects.get(pk=9)
  def get(self, request):
     form = WhatsappForm()
     return render(request, self.template_name, {'form':form, 'post':post})

  def post(self, request):
    form = WhatsappForm(request.POST)
    if form.is_valid():
     whatsapp = form.cleaned_data['cell']
     whats_link = f"https://api.whatsapp.com/send?phone={whatsapp}"
     return render(request, self.template_name, {'whats_link':whats_link,'post':post})
  
