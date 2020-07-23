from django.shortcuts import render
import markdown2
from markdown2 import Markdown
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryPage(request, title):
    markdowner=Markdown()
    return render(request,"encyclopedia/entryPage.html",{
        "content": markdowner.convert(util.get_entry(title))    # Converting markdown into html format before passing into template.
    })

