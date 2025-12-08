from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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