from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Customer


class CustomerListView(ListView):
    template_name = "customer/customer_list.html"
    model = Customer
    queryset = Customer.objects.all()


class CusomerCreateView(CreateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm

    def form_valid(self, form):
        return super().form_valid(form)
