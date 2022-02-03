from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField
from django.core.exceptions import ValidationError


class UserRegisterForm(forms.ModelForm):
      confirm_password = forms.CharField(label="Confirm Password")

      class Meta:
          model = CustomUser
          fields = ['first_name','last_name','username','email','image','password','confirm_password']

      def __init__(self, *args, **kwargs):
          super(UserRegisterForm,self).__init__(*args, **kwargs)
          self.fields['first_name'].widget.attrs ={'placeholder': "FirstName", 'class': 'form-control','required':True}
          self.fields['last_name'].widget.attrs ={'placeholder': "LastName", 'class': 'form-control','required':True}
          self.fields['username'].widget.attrs ={'placeholder': "UserName", 'class': 'form-control'}
          self.fields['email'].widget.attrs ={'placeholder': "Email Address", 'class': 'form-control','required':True}
          self.fields['password'].widget = forms.PasswordInput(attrs ={'placeholder': "Password", 'class': 'form-control'})
          self.fields['confirm_password'].widget = forms.PasswordInput(attrs ={'placeholder': "Confirm Password", 'class': 'form-control'})
          self.fields['image'].widget.attrs ={'required':True}
          
      def clean(self):       
         cleaned_data = super(UserRegisterForm, self).clean()
         password = self.cleaned_data.get('password')
         password2 = self.cleaned_data.get('confirm_password')

         if password and password2 and password != password2:
            raise forms.ValidationError("passwords do not match")

         return self.cleaned_data

      def clean_username(self):
         username = self.cleaned_data['username']
         return username


      def clean_email(self):
            email = self.cleaned_data.get('email')
            try:  
                  match = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                  return email
            raise forms.ValidationError('This email address is already in use.')

      def clean_password(self):
         password= self.cleaned_data['password']
         if len(password) < 8:
            raise forms.ValidationError("Your password should be at least 8 Characters")
         return password

class UserLoginForm(AuthenticationForm):
   
   class Meta:
      model = CustomUser
      fields = ['username','password']

   def __init__(self, *args, **kwargs):
          super(UserLoginForm,self).__init__(*args, **kwargs)
          self.fields['username'].widget.attrs ={'placeholder': "Email Address", 'class': 'form-control'}         
          self.fields['password'].widget = forms.PasswordInput(attrs ={'placeholder': "Password", 'class': 'form-control'})



class UserProfileUpdateForm(forms.ModelForm):
   class Meta:
      model = CustomUser
      fields = ['first_name','last_name','username','email'] 
   

   def __init__(self, *args, **kwargs):
          super(UserProfileUpdateForm,self).__init__(*args, **kwargs)
          self.fields['first_name'].widget.attrs ={ 'class': 'form-control'}         
          self.fields['last_name'].widget.attrs ={'class': 'form-control'}
          self.fields['username'].widget.attrs ={ 'class': 'form-control'}         
          self.fields['email'].widget.attrs ={'class': 'form-control'}



