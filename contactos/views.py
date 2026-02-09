from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

def contacto(request):
    formulario = FormularioContacto()

    if request.method == "POST":
        formulario = FormularioContacto(data=request.POST)
        
        if formulario.is_valid():
            # 1. Recuperamos los datos con los NOMBRES NUEVOS
            nombre = formulario.cleaned_data["nombre"]
            email = formulario.cleaned_data["email"]     # Antes era emailUsuario
            servicio = formulario.cleaned_data["servicio"] # Nuevo campo
            mensaje = formulario.cleaned_data["mensaje"] # Antes era contenido

            # 2. Plantilla del correo actualizada con mejor diseño
            html_message = f"""
            <div style="font-family: Arial, sans-serif; color: #333; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 8px; overflow: hidden;">
                <div style="background-color: #1A365D; padding: 20px; text-align: center;">
                    <h2 style="color: #ffffff; margin: 0;">Nuevo Lead desde la Web</h2>
                </div>
                <div style="padding: 20px;">
                    <p style="font-size: 16px;">Has recibido una nueva solicitud de presupuesto:</p>
                    
                    <table style="width: 100%; border-collapse: collapse; margin-top: 15px;">
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 10px; font-weight: bold; width: 30%;">Cliente:</td>
                            <td style="padding: 10px;">{nombre}</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 10px; font-weight: bold;">Email:</td>
                            <td style="padding: 10px;"><a href="mailto:{email}" style="color: #2B6CB0;">{email}</a></td>
                        </tr>
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 10px; font-weight: bold;">Interés:</td>
                            <td style="padding: 10px; color: #d97706; font-weight: bold;">{servicio}</td>
                        </tr>
                    </table>

                    <div style="background-color: #f8fafc; padding: 15px; border-left: 4px solid #2B6CB0; margin-top: 20px;">
                        <p style="margin: 0; font-style: italic;">"{mensaje}"</p>
                    </div>
                </div>
                <div style="background-color: #f1f1f1; padding: 10px; text-align: center; font-size: 12px; color: #888;">
                    Mensaje enviado automáticamente desde tu sistema Django.
                </div>
            </div>
            """

            # 3. Configuración del envío
            enviar_mensaje = EmailMessage(
                subject=f"📦 Nuevo Lead: {nombre} - {servicio}", # Asunto más claro
                body=html_message,
                from_email="tu_correo_configurado@gmail.com", # Pon aquí el correo que envía (settings.EMAIL_HOST_USER)
                to=["julio.rivera.1596@gmail.com"],
                reply_to=[email]
            )
            
            enviar_mensaje.content_subtype = "html"

            try:
                enviar_mensaje.send()
                # Redirección de éxito
                return redirect("/contactos/?okEnviado") 
            except Exception as e:
                # Es útil imprimir el error en consola para depurar si falla
                print(f"Error enviando correo: {e}")
                return redirect("/contactos/?failNoEnviado")
        else:
            # Si el formulario no es válido, sería bueno saber por qué (debugging)
            print(formulario.errors)

    return render(request, "contactos/contacto.html", {'miformulario': formulario})