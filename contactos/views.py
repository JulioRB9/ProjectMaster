from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
# https://www.youtube.com/watch?v=_BOOv6GK-68&list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB&index=45
def contacto(request):

    formulario = FormularioContacto()
    if request.method == "POST":
        formulario = FormularioContacto(data=request.POST)
        if formulario.is_valid():
            # Aquí puedes procesar los datos del formulario
            # Por ejemplo, enviar un correo electrónico o guardar en la base de datos
            nombre = formulario.cleaned_data["nombre"]
            email_usuario = formulario.cleaned_data["emailUsuario"]
            contenido = formulario.cleaned_data["contenido"]
            # print(f"Nombre: {nombre}, Email: {email}, Mensaje: {mensaje}")

            # Enviar correo electrónico
            enviar_mensaje = EmailMessage(
                subject="Nuevo mensaje de contacto de APP django",
                body=f"El usuario {nombre} con email {email_usuario} ha enviado el siguiente mensaje:\n\n{contenido}",
                from_email="",
                to=["julio.rivera.1596@gmail.com"],
                reply_to=[email_usuario]
            )
            
            try:
                enviar_mensaje.send()
                return redirect("/contactos/?okEnviado")
            except Exception as e:
                return redirect("/contactos/?failNoEnviado")

    return render(request, "contactos/contacto.html", {'miformulario': formulario})