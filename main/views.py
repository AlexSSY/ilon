from django.shortcuts import render, redirect
from .forms import MainForm

def index(reguest):
    form = MainForm()
    return render(reguest, 'main/page.html', {'title': 'Tesla X', 'form': form})

def send(request):
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:success')
    else:
        form = MainForm()

    return render(request, 'main/send.html', {'title': 'Tesla X', 'form': form})

def success(request):
    return render(request, 'main/success.html',  {'title': 'Tesla X'})