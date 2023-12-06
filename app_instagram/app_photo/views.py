from django.shortcuts import render, redirect

from .forms import PictureForm
from .models import Picture
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request, 'app_photo/index.html', context={"msg": "Hello world!"})


@login_required
def pictures(request):
    pics = Picture.objects.filter(user=request.user).all()
    return render(request, 'app_photo/pictures.html', context={"pics": pics})


@login_required
def upload(request):
    form = PictureForm(instance=Picture())
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES, instance=Picture())
        if form.is_valid():
            pic = form.save(commit=False)
            pic.user = request.user
            pic.save()
            return redirect(to='app_photo:pictures')
    return render(request, 'app_photo/upload.html', context={'form': form})


@login_required
def edit(request, pic_id):
    form = PictureForm(instance=Picture())
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES, instance=Picture())
        if form.is_valid():
            pic = form.save(commit=False)
            pic.user = request.user
            pic.save()
            return redirect(to='app_photo:pictures')
    return render(request, 'app_photo/upload.html', context={'form': form})


@login_required
def remove(request, pic_id):
    form = PictureForm(instance=Picture())
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES, instance=Picture())
        if form.is_valid():
            pic = form.save(commit=False)
            pic.user = request.user
            pic.save()
            return redirect(to='app_photo:pictures')
    return render(request, 'app_photo/upload.html', context={'form': form})