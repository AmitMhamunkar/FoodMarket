from django.urls import path
from orderapp.views import placeOrderView,showOrderView
urlpatterns = [
	path('placeOrderView/',placeOrderView),
	path('showorder/',showOrderView),
]

