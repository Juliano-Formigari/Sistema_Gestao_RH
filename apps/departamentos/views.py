from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView,
    DeleteView,
)
from .models import Departamento
from django.urls import reverse_lazy


class DepartamentoList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)
    

class DepartamentoNew(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoNew, self).form_valid(form)


class DepartamentoEdit(UpdateView):
    model = Departamento
    fields = ['nome']


class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')
