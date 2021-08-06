from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/new", views.create_entry, name="createEntry"),
    path("wiki/random", views.random_entry, name="randomEntry"),
    path("wiki/search", views.search_entries, name="searchEntries"),
    path("wiki/<title>", views.get_entry, name="getEntry"),
    path("wiki/<title>/edit", views.edit_entry, name="editEntry"),
]
