from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class ModelBase(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Fornecedor(ModelBase):
    descricao = models.CharField(max_length=100, null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=15, blank=False, unique=True)
    endereco = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.descricao


class Produto(ModelBase):
    descricao = models.CharField(max_length=100, null=False, blank=False, unique=True)
    quantidade = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    data_validade = models.DateTimeField(blank=False, unique=True)
    preco_unidade = models.DecimalField(validators=[MinValueValidator(1)], max_digits=20, decimal_places=2)
    fornecedor = models.ForeignKey(Fornecedor, related_name='produtos', on_delete=models.CASCADE)
    ativo = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.descricao
