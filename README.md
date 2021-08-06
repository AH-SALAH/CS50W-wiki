### CS50W Project 1 - Wiki

- A Wikipedia-like online encyclopedia.

> Wikipedia is a free online encyclopedia that consists of a number of encyclopedia entries on various topics.

#### Tech
- HTML
- Css3
- Python
- Django

---
### Structure

```
├── encyclopedia
│   ├── forms
│   │   └── add_entry.py
│   ├── migrations
│   │   └── __init__.py
│   ├── static
│   │   └── encyclopedia
│   │       └── styles.css
│   ├── templates
│   │   └── encyclopedia
│   │       ├── includes
│   │       │   └── side_nav.html
│   │       ├── add_entry.html
│   │       ├── edit_entry.html
│   │       ├── entry_details.html
│   │       ├── index.html
│   │       ├── layout.html
│   │       └── search.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── util.py
│   └── views.py
├── entries
│   ├── CSS.md
│   ├── Django.md
│   ├── Git.md
│   ├── Go.md
│   ├── HTML.md
│   ├── Javascript.md
│   ├── Python.md
│   └── Ruby.md
├── wiki
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitattributes
├── .gitignore
├── db.sqlite3
├── manage.py
├── Pipfile
├── Pipfile.lock
└── README.md
```