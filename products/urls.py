from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:product_id>/', views.product, name='product'),
    path('new_order/<int:product_id>/', views.new_order, name='new_order'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('notices/', views.notices, name='notices'),
    path('download_orders', views.download_orders, name='download_orders'),
    path('feedbacks/', views.feedbacks, name='feedbacks'),
    path('new_feedback/', views.new_feedback, name='new_feedback')
]
