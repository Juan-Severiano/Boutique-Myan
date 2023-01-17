from django.shortcuts import render, get_object_or_404
from app.models import Produto

# Create your views here.

def home(request):
    produtos = Produto.objects.filter(publicado=True).order_by('-id')
    return render(request,'app/pages/home.html', context={
        'produtos' : produtos
    })


def categoria(request, id_categoria):
    produtos = Produto.objects.filter(
        publicado=True,
        categoria__id=id_categoria,
        ).order_by('-id')
    return render(request,'app/pages/home.html', context={
        'produtos' : produtos
    })

def produto(request, id):
    produto = get_object_or_404(Produto, pk=id, publicado=True)
    return render(request, 'app/pages/produto-view.html', context={
        'produto' : produto,
        'is_detail_page':True,
    })