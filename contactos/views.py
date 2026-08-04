from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from django.conf import settings

def contacto(request):
    formulario = FormularioContacto()

    if request.method == "POST":
        formulario = FormularioContacto(data=request.POST)
        
        if formulario.is_valid():
            # 1. Recuperar los datos validados
            nombre = formulario.cleaned_data["nombre"]
            email = formulario.cleaned_data["email"]
            servicio = formulario.cleaned_data.get("servicio", "General")
            mensaje = formulario.cleaned_data["mensaje"]

            # 2. Plantilla HTML con tipografía moderna, tarjeta elevada y botón de respuesta rápida
            html_message = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <style>
                    body {{ font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background-color: #f8fafc; margin: 0; padding: 20px; }}
                    .card {{ max-width: 600px; margin: 0 auto; background: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 12px 35px rgba(15, 23, 42, 0.1); border: 1px solid #e2e8f0; }}
                    .header {{ background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #1a365d 100%); padding: 32px 25px; text-align: center; color: #ffffff; position: relative; }}
                    .brand-badge {{ display: inline-block; background: rgba(56, 189, 248, 0.18); border: 1px solid rgba(56, 189, 248, 0.35); color: #38bdf8; font-size: 11px; font-weight: 700; padding: 5px 14px; border-radius: 20px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px; }}
                    .brand-title {{ font-size: 26px; font-weight: 800; margin: 0; color: #ffffff; letter-spacing: -0.5px; }}
                    .brand-title span {{ color: #38bdf8; }}
                    .body-content {{ padding: 32px 28px; }}
                    .lead-intro {{ font-size: 15px; color: #475569; margin-bottom: 25px; line-height: 1.6; }}
                    .info-table {{ width: 100%; border-collapse: collapse; margin-bottom: 25px; background: #f8fafc; border-radius: 12px; overflow: hidden; border: 1px solid #e2e8f0; }}
                    .info-table td {{ padding: 14px 18px; font-size: 14px; border-bottom: 1px solid #e2e8f0; }}
                    .info-table tr:last-child td {{ border-bottom: none; }}
                    .info-label {{ font-weight: 700; color: #1e293b; width: 38%; }}
                    .info-value {{ color: #334155; font-weight: 500; }}
                    .service-badge {{ display: inline-block; background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); color: #ffffff; padding: 5px 14px; border-radius: 6px; font-size: 12px; font-weight: 700; box-shadow: 0 2px 8px rgba(37, 99, 235, 0.3); }}
                    .message-box {{ background-color: #f1f5f9; border-left: 4px solid #2563eb; padding: 20px; border-radius: 8px; margin-bottom: 28px; }}
                    .message-label {{ font-size: 11px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }}
                    .message-text {{ font-size: 14px; color: #0f172a; line-height: 1.7; margin: 0; font-style: italic; }}
                    .btn-reply {{ display: inline-block; background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); color: #ffffff !important; text-decoration: none; padding: 13px 30px; border-radius: 50px; font-weight: 700; font-size: 14px; box-shadow: 0 4px 16px rgba(37, 99, 235, 0.4); text-align: center; }}
                    .footer {{ background-color: #f8fafc; padding: 18px 25px; text-align: center; font-size: 12px; color: #64748b; border-top: 1px solid #e2e8f0; }}
                </style>
            </head>
            <body>
                <div class="card">
                    <div class="header">
                        <!-- Brand Monogram Logo Oficial -->
                        <div style="width: 50px; height: 50px; border-radius: 50%; background-color: #0f172a; color: #ffffff; font-weight: 800; font-size: 1.25rem; font-family: Arial, sans-serif; display: inline-block; text-align: center; border: 2px solid #ffffff; outline: 2px solid #38bdf8; box-shadow: 0 4px 14px rgba(0,0,0,0.35); margin: 0 auto 14px auto; vertical-align: middle;">
                            <span style="line-height: 50px; text-align: center; display: block; font-family: Arial, sans-serif;">JR</span>
                        </div>
                        <br>
                        <div class="brand-badge">⚡ NUEVA SOLICITUD RECIBIDA</div>
                        <h1 class="brand-title">Julio<span>.dev</span></h1>
                        <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 13px;">Sistema de Gestión de Pedidos & Logística</p>
                    </div>
                    <div class="body-content">
                        <p class="lead-intro">Se ha registrado una nueva consulta desde el formulario web de contactos. A continuación los detalles:</p>
                        
                        <table class="info-table">
                            <tr>
                                <td class="info-label">👤 Cliente:</td>
                                <td class="info-value"><strong>{nombre}</strong></td>
                            </tr>
                            <tr>
                                <td class="info-label">✉️ Correo Electrónico:</td>
                                <td class="info-value"><a href="mailto:{email}" style="color: #2563eb; text-decoration: none; font-weight: 600;">{email}</a></td>
                            </tr>
                            <tr>
                                <td class="info-label">📦 Servicio de Interés:</td>
                                <td class="info-value"><span class="service-badge">{servicio}</span></td>
                            </tr>
                        </table>

                        <div class="message-box">
                            <div class="message-label">💬 Contenido del Mensaje:</div>
                            <p class="message-text">"{mensaje}"</p>
                        </div>

                        <div style="text-align: center; margin-top: 25px;">
                            <a href="mailto:{email}?subject=Re:%20Solicitud%20de%20Presupuesto%20-%20Julio.dev" class="btn-reply">
                                ✉️ Responder al Cliente
                            </a>
                        </div>
                    </div>
                    <div class="footer">
                        🟢 Notificación del Sistema <strong>Julio.dev</strong> &bull; Gestión Inteligente de Logística
                    </div>
                </div>
            </body>
            </html>
            """

            # 3. Configuración y envío del mensaje usando los ajustes globales
            from_email = getattr(settings, 'EMAIL_HOST_USER', 'julio.rivera.1596@gmail.com')
            to_email = getattr(settings, 'EMAIL_HOST_USER', 'julio.rivera.1596@gmail.com')

            enviar_mensaje = EmailMessage(
                subject=f"📦 Nuevo Lead: {nombre} - {servicio}",
                body=html_message,
                from_email=from_email,
                to=[to_email],
                reply_to=[email]
            )
            enviar_mensaje.content_subtype = "html"

            try:
                enviar_mensaje.send(fail_silently=False)
                return redirect("/contactos/?valido")
            except Exception as e:
                print(f"[ERROR SMTP GMAIL] No se pudo autenticar o enviar correo: {e}")
                return redirect("/contactos/?failNoEnviado")
        else:
            print("Errores en formulario de contacto:", formulario.errors)

    return render(request, "contactos/contacto.html", {'miformulario': formulario})