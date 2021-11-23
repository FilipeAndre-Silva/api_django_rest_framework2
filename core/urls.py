from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import FornecedorList, FornecedorDetail, ProdutoList, ProdutoDetail, FornecedorViewSet, ProdutoViewSet


router = SimpleRouter()
router.register('fornecedores', FornecedorViewSet)
router.register('produtos', ProdutoViewSet)

urlpatterns = [
	path('fornecedores/', FornecedorList.as_view(), name='fornecedor'),
	path('fornecedores/<int:pk>/produto/<int:produto_pk>', ProdutoList.as_view(), name='fornecedor'),
	path('fornecedores/<int:pk>/', FornecedorDetail.as_view(), name='fornecedor'),
]
