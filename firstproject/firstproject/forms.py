from django import forms

class usersForm(forms.ModelForm):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)
