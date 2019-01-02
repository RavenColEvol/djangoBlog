from django.urls import path
from .views import index,detail,addPost,addUser,UserAuth,userlogout

urlpatterns = [
    path('',index,name='index'),
    path('<int:id>/',detail,name='detail'),
    path('addpost/',addPost,name="addpost"),
    path('login/',addUser,name="adduser"),
    path('signin/',UserAuth,name="signin"),
    path('logout/',userlogout,name="userlogout")
]