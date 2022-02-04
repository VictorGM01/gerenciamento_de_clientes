from django import forms
from .models import Customer


class DateInput(forms.DateInput):
    input_type = "date"


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(label="Nome")
    last_name = forms.CharField(label="Sobrenome")
    email = forms.EmailField(label="E-mail")
    birth_date = forms.DateField(label="Data de Nascimento", widget=DateInput())
    area_code = forms.RegexField(
        label="DDD",
        regex=r"^[0-9]{2}$",
        error_messages={"invalid": "Número de DDD inválido"}
    )
    phone_number = forms.RegexField(
        label="Telefone",
        regex=r"^[0-9]{9}$",
        error_messages={"invalid": "Número de Telefone inválido"}
    )
    country = forms.CharField(label="País")
    state = forms.CharField(label="Estado")
    city = forms.CharField(label="Cidade")

    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'email',
            'birth_date',
            'area_code',
            'phone_number',
            'country',
            'state',
            'city'
        ]