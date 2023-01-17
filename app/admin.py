from django.contrib import admin
from .models import Categoria, SubCategoria, Produto

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ...



@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    ...



@admin.register(SubCategoria)
class SubCategoriaAdmin(admin.ModelAdmin):
    ...
