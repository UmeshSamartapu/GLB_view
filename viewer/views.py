from django.shortcuts import render, redirect
from .forms import GLBUploadForm
from .models import GLBModel

def landing(request):
    return render(request, 'landing.html')

def upload_model(request):
    if request.method == 'POST':
        form = GLBUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mobile')
    else:
        form = GLBUploadForm()
    return render(request, 'upload.html', {'form': form})

def mobile_view(request):
    model = GLBModel.objects.last()
    return render(request, 'mobile.html', {'model': model})

def laptop_view(request):
    model = GLBModel.objects.last()
    return render(request, 'laptop.html', {'model': model})