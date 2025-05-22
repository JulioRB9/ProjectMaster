from django import forms


class formularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label="Email", required=True)
    contenido = forms.CharField(widget=forms.Textarea, label="Contenido", required=True)