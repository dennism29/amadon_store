from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    item = Product.objects.get(id=request.POST["id"])
    price_from_form = float(item.price)
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    request.session['total_charge'] = total_charge
    return redirect("/checkout")

def checkout_page(request):
    all_orders = Order.objects.all()
    total_quantity = 0
    total_spending = 0
    for order in all_orders:
        total_quantity = total_quantity + order.quantity_ordered
        total_spending = total_spending + order.total_price
    context = {
        "total_item_qty": total_quantity,
        "total_spending": total_spending
    }
    return render(request, "store/checkout.html", context)