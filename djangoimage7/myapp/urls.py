from django.urls import path
from.import views

urlpatterns = [
    path('',views.firstone),
    path('asd/',views.form, name='card'),
    path('abc/',views.view,name='form'),
    path('ab/<int:pk>', views.delete, name='del')

]