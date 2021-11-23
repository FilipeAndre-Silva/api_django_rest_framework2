from rest_framework import serializers
from .models import Fornecedor, Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
            'id',
            'descricao',
            'quantidade',
            'data_validade',
            'preco_unidade',
            'fornecedor',
            'ativo',
        )

    def validate_quantidade(self, valor):
        if valor <= 100:
            return valor
        raise serializers.ValidationError("A quantidade não pode ser maior que 100 unidades.")


class FornecedorSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(many=True, read_only=True)
    quantidade_produtos = serializers.SerializerMethodField()

    class Meta:
        extra_kargs = {
            'email': {'write_only': True}  # definindo o email não vai ser apresentado em uma consulta de fornecedores
        }
        model = Fornecedor
        fields = (
            'id',
            'descricao',
            'email',
            'telefone',
            'endereco',
            'quantidade_produtos',
            'produtos',
        )

    def get_quantidade_produtos(self, obj):
        produtos = Produto.objects.filter(fornecedor=obj.id)
        return len(produtos)
