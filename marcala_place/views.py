from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from taggit.models import Tag

from marcala_place.models import Product, Category, Vendor, CartOrder, ProductImages, ProductReview, CartOrderProducts, wishlist_model, Address, Coupon

# Create your views here.
#VIEWS DE LOS PRODUCTOS 
def index(request):
    Products = Product.objects.filter(product_status="published", featured=True).order_by("-id")

    context = {
        "productsf":Products
    }
    return render(request, 'marcala_place/index.html', context)

#VIEWS DE LAS LISTAS DE LOS PRODUCTOS
def product_list_view(request):
    products = Product.objects.filter(product_status="published").order_by("-id")
    #tags = tags.objects.all().order_by("-id")[:6]

    context = {
        "productsf":products,
      #  "tags":tags,
    }
    return render(request, 'marcala_place/product-list.html', context)

#VIEWS DE LAS CATEGORIAS DE LOS PRODUCTOS
def category_list_view(request):
    categories = Category.objects.all()
   

    context = {
        "categoriescf":categories
    }
    return render(request, 'marcala_place/category-list.html', context)

#VIEWS DE LA LISTA DE LOS PRODUCTOS PERO EN SUS CATEGORIAS 
def category_product_list__view(request, cid):

    category = Category.objects.get(cid=cid) # tecnologia, construccion
    products = Product.objects.filter(product_status="published", category=category)

    context = {
        "categoryf":category,
        "productsf":products,
    }
    return render(request, "marcala_place/category-product-list.html", context)

#VIEWS PARA LOS DETALLES DE LOS PORDUCTOS DESDE CATEGORIAS OSEA ENTRAS A LOS PRODUCTOS DE UNA CATEGORIAS JSJS
def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    #product = get_object_or_404(Product, pid=pid)
    products = Product.objects.filter(category=product.category).exclude(pid=pid)

    # Getting all reviews related to a product
   # reviews = ProductReview.objects.filter(product=product).order_by("-date")

    # Getting average review
   # average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    # Product Review form
   # review_form = ProductReviewForm()


    # make_review = True 

   # if request.user.is_authenticated:
   #AUN NO TIENES EL AUTENTICADOR DE USUARIO BABOSO 
    #address = Address.objects.get(status=True, usuario=request.user)
    address = Address.objects.get()
    #     user_review_count = ProductReview.objects.filter(user=request.user, product=product).count()

    #     if user_review_count > 0:
    #         make_review = False
    
    #address = "Login To Continue"


    p_image = product.p_images.all()

    context = {
        "p": product,
        "address": address,
    #     "make_review": make_review,
    #     #"review_form": review_form,
        "p_image": p_image,
    #    # "average_rating": average_rating,
    #     "reviews": reviews,
        "productsf": products,
        #"product": product
    }

    return render(request, "marcala_place/product-detail.html", context)

#VIEWS PARA LOS VENDEDORES O TIENDAS ES LA LISTA 
def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {
        "vendorf": vendors,
    }
    return render(request, "marcala_place/vendor-list.html", context)

#VIEWS PARA LOS DETALLES DE LOS VENDEDORES O TIENDAS JSJSJS
def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor, product_status="published").order_by("-id")

    context = {
        "vendorf": vendor,
        "productsf": products,
    }
    return render(request, "marcala_place/vendor-detail.html", context)

#VIEWS PARA EL CARRITO DE COMPRAS 
def add_to_cart(request):
    cart_product = {}

    cart_product[str(request.GET['id'])] = {
        'title': request.GET['title'],
        'qty': request.GET['qty'],
        'price': request.GET['price'],
        'image': request.GET['image'],
        'pid': request.GET['pid'],
    }

    if 'cart_data_obj' in request.session:
        if str(request.GET['id']) in request.session['cart_data_obj']:

            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data
        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data

    else:
        request.session['cart_data_obj'] = cart_product
    return JsonResponse({"data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj'])})

def cart_view(request):
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
        return render(request, "marcala_place/cart.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount})
    else:
        messages.warning(request, "Your cart is empty")
        return redirect("marcala_place:index")