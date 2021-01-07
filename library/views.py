from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Comment
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
#from .forms import BookForm, CommentForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import RegisterForm


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'library/index.html', {'page_title': 'Library app'})
    else:
        return redirect('library:books')

@login_required()
def books(request):
    tmp = Book.objects.all()
    return render(request, 'library/books.html', {'books': tmp})


def book(request, id):
    return None


def edit(request, id):
    return None


def new(request):
    return None


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'library/register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()

                # Login the user
                login(request, user)

                # redirect to accounts page:
                return redirect('library:books')

    # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})