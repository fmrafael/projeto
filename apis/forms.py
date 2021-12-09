from django import forms

class SearchKeyForm(forms.Form):
  search_key = forms.CharField(label = 'insira a palavra-chave', max_length = 200 )

