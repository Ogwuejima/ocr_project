
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import OCRResult

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = OCRResult
        fields = ['image']  # Add more fields if users should input them


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import OCRResult

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = OCRResult

        fields = ['image']