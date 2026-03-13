from django.shortcuts import render, get_object_or_404
from books.models import Books
from django.core.paginator import Paginator
from django.db.models import F #модуль для просмотров




#поиск
def search_view(request):
    query = request.GET.get("s", "")
    if query:
        book = Books.objects.filter(name_book__icontains=query)
    else:
        book = Books.objects.none
    
    return render(
        request,
        'book_list.html',
        {
            "book_key": book,
        }
    )

    






def book_list_view(req):
    if req.method == 'GET':
        # book - это значение
        book = Books.objects.all().order_by('-id')

        paginator = Paginator(book, 2)
        page = req.GET.get('page')
        page_obj = paginator.get_page(page)

    return render(
            req,
            #book_key - ключ который будет передан на html шаблон для запроса в виде скрипта на 
            #python
            'book_list.html',
            {
                "book_key": page_obj,
            }
        )




def book_detail_view(req, id):
    if req.method == 'GET':
        book_id = get_object_or_404(Books, id=id)
        views_book = req.session.get('viewed_book', [])

        if id not in views_book:
            #Увеличиваеться счетчик просмотров
            book_id.views = F("views")+1
            book_id.save()
            book_id.refresh_from_db()

            views_book.append(id)
            req.session["viewed_book"] = views_book



    return render(
        req,
        'book_detail.html',
        {
            'book_id_key': book_id,
        }
    )   