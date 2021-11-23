from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import EhSuperUser
from .serializers import FornecedorSerializer, ProdutoSerializer
from rest_framework import generics, permissions
from .models import Fornecedor, Produto
from rest_framework import viewsets
from rest_framework import mixins


class FornecedorList(generics.ListCreateAPIView):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer


class FornecedorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (EhSuperUser, permissions.DjangoModelPermissions,)
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer


class ProdutoList(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get_queryset(self):
        if self.kwargs.get('produto_pk'):
            return self.queryset.filter(fornecedor_id=self.kwargs.get('produto_pk'))
        return self.queryset.all()


class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

    @action(detail=True, methods=['get'])
    def produtos(self, request, pk=None):
        fornecedor = self.get_object()
        serializer = ProdutoSerializer(fornecedor.produtos.all(), many=True)
        return Response(serializer.data)


"""class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer"""
class ProdutoViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
