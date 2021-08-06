from django.http.request import QueryDict
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from . import util
import markdown2
from .forms.add_entry import AddEntryForm
# from random import randint
import random


def index(req):
    entries = util.list_entries()
    entries_len = len(entries)
    return render(req, "encyclopedia/index.html", {"entries_len": entries_len, "entries": entries})


def get_entry(req, title):
    ctx = {
        "title": title,
        "content": markdown2.markdown(util.get_entry(title))
        if util.get_entry(title)
        else None,
    }
    return render(req, "encyclopedia/entry_details.html", ctx)


def create_entry(req):

    if req.method == "POST":
        form = AddEntryForm(req.POST)
        if form.is_valid():
            try:

                ctx = {"form": form}

                # is exists
                is_exists = util.get_entry(form.cleaned_data["title"])
                if is_exists:
                    messages.error(
                        req, "Entry Already Exists!", "danger", fail_silently=True
                    )
                    return render(req, "encyclopedia/add_entry.html", ctx)

                #  save
                util.save_entry(
                    form.cleaned_data["title"], form.cleaned_data["content"]
                )
                messages.success(
                    req, "Saved Successfully", "success", fail_silently=True
                )
                return redirect(
                    reverse(
                        "encyclopedia:getEntry",
                        kwargs={"title": form.cleaned_data["title"]},
                    )
                )

            except Exception as er:
                messages.error(req, er, "danger", fail_silently=True)

        return render(req, "encyclopedia/add_entry.html", ctx)
    
    else:
        form = AddEntryForm()
        ctx = {"form": form, "title": "Create New"}
        return render(req, "encyclopedia/add_entry.html", ctx)


def edit_entry(req, title):

    if req.method == "POST":
        request = QueryDict(f'title={title}&content={req.POST["content"]}').copy()
        form = AddEntryForm(request)
        ctx = {"form": form, "title": title}
        if form.is_valid():
            try:

                #  save
                util.save_entry(
                    title, form.cleaned_data["content"]
                )
                messages.success(
                    req, "Updated Successfully", "success", fail_silently=True
                )
                return redirect(
                    reverse(
                        "encyclopedia:getEntry",
                        kwargs={"title": title},
                    )
                )

            except Exception as er:
                messages.error(req, er, "danger", fail_silently=True)

        return render(req, "encyclopedia/edit_entry.html", ctx)
    
    else:
        form = AddEntryForm()
        # set initial values
        form.initial = {
            "content": util.get_entry(title)
        }
        ctx = {"form": form, "title": title}
        
        return render(req, "encyclopedia/edit_entry.html", ctx)


def random_entry(req):
    entries = util.list_entries()
    li_len = len(entries)

    if not li_len:
        messages.error(req, "No Entries Yet!", "danger", fail_silently=True)
        return render(req, "encyclopedia/index.html")

    # rand_entry = entries[randint(0, li_len - 1)]
    rand_entry = random.choice(entries)

    ctx = {
        "title": rand_entry,
        "content": markdown2.markdown(util.get_entry(rand_entry))
        if util.get_entry(rand_entry)
        else None,
    }
    return render(req, "encyclopedia/entry_details.html", ctx)

@csrf_exempt
def search_entries(req):
    q = req.GET.get("q")
    if not q:
        return render(req, "encyclopedia/search.html")

    try:
        entries = util.search_entry(q)
        if not entries:
            return render(req, "encyclopedia/search.html")

        return render(req, "encyclopedia/search.html", {"results": entries, "q": q})
    
    except Exception as er:
        messages.error(req, er, "danger", fail_silently=True)
        return render(req, "encyclopedia/search.html")