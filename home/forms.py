from django import forms

class TeacherLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class TeacherRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

