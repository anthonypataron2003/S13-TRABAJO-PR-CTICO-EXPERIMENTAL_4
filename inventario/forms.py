from django import forms
from .models import Producto, Categoria
class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=['nombre','categoria','precio','stock','minimo']
    def clean_precio(self):
        p=self.cleaned_data['precio']
        if p<=0: raise forms.ValidationError('El precio debe ser positivo.')
        return p
class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=['nombre']
