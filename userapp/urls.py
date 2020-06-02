
from django.urls import path
from userapp.views import showAllUser,deleteUserById,createUserView,updateUserById,UserLogin,Logout,restTestView

urlpatterns = [
    path('users/', showAllUser),
	path('delete/<int:id>', deleteUserById),
	path('adduser/', createUserView),
	path('update/',updateUserById),
	path('userlogin/',UserLogin),
	path('logout/',	Logout),
	path('restTest/',restTestView)
	
]

