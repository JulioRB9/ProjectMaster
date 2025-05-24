from django.shortcuts import render
from .forms import formularioContacto
from django.shortcuts import redirect
from django.core.mail import EmailMessage

# Create your views here.
# https://www.youtube.com/watch?v=_BOOv6GK-68&list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB&index=45
def contacto(request):
    formulario = formularioContacto()

    if request.method == "POST":
        formulario = formularioContacto(request.POST)
        if formulario.is_valid():
            # Aquí puedes procesar los datos del formulario
            # Por ejemplo, enviar un correo electrónico o guardar en la base de datos
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            mensaje = request.POST.get("mensaje")
            # print(f"Nombre: {nombre}, Email: {email}, Mensaje: {mensaje}")

            # Enviar correo electrónico
            email = EmailMessage(
                "Nuevo mensaje de contacto de APP django",
                "El usuario {} con email {} ha enviado el siguiente mensaje:\n\n{}".format(
                    nombre, email, mensaje
                ),["julio.rivera.1596@outlook.com"],reply_to=[email])
                
            try:
                email.send()
                return redirect("/contactos/?ok")
            except:
                return redirect("/contactos/?fail")

    return render(request, "contactos/contacto.html", {"miformulario": formulario})