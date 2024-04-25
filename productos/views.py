from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required
def index(request):
    productos = Producto.objects.all()
    print(productos)
    return render(
        request,
        'index.html',
        { 'productos': productos }
    )

@login_required
@permission_required('productos.add_producto', raise_exception=True)
def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST) # Aqui en el request.POST viene nombre, stock, categoria, imagen
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()
    return render(
        request,
        'producto_form.html',
        {'form': form }
    )
@login_required
def detail(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detail.html', context={'producto': producto})

# def detail(request, producto_id):
#     try:
#         producto = Producto.objects.get(id=producto_id)
#         return render(request, 'detail.html', context={'producto': producto})
#     except Producto.DoesNotExist:
#         raise Http404()