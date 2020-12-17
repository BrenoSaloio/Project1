from django.shortcuts import render
from django import forms

from . import util


class ContentForm(forms.Form):
    entry_title = forms.CharField()
    entry_content = forms.CharField(widget=forms.Textarea())



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new_page(request):
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["entry_title"]
            content = form.cleaned_data["entry_content"]
            util.save_entry(title, content)
        else:
            return render(request, "encyclopedia/new_page.html", {
                "form": ContentForm() })
    return render(request, "encyclopedia/new_page.html", {
            "form": ContentForm() })



def topic(request, name):
    if util.get_entry(name):
        if  util.get_entry(name).find("#") >= 0:
            return render(request, "encyclopedia/topic.html", {
                "entries": util.list_entries(),
                "name": name.upper(),
                "content": util.get_entry(name)[len(name)+2:]
                })
        else:
            return render(request, "encyclopedia/topic.html", {
                "entries": util.list_entries(),
                "name": name.upper(),
                "content": util.get_entry(name)
                })
    else:
        return render(request, "encyclopedia/topic.html", {
            "entries": util.list_entries(),
            "name": name.upper(),
            "content": util.get_entry(name)
            })
