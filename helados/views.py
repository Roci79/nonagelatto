# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import HeladoRecipienteCristal,Sabor
from django.http import HttpResponse
from .carro import Carro


def home(request):

   return render(request,'helados/index.html')

def about(request):

   return render(request,'helados/about.html')

def productos(request):
     context = {
        'lista_helados': HeladoRecipienteCristal.objects.all(),
        'total_productos': request.session.get('total_productos', 0),
        'total_pagar': request.session.get('total_pagar', 0),
    }
     return render(request,'helados/productos.html',context)

def contactar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        motivo = request.POST.get('motivo')
        mensaje = request.POST.get('mensaje')
        
        return HttpResponse('<script>alert("El formulario se ha enviado correctamente"); window.location.href = "http://localhost:8000/helados/contactar";</script>')
    else:
        return render(request, 'helados/contactar.html')

   

def servicios(request):

   return render(request,'helados/servicios.html')

def galeria(request):

   return render(request,'helados/galeria.html')

def sabor(request):
     context = {
        'lista_sabores': Sabor.objects.all(),
        'total_productos': request.session.get('total_productos', 0),
        'total_pagar': request.session.get('total_pagar', 0),
    }
     return render(request,'helados/sabor.html',context)
  
def detalle_helados(request, id_helado):
      context={
         'helado': HeladoRecipienteCristal.objects.get(pk=id_helado)
      }
      return render(request,'helados/detalle_helados.html',context)
   
def detalle_sabores(request, id_sabor):
   context = {
      'sabor': Sabor.objects.get(pk=id_sabor)
   }
   return render(request, 'helados/detalle_sabores.html', context)

def detalle_recipiente(request):
   
   return render(request, 'helados/detalle_recipiente.html')

def ver_carro(request):
    carro = Carro(request)
    carrito = carro.carro  
    total_productos = sum(item['cantidad'] for item in carrito.values())
    total_pagar = sum(float(item['precio']) * item['cantidad'] for item in carrito.values())

    request.session['total_pagar'] = total_pagar
    
    tipo_producto = request.GET.get('tipo_producto', '') 
    return render(request, 'helados/carro.html', {
        'carrito': carrito,
        'total_productos': total_productos,
        'total_pagar': total_pagar,
        'tipo_producto': tipo_producto,   
    })

def carro(request, tipo_producto, producto_id):
    if tipo_producto == 'helado':
        producto = get_object_or_404(HeladoRecipienteCristal, id=producto_id)
    elif tipo_producto == 'sabor':
        producto = get_object_or_404(Sabor, id=producto_id)

    carro = Carro(request)
    carro.agregar(producto, tipo_producto)

    carrito = carro.carro
    total_productos = sum(item['cantidad'] for item in carrito.values())
    total_pagar = sum(float(item['precio']) * item['cantidad'] for item in carrito.values())

    request.session['total_pagar'] = total_pagar
    request.session['total_productos'] = total_productos

    
    return redirect(request.META.get('HTTP_REFERER'))
    
    # return render(request, 'helados/carro.html', {
    #     'carrito': carrito,
    #     'total_productos': total_productos,
    #     'total_pagar': total_pagar
    # })

def agregar_producto(request,tipo_producto, producto_id):
   if tipo_producto == 'helado':
        producto = get_object_or_404(HeladoRecipienteCristal, id=producto_id)
   elif tipo_producto == 'sabor':
        producto = get_object_or_404(Sabor, id=producto_id)
   carro = Carro(request)
   carro.agregar(producto, tipo_producto)
   return redirect('ver_carro')

def eliminar_producto(request, item_id):
    carro = Carro(request)
    
    try:
        producto = get_object_or_404(HeladoRecipienteCristal, id=item_id)
    except:
        producto = get_object_or_404(Sabor, id=item_id)
    
    carro.eliminar(producto.id)
    return redirect('ver_carro')


def restar_producto(request, tipo_producto, producto_id):
    if tipo_producto == 'helado':
        producto = get_object_or_404(HeladoRecipienteCristal, id=producto_id)
    elif tipo_producto == 'sabor':
        producto = get_object_or_404(Sabor, id=producto_id)
   
    carro = Carro(request)
    carro.restar_producto(producto)
    return redirect('ver_carro')

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect('carro')

@login_required(login_url='/usuarios/login_user')
def pagar(request):
    total_pagar = request.session.get('total_pagar', 0)
    return render(request, 'helados/pagar.html', {'total_pagar': total_pagar})

def fin(request):
   return render(request,'helados/fin.html')