from django.contrib import admin
from .models import Fornecedor, Produto


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'email', 'telefone', 'endereco')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'quantidade', 'data_validade', 'preco_unidade', 'fornecedor', 'ativo')