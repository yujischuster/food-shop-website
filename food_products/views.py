from django.shortcuts import render
from .models import ProductDetail


def product_list(request):
    # gets the value from the url parameter (from the GET request)
    selected_category = request.GET.get('category')
    # filters by selected category
    productinfo = ProductDetail.objects.all().order_by('-created_at').filter(category=selected_category)
    return render(request, 'food_products/product_list.html', {'productinfo': productinfo}) 

def product_detail(request, slug):
    # return HttpResponse(slug)
    indv_product = ProductDetail.objects.get(slug=slug)
    return render(request, 'food_products/product_detail.html', {'indv_product': indv_product})

