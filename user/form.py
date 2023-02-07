from django import forms

 
# creating a form
class SignUp(forms.Form):
 
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length = 18)
    confirm_password = forms.CharField(max_length=18)

