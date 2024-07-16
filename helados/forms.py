from django import forms
from.models import HeladoRecipienteCristal,Sabor,Pedido,DetallePedido

        
class HeladoRecipienteCristalForm(forms.ModelForm):
    class Meta:
        model = HeladoRecipienteCristal
        fields =  fields = ['nombre', 'descripcion', 'precio','foto']

class SaborForm(forms.ModelForm):
    class Meta:
        model = Sabor
        fields =  fields = ['nombre', 'descripcion', 'precio', 'foto']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = []  # No incluyas ningún campo aquí, ya que los detalles del pedido se agregarán dinámicamente
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agrega un campo para cada detalle del pedido
        for sabor in Sabor.objects.all():
            field_name = f'sabor_{sabor.id}'
            self.fields[field_name] = forms.IntegerField(min_value=0, label=f'Cantidad de {sabor.nombre}')