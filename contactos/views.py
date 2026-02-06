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
            

            html_message = f"""
                <h2 style="color: #2c3e50;">Recibistes un nuevo mensaje</h2>
                <p><strong>Nombre:</strong> {nombre}</p>
                <p><strong>Email:</strong> {email_usuario}</p>
                <p><strong>Mensaje:</strong></p>
                <div style="background-color: #f4f4f4; padding: 15px; border-left: 4px solid #3498db;">
                    {contenido}
                </div>
                <p style="font-size: 0.9em; color: #888;">Este mensaje fue enviado desde el formulario de contacto de tu sitio web.</p>
                """
            # Enviar correo electrónico
            enviar_mensaje = EmailMessage(
                subject="📩 Sistema - APP Django",
                body=html_message,
                from_email="",
                to=["julio.rivera.1596@gmail.com"],
                reply_to=[email_usuario]
            )
            # Configurar el contenido del mensaje como HTML
            enviar_mensaje.content_subtype = "html"  # Importante: indica que el contenido es HTML
            try:
                enviar_mensaje.send()
                return redirect("/contactos/?okEnviado")
            except Exception as e:
                return redirect("/contactos/?failNoEnviado")

    return render(request, "contactos/contacto.html", {'miformulario': formulario})