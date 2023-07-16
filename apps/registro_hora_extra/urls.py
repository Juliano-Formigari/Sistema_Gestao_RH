from django.urls import path
from .views import (
    HoraExtraList,
    HoraExtraEdit,
    HoraExtraDelete,
)

urlpatterns = [
    path('', HoraExtraList.as_view(),name='list_horas_extras'),
    path('editar/<int:pk>', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('deletar/<int:pk>', HoraExtraDelete.as_view(), name='delete_hora_extra'),
]
