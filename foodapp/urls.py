
from django.urls import path
from foodapp.views import showAllFoodsView,deleteFoodByIdView,createFoodView,updateFoodByIdView,filterFoodbyname

urlpatterns = [
    path('foods/', showAllFoodsView),
	path('delete/<int:id>',deleteFoodByIdView ),
	path('addfood/', createFoodView),
	path('update/<int:id>',updateFoodByIdView),
	path('search/<str:name>',filterFoodbyname)
]

