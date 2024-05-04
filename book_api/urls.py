from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL for the book homepage
    path('book-details/', views.FetchBookDetails, name='book_details'),  # URL for fetching book details
]
