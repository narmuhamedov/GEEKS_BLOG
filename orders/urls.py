from django.urls import path
from orders.views import create_order_view, order_list_view, update_order_view, delete_order_view


urlpatterns = [
    path('create_order/', create_order_view),
    path('order_list/', order_list_view),
    path('order_list/<int:id>/update/', update_order_view),
    path('order_list/<int:id>/delete/', delete_order_view),
]