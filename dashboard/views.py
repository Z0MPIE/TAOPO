from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from .models import Grocery
from .forms import ProductForm
from .forms import GroceryForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

@login_required
def index(request):
    grocery_count = Grocery.objects.all().count()
    employees_count = User.objects.all().count()
    items_count = Product.objects.all().count()
    products = Product.objects.all()
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = GroceryForm()
    context = {
        'form': form,
        'products': products,
        'employees_count': employees_count,
        'items_count': items_count,
        'grocery_count': grocery_count,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def staff(request):
    employees = User.objects.all()
    employees_count = employees.count()
    items_count = Product.objects.all().count()
    grocery_count = Grocery.objects.all().count()
    context={
        'employees':employees,
        'employees_count': employees_count,
        'items_count': items_count,
        'grocery_count': grocery_count,
    }
    return render(request, 'dashboard/staff.html', context)

@login_required
def staff_detail(request, pk):
    employees = User.objects.get(id=pk)
    context={
        'employees': employees,
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required
def inventory(request): 
    items = Product.objects.all() #Using ORM
    #items = Product.objects.raw('SELECT * FROM dashboard_product')
    items_count = items.count()
    employees_count = User.objects.all().count()
    grocery_count = Grocery.objects.all().count()

    for item in items:
        item.islow = item.quantity < 5

    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect ('dashboard-inventory')
    else:
        form = ProductForm()
    context ={
        'items': items,
        'items_count': items_count,
        'form': form,
        'employees_count': employees_count,
        'grocery_count': grocery_count,
    }
    return render(request, 'dashboard/inventory.html', context)

@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-inventory')
    return render(request, 'dashboard/inventory_delete.html')

@login_required
def product_update(request, pk):
 item = Product.objects.get(id=pk)
 
 if request.method =='POST':
    form = ProductForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return redirect ('dashboard-inventory')
    
 else:
    form = ProductForm(instance=item)

    context={
        'form': form,
    }
    return render(request, 'dashboard/inventory_update.html', context)

@login_required
def grocery(request):
    items = Grocery.objects.all() #Using ORM
    #items = Product.objects.raw('SELECT * FROM dashboard_product')
    employees_count = User.objects.all().count()
    items_count = Product.objects.all().count()
    grocery_count = Grocery.objects.all().count()
    if request.method =='POST':
        form = GroceryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('dashboard-grocery')
    else:
        form = GroceryForm()
    context ={
        'items': items,
        'form': form,
        'employees_count': employees_count,
        'items_count': items_count,
        'grocery_count': grocery_count,
    }
    return render(request, 'dashboard/grocery.html', context)

@login_required
def product_purchased(request, pk):
    item = Grocery.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-grocery')
    return render(request, 'dashboard/grocery_purchased.html')

@login_required
def product_edit(request, pk):
 item = Grocery.objects.get(id=pk)
 if request.method =='POST':
    form = GroceryForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return redirect ('dashboard-grocery')
 else:
    form = GroceryForm(instance=item)

    context={
        'form': form,
    }
    return render(request, 'dashboard/grocery_edit.html', context)
