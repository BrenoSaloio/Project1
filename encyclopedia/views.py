from django.shortcuts import render
from django import forms

from . import util




class ContentForm(forms.Form):
    entry_title = forms.CharField()
    entry_content = forms.CharField(widget=forms.Textarea(attrs={'width':"50%", 'cols' : "10", 'rows': "20", }))



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new_page(request):
    return render(request, "encyclopedia/new_page.html", {
        "entries": util.list_entries(),
        "form": ContentForm()
    })
