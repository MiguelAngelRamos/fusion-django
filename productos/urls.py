from django.urls import path
from . import views
#* llego con esta base http://127.0.0.1:8000/productos/
app_name = 'producto' # asegurarme que exista el namespace 

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.formulario, name='formulario'), 
    path('<int:producto_id>', views.detail, name="detail"), 
    path('<int:producto_id>/eliminar/', views.eliminar_producto, name="eliminar"),
    path('<int:producto_id>/editar/', views.editar_producto, name='editar')
]
