from django.shortcuts import render, redirect
from .models import Product, Order, Notice
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv

# Create your views here.

@login_required
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/index.html', context)

@login_required
def products(request):
    products = Product.objects.order_by('-id')
    context = {'products': products}
    return render(request, 'products/products.html', context)

@login_required
def product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'products/product.html', context)


@login_required
def new_order(request, product_id):
    product =Product.objects.get(id=product_id)

    if request.method != 'POST':
        form = OrderForm()
    else:
        form = OrderForm(data=request.POST)
        if form.is_valid:
            new_order = form.save(commit=False)
            new_order.product = product
            new_order.user = request.user
            new_order.save()
            return redirect('products:my_orders')
    context = {'form': form, 'product': product}
    return render(request, 'products/new_order.html', context)


@login_required
def my_orders(request):
    my_orders = Order.objects.filter(user=request.user).order_by('-ordered_at')
    context ={'my_orders': my_orders}
    return render(request, 'products/my_orders.html', context)

@login_required
def notices(request):
    notices = Notice.objects.order_by('-date_created')
    context = {'notices': notices}
    return render(request, 'products/notices.html', context)

@login_required
def download_orders(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=orders.csv'

    writer = csv.writer(response)
    fields = Order._meta.fields

    # Add styling to header row
    header_row = [field.name.replace('_', ' ').title() for field in fields]  # Capitalize and replace underscores
    writer.writerow(header_row)

    # Add styling to data rows
    for obj in Order.objects.all():
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            # Add custom formatting if needed
            data_row.append(value)
        writer.writerow(data_row)
    
    return response