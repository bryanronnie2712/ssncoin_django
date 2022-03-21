from django.urls import path
from.import views
from django.conf.urls import url
app_name="blockapp"
urlpatterns = [
    path('', views.home, name='home'),
    path('details',views.details,name="details"),
    path('mine',views.mine,name="mine"),
    path(r'mine1/<int:id>',views.mine1,name="mine1"),
    url(r'logout',views.userlogout,name="logout"),
    #url(r'login',views.userlogin,name="login")
]
