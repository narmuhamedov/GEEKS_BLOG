from django.shortcuts import render, redirect, get_object_or_404
from orders.forms import OrderForm
from orders.models import OrderBook

from django.views import generic


#create order

class CreateOrderView(generic.CreateView):
    template_name = 'create_order.html'
    form_class = OrderForm
    success_url = '/order_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateOrderView, self).form_valid(form=form)


#read
class OrderListView(generic.ListView):
    template_name = 'order_list.html'
    model = OrderBook
    context_object_name = 'order'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')



#update order
class UpdateOrderView(generic.UpdateView):
    template_name = 'update_order.html'
    form_class = OrderForm
    model = OrderBook
    success_url = '/order_list/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=order_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateOrderView, self).form_valid(form=form)




#delete - есть два способа с confirm используете именно DeleteView в generic
class DeleteOrderView(generic.View):
    def get(self, request, id):
        order_id = get_object_or_404(OrderBook, id=id)
        order_id.delete()
        return redirect('/order_list/')



