
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UploadImageForm
from .models import OCRResult
from PIL import Image
import pytesseract

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'ocr_app/register.html', {'form': form})

@login_required
def home(request):
    results = OCRResult.objects.filter(user=request.user)
    return render(request, 'ocr_app/home.html', {'results': results})

@login_required
def upload_image(request):
    text = ""
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            image = Image.open(obj.image)
            text = pytesseract.image_to_string(image)
            obj.extracted_text = text
            obj.save()
            return render(request, 'ocr_app/upload.html', {'form': form, 'text': text})
    else:
        form = UploadImageForm()

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UploadImageForm
from .models import OCRResult
from PIL import Image
import pytesseract

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'ocr_app/register.html', {'form': form})

@login_required
def home(request):
    results = OCRResult.objects.filter(user=request.user)
    return render(request, 'ocr_app/home.html', {'results': results})

@login_required
def upload_image(request):
    text = ""
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            image = Image.open(obj.image)
            text = pytesseract.image_to_string(image)
            obj.extracted_text = text
            obj.save()
            return render(request, 'ocr_app/upload.html', {'form': form, 'text': text})
    else:
        form = UploadImageForm()

    return render(request, 'ocr_app/upload.html', {'form': form})