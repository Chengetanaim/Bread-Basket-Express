from django.contrib import admin
from .models import Product, Order, Notice, Feedback


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image', 'available']
    list_filter = ['available']
    search_fields = ['name', 'description']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity','ordered_at']
    list_filter = ['user', 'ordered_at']
    search_fields = ['product']
    raw_id_fields = ['user']
    date_hierachy = 'ordered_at'
    ordering = ['ordered_at']

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'image','date_created']
    list_filter = ['date_created']
    search_fields = ['title', 'description']
    date_hierachy = 'date_created'
    ordering = ['date_created']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_added']
    list_filter = ['user', 'date_added']
    search_fields = ['user', 'text']
    date_hierachy = 'date_added'
    ordering = ['date_added']