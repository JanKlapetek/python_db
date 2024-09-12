from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from .forms import CartItemForm

def add_to_cart(request):
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_cart')
    else:
        form = CartItemForm()
    return render(request, 'cart/add_to_cart.html', {'form': form})

def edit_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        form = CartItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('view_cart')
    else:
        form = CartItemForm(instance=item)
    return render(request, 'cart/edit_cart_item.html', {'form': form})

def delete_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('view_cart')

def view_cart(request):
    items = CartItem.objects.all()
    return render(request, 'cart/view_cart.html', {'items': items})
