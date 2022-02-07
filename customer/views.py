from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q


class CustomerListView(ListView):
    template_name = "customer/customer_list.html"
    paginate_by = 4
    model = Customer

    def get_queryset(self):
        nome = self.request.GET.get('nome')

        if nome:
            object_list = self.model.objects.filter(
                Q(first_name__icontains=nome) | Q(last_name__icontains=nome))
        else:
            object_list = self.model.objects.all()
        return object_list


class CustomerCreateView(CreateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('customer:customer-list')


class CustomerUpdateView(UpdateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self, queryset=None):
        id_cliente = self.kwargs.get('id')
        return get_object_or_404(Customer, pk=id_cliente)

    def get_success_url(self):
        return reverse('customer:customer-list')


class CustomerDeleteView(DeleteView):
    def get_object(self, queryset=None):
        id_cliente = self.kwargs.get('id')
        return get_object_or_404(Customer, pk=id_cliente)

    def get_success_url(self):
        return reverse('customer:customer-list')
