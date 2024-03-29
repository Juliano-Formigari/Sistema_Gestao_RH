from django.urls import path
from .views import (
    DepartamentoList, 
    DepartamentoNew, 
    DepartamentoEdit,
    DepartamentoDelete,
)


urlpatterns = [
    path('', DepartamentoList.as_view(), name='list_departamentos'),
    path('novo/', DepartamentoNew.as_view(), name='create_departamento'),
    path('editar/<int:pk>/', DepartamentoEdit.as_view(), name='update_departamento'),
    path('deletar/<int:pk>/', DepartamentoDelete.as_view(), name='delete_departamento'),
]
