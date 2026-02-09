from django import forms

class FormularioContacto(forms.Form):
    # Los nombres de estas variables DEBEN coincidir con el atributo name="" del HTML
    nombre = forms.CharField(label="Nombre", required=True, max_length=100)
    email = forms.EmailField(label="Email", required=True)
    servicio = forms.CharField(label="Servicio", required=False) # Nuevo campo del select
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea, required=True)