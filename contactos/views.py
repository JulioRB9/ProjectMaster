from django.shortcuts import render
from .forms import FormularioContacto
from django.shortcuts import redirect
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
            nombre = request.POST.get("nombre")
            emailUsuario = request.POST.get("emailUsuario")
            contenido = request.POST.get("contenido")
            # print(f"Nombre: {nombre}, Email: {email}, Mensaje: {mensaje}")

            # Enviar correo electrónico
            emailUsuario = EmailMessage(
                "Nuevo mensaje de contacto de APP django",
                "El usuario {} con email {} ha enviado el siguiente mensaje:\n\n{}".format(
                    nombre, emailUsuario, contenido
                ),["julio.rivera.1596@gmail.com"],reply_to=[emailUsuario])
                
            try:
                emailUsuario.send()
                return redirect("/contactos/?okEnviado")
            except:
                return redirect("/contactos/?failNoEnviado")

    return render(request, "contactos/contacto.html", {'miformulario': formulario})