from django.urls import path
from django.urls import path
from .views import list_books, LibraryDetailView
from .views import admin_view, librarian_view, member_view

urlpatterns += [
    path("admin/", admin_view, name="admin_view"),
    path("librarian/", librarian_view, name="librarian_view"),
    path("member/", member_view, name="member_view"),
]
urlpatterns += [
    path("book/add/", add_book, name="add_book"),
    path("book/edit/<int:book_id>/", edit_book, name="edit_book"),
    path("book/delete/<int:book_id>/", delete_book, name="delete_book"),
]


urlpatterns = [
    path("books/", views.list_books, name="list_books"),  # FBV
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    path("register/", register, name="register"),
]
"views.register"
