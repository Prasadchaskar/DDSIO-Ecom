from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('productdetail/<int:myid>',views.Details,name='productdetail'),
]