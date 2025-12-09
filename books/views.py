from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Book  
from .forms import BookForm


def helloWordViews(request):
    writers = [
        'Николай Гоголь',
        'Иван Бунин',
        'Антон Чехов',
        'Сергей Есенин',
        'Владимир Маяковский',
        'Максим Горький',
        'Александр Куприн',
        'Надежда Тэффи',
        'Михаил Пришвин',
        'Андрей Платонов',
    ]

    return HttpResponse("<br>".join(writers))


def quotesView(request):
    quotes = [
        'Джейн Остин: «Нет очарования равного искренности.»',
        'Фёдор Достоевский: «Красота спасёт мир.»',
        'Франц Кафка: «Путь создаётся идущим.»',
        'Оскар Уайльд: «Будь собой — остальные роли уже заняты.»',
        'Рэй Брэдбери: «Любите то, что делаете, иначе ничего не получится.»',
    ]
    return HttpResponse("<br>".join(quotes))


def timeView(request):
    now = datetime.now().strftime("%H:%M:%S  %d.%m.%Y")
    return HttpResponse(f"Текущее системное время: {now}")


def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", {"book": book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'books/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('book_detail', pk=pk)

    return render(request, 'books/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'books/book_delete_confirm.html', {'book': book})

