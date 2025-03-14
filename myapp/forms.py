from django import forms

from myapp.models import TaskModel

class Userform(forms.Form):

    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control w-75','placeholder':'enter username'}))

    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control w-75','placeholder':'enter first name'}))

    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control w-75','placeholder':'enter last name'}))

    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control w-75','placeholder':'enter the email'}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control w-75','placeholder':'enter your password'}))


class Loginform(forms.Form):
    
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control w-75','placeholder':'enter username'}))

    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control w-75','placeholder':'enter your password'}))


class Taskform(forms.ModelForm):
    
   class Meta:
       
       model=TaskModel

       fields=["task_name","due_date","priority_level"]

       widgets={'task_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter the task'})}

       
