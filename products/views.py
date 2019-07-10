from django.shortcuts import render,redirect,get_object_or_404
from .models import product
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def aproduct(request):

    if request.method =='POST':
        pass

    else :

        all_products = product.objects.all()


        return render(request,'products/product.html',{'all_products':all_products})

@login_required
def add_product(request):

    if request.method == 'POST':
        
        # prod_t = request.POST['tit']
        prod_u = request.POST['urls']
        image_u = request.POST['image_urls']
        prod_d = request.POST['details']
        try:

            prod_t = request.POST['name']
        except MultiValueDictKeyError:
            prod_t= "  "

        if (prod_d and prod_t and prod_u and image_u) :


            prod = product()
            prod.detail=prod_d
            prod.url=prod_u
            prod.title=prod_t
            prod.image_url= image_u
            prod.date = timezone.datetime.now()
            prod.hunter= request.user

            prod.save()
            return redirect('home')

    return render(request,'products/add.html')


def detail(request,product_id):
    prod = get_object_or_404(product,pk=product_id)
    return render(request,'products/detail.html',{'product':prod})


@login_required
def upvote(request,product_id):
    if request.method == 'POST':
        prod=get_object_or_404(product,pk=product_id)
        prod.likes += 1
        prod.save()

        return render(request,'products/detail.html',{'product':prod})

