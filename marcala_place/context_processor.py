from marcala_place.models import Product, Category, Vendor, CartOrder, ProductImages, ProductReview, CartOrderProducts, wishlist_model, Address, Coupon

def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()
    address = Address.objects.get()
   

    # try:
    #    address = Address.objects.get(usuario=request.user)
    # except:
    #     address = None



    return {
        'categoriescf':categories,
        'address':address,
        'vendorscf':vendors,
    }