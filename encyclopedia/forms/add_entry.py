from django import forms

class AddEntryForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Title"}), label_suffix='', label='')
    content = forms.CharField(widget=forms.Textarea(attrs={"cols": 30, "rows": 15, "class": "form-control", "placeholder": "Content.."}), required=True, label_suffix='', label='')