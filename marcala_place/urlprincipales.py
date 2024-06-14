from django.urls import path
from marcala_place.views import index, product_list_view, category_list_view, category_product_list__view, product_detail_view, vendor_list_view, vendor_detail_view, add_to_cart,cart_view

app_name = "marcala_place"
urlpatterns =[
    #URL PARA PAG PRINCIPALES EL INDEX
    path("", index, name="index"),
    
    #URL PARA LAS PAG DE PRODUCTOS
    path("products/", product_list_view, name="product-list"),
    path("product/<pid>/", product_detail_view, name="product-detail"), 

    #URL PARA LAS PAG DE CATEGORIAS DE LOS PRODUCTOS
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>/", category_product_list__view, name="category-product-list"),
    
    #URL PARA LOS VENDEDORES O TIENDAS 
    path("vendors/", vendor_list_view, name="vendor-list"),
    path("vendor/<vid>/", vendor_detail_view, name="vendor-detail"),

    #URL PARA EL CARRITO DE COMPRAS 
    path("add-to-cart/", add_to_cart, name="add-to-cart"),
    path("cart/", cart_view, name="cart"),
]