from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
 
from .models import *
from .cart import Cart
from .forms import OrderForm


# Create your views here.


# cart Function
def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect("cart_view")


def change_quantity(request, product_id):
    action = request.GET.get("action", "")

    if action:
        quantity = 1
        if action == "decrease":
            quantity = -1

        cart = Cart(request)
        cart.add(product_id, quantity, True)

    return redirect("cart_view")


def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    return redirect("cart_view")


def cart_view(request):
    cart = Cart(request)
    return render(
        request,
        "store/cart_view.html",
        {
            "cart": cart,
        },
    )


# wselt ll partie 8


@login_required
def checkout(request):
    cart = Cart(request)

    # bech ki yebda l panier fera8 ma yod5olch ll checkout
    if cart.get_total_cost() == 0:
        return redirect("cart_view")

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            totla_price = 0

            for item in cart:
                product = item["product"]
                totla_price += product.price * item["quantity"]

            order = form.save(commit=False)
            order.created_by = request.user
            order.paid_amount = totla_price
            order.save()

            for item in cart:
                product = item["product"]
                quantity = int(item["quantity"])
                price = product.price * quantity
                item = OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=price,
                    quantity=quantity,
                )

                cart.clear()

            return redirect("myaccount")
    else:
        form = OrderForm()
    return render(
        request,
        "store/checkout.html",
        {
            "cart": cart,
            "form": form,
        },
    )


# End cart Function


def search(request):
    query = request.GET.get("query", "")
    products = Product.objects.filter(status=Product.ACTIVE).filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    print(products)
    return render(
        request,
        "store/search.html",
        {
            "query": query,
            "products": products,
        },
    )


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status=Product.ACTIVE)
    return render(
        request,
        "store/category_detail.html",
        {
            "category": category,
            "products": products,
        },
    )


def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)
    return render(request, "store/product_detail.html", {"product": product})
