from django.urls import path
from .views import DocumentoNew

urlpatterns = [
    path('novo/<int:funcionario_id>', DocumentoNew.as_view(), name='create_documento'),
]

