from django import forms


# Search Form
class SearchForm(forms.Form):
    query = forms.CharField()
