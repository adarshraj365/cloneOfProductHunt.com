
from django.urls import path
from . import views

urlpatterns = [
    path('',views.aproduct,name='home'),
    path('add/',views.add_product,name='add'),
    path('<int:product_id>',views.detail,name='detail'),
    path('<int:product_id>/upvote',views.upvote,name='upvote'),
]
