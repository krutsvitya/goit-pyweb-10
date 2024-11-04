from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, AuthorForm, QuoteForm
from django.contrib.auth import logout
from .models import Author, Quote


def main(request):
    authors_arr = Author.objects.all()
    return render(request, 'authorsapp/index.html', {'authors': authors_arr})


def author_info(request, fullname):
    author = get_object_or_404(Author, fullname=fullname)
    quotes = Quote.objects.filter(author=author)
    return render(request, 'authorsapp/author_info.html', {'author': author, 'quotes': quotes})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'authorsapp/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'authorsapp/login.html', {'form': form})


def my_logout(request):
    logout(request)
    return redirect('/')


@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AuthorForm()
    return render(request, 'authorsapp/add_author.html', {'form': form})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authorsapp:main')
    else:
        form = QuoteForm()
    return render(request, 'authorsapp/add_quote.html', {'form': form})

