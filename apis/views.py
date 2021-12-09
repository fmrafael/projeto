from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SearchKeyForm
import requests


class SearchKeyView(TemplateView):
  template_name = 'apis/search_key.html'
  
  def get(self, request):
    form = SearchKeyForm()
    return render(request, self.template_name, {'form':form})

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
      
      response = requests.request("GET", url, headers=headers, params=querystring).json()['googleGuggestedKeywords']
    return render(request, self.template_name, {'form':form, 'response':response})
    

      

    #return render(request, {"response":response,})

  
