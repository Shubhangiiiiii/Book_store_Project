from django.shortcuts import render
import requests

def home(request):
    return render(request, 'book_api/home.html')  # Change 'app/home.html' to 'book_api/home.html'

def FetchBookDetails(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        url = f'http://127.0.0.1:8000/books/{name}/'
        response = requests.get(url)
        if response.status_code == 200:
            book_details = response.json()
            return render(request, 'book_api/book_details.html', {'book_details': book_details})
        else:
            error_message = f"Failed to fetch book details. Status code: {response.status_code}"
            return render(request, 'book_api/error.html', {'error_message': error_message})
    return render(request, 'book_api/home.html')
