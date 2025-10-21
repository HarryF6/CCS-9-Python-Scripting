import smtplib
from email.mime.text import MIMEText

remitente = "gonfa1999@gmail.com"
destinatario = "gonfa1999@gmail.com"
mensaje = MIMEText("Hola, este es un correo enviado desde Python usando Gmail y una contraseña de aplicación.")
mensaje["Subject"] = "Prueba Python Gmail"
mensaje["From"] = remitente
mensaje["To"] = destinatario

# Conexión segura con Gmail
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(remitente, "rszyteyeshnojuxr")
    smtp.send_message(mensaje)

print("✅ Correo enviado correctamente.")
