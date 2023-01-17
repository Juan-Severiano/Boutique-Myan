from django.db import models


# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=65)

    def __str__(self):
        return self.nome


class SubCategoria(models.Model):
    nome = models.CharField(max_length=65)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null = True
    )

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=65)
    descriçao = models.CharField(max_length=165)
    detalhes_produto = models.TextField()
    marca = models.CharField(max_length=65)
    preço = models.FloatField()
    tamanho = models.CharField( max_length=50)
    estoque = models.IntegerField()
    unidade_tamanho = models.CharField(max_length=65)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null = True
    )
    sub_categoria = models.ForeignKey(
        SubCategoria, on_delete=models.SET_NULL, null=True
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    update_em = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='app/imagens/%Y/%m/%d')


    def __str__(self):
        return self.nome