import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def search_entry(title):
    """search encyclopedia by title

    Args:
        title (str): encyclopedia title query str

    Returns:
        [list | None]: returns list of matched queries [dict{<str:title>, <str:content>}] or an empty list 
        otherwise None if any error
    """
    if not title:
        return None

    try:
        filenames = list_entries()
        if not filenames:
            return None

        names = []

        for filename in filenames:
            content = get_entry(filename)
            if filename == title or [i.group() for i in re.finditer(title, filename, re.I)]:
                names.append({"title": filename, "content": content})
            
        return names
    
    except:
        return None
    