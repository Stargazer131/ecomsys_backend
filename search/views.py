from django.shortcuts import render
from product.models import Book


# Create your views here.
def search_by_name(request):
    # handle search
    if request.method == 'POST':
        search_type = request.POST.get('searchType')
        text_search = request.POST.get('textSearch')
        image_search = request.FILES.get('imageSearch')
        voice_search = request.POST.get('voiceSearch')
        
        if search_type == 'text':
            books = Book.objects.filter(name__icontains=text_search)
        elif search_type == 'voice':
            books = Book.objects.filter(name__icontains=voice_search)
        else:
            books = Book.objects.all()
            
        context = {
            'books': books,
            'search_type': search_type,
        }
        return render(request, 'product/home.html', context)
    else:
        return render(request, 'book/index.html')
    