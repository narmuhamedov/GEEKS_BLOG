from django.shortcuts import render, redirect, get_object_or_404
from orders.forms import OrderForm
from orders.models import OrderBook


#create order
def create_order_view(request):
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/order_list/')
    else:
        form = OrderForm()
    
    return render(
        request,
        'create_order.html',
        {'form': form}
    )

#read
def order_list_view(request):
    if request.method == 'GET':
        order = OrderBook.objects.all().order_by('-id')
    return render(request, 'order_list.html', {'order': order})


#update order
def update_order_view(request, id):
    order_id = get_object_or_404(OrderBook, id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order_id)
        if form.is_valid():
            form.save()
            return redirect('/order_list/')
    else:
        form = OrderForm(instance=order_id)
    
    return render(
        request,
        'update_order.html',
        {
            'form': form,
            'order_id': order_id
        }
    )

#delete
def delete_order_view(request, id):
    order_id = get_object_or_404(OrderBook, id=id)
    order_id.delete()
    return redirect('/order_list/')