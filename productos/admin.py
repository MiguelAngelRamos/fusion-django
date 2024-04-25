from django.contrib import admin
from .models import Categoria, Producto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    
class ProductoAdmin(admin.ModelAdmin):
    exclude = ('create_at', )
    list_display = ('id', 'nombre', 'image', 'precio', 'stock', 'create_at')
    

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
