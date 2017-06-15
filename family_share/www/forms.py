from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='Last Name', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password_confirm = forms.CharField(label='Retype Password', widget=forms.PasswordInput(attrs={'placeholder': 'Retype Password'}))
