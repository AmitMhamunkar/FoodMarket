from django.urls import path
from cartapp.views import ShowAddToCartView,addToCartView,showCartView,deleteCartView,CheckQuantitybeforeadding,totalPriceDisplay

urlpatterns = [
   path('addToCart/<int:id>', ShowAddToCartView),
	path('addToCart', addToCartView),
	path('showcart/',showCartView),
	path('delete/<int:id>',deleteCartView),
	path('Check/',CheckQuantitybeforeadding),
	path('total/',totalPriceDisplay)
]

