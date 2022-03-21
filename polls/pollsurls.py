from django.urls import path,include
from django.conf.urls import url
from.import views
app_name="polls"
urlpatterns = [
    url(r'^account/activate/',views.activate,name="activate"),
    path('', views.index, name='index'),
    path('signup',views.signup, name="signup"),
    path('slogin',views.slogin, name="login"),
    #
    # url(r'login',views.userlogin,name="login")
]