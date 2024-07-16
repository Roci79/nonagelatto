"""
URL configuration for Heladeria_nona project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path,include

urlpatterns = [
    path('home/', views.home, name='home' ),
    path('about/', views.about, name='about'),
    path('productos/', views.productos, name='productos'),
    path('contactar/', views.contactar, name='contactar'),
    path('servicios/', views.servicios, name='servicios'),
    path('galeria/', views.galeria, name='galeria'),
    path('sabor/', views.sabor, name='sabor'),
    path('<int:id_helado>/', views.detalle_helados, name='detalle_helados'),
    path('sabor<int:id_sabor>/', views.detalle_sabores, name='detalle_sabores'),
    path('recipiente/', views.detalle_recipiente, name='detalle_recipiente'),
    path('ver_carro/', views.ver_carro, name='ver_carro'),
    path('carro/<str:tipo_producto>/<int:producto_id>/', views.carro, name='carro'),
    path('agregar_producto/<str:tipo_producto>/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('eliminar_producto/<int:item_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('helados/restar_producto/<str:tipo_producto>/<int:producto_id>/', views.restar_producto, name='restar_producto'),
    path('ver_carro/', views.ver_carro, name='ver_carro'),
    path('pagar/', views.pagar, name='pagar'),
    path('fin/', views.fin, name='fin'),
    
 

]
