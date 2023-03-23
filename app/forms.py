from datetime import date
from .models import Estudiante, Pago, Inscription
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class Create_EstudianteForm(forms.ModelForm):

    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': DateInput(),
            'observaciones': forms.TextInput(attrs={'row': 1}),
        }


class Create_InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = ('curso', 'curso_nivel', 'trimestre')



class Create_PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ('cargo_tipo', 'fecha_pago', 'monto_valor', 'monto_pagar')

class Update_EstudianteForm(forms.ModelForm):

    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': DateInput(),
            'observaciones': forms.TextInput(attrs={'row': 1}),
        }


class Update_InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = '__all__'



class Update_PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = '__all__'