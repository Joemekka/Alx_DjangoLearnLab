from django.shortcuts import render, get_object_or_404
from .models import Book, Library
from django.views.generic import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegisterForm


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            messages.success(request, f"Account created for {user.username}!")
            return redirect("list_books")  # Redirect to books list
    else:
        form = UserRegisterForm()
    return render(request, "relationship_app/register.html", {"form": form})


# User login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("list_books")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


# User logout view
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return render(request, "relationship_app/logout.html")
