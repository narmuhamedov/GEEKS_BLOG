from django.shortcuts import render, get_object_or_404
from books.models import Books

def book_list_view(req):
    if req.method == 'GET':
        # book - это значение
        book = Books.objects.all().order_by('-id')
    return render(
            req,
            #book_key - ключ который будет передан на html шаблон для запроса в виде скрипта на 
            #python
            'book_list.html',
            {
                "book_key": book,
            }
        )

def book_detail_view(req, id):
    if req.method == 'GET':
        book_id = get_object_or_404(Books, id=id)

    return render(
        req,
        'book_detail.html',
        {
            'book_id_key': book_id,
        }
    )   