from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search for images', max_length=100)
