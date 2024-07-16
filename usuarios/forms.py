from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Apellido')
    email = forms.EmailField()
    
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username','password1','password2')
        
    def __init__(self, *arg, **kwargs):
        super(UserCreationForm,self).__init__(*arg,**kwargs)
        for field in self.fields:
                self.fields[field].widget.attrs.update({'class':'form-control'})