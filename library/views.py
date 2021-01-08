from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Comment
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from .forms import BookForm, CommentForm
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

def comment_view(request):
    return render(request, 'library/book.html', {'books': Book.object.all()})

@login_required()
def book(request, id):
    tmp = get_object_or_404(Book, id=id)
    return render(request, 'library/book.html', {'book': tmp, 'page_title': tmp.title})

@permission_required('library.change_book')
def edit(request, id):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            a = Book.objects.get(id=id)
            a.title = form.cleaned_data['title']
            a.content = form.cleaned_data['content']
            a.save()
            return redirect('library:books')
        else:
            return render(request, 'library/edit.html', {'form': form, 'id': id})
    else:
        a = Book.objects.get(id=id)
        form = BookForm(instance=a)
        return render(request, 'library/edit.html', {'form': form, 'id': id})

@permission_required('library.add_book')
def new(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            a = Book(title=form.cleaned_data['title'], content=form.cleaned_data['content'], owner=request.user)
            a.save()
            return redirect('library:books')
        else:
            return render(request, 'library/new.html', {'form': form})
    else:
        form = BookForm()
        return render(request, 'library/new.html', {'form': form})


@permission_required('library.delete_book')
def delete(request, id):
    Book.objects.filter(id=id).delete()
    tmp = Book.objects.all()
    return render(request, 'library/books.html', {'books': tmp})


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


