from django import forms


class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    emailUsuario = forms.EmailField(label="Email", required=True)
    contenido = forms.CharField(widget=forms.Textarea, label="Contenido", required=True)