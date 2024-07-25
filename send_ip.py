import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests

# Configurações de e-mail
EMAIL = 'EMAIL_QUE_VAI_ENVIAR_O_IP_PUBLICO'
PASSWORD = 'SENHA_DO_APLICATIVO_GOOGLE'  # Use uma senha de aplicativo se a verificação em duas etapas estiver ativada
TO_EMAIL = 'EMAIL_QUE_VAI_RECEBER_O_IP_PUBLICO'
SUBJECT = 'IP Público'

# Obter o IP público
IP = requests.get('http://ifconfig.me').text

# Configurar a mensagem
msg = MIMEMultipart()
msg['From'] = EMAIL
msg['To'] = TO_EMAIL
msg['Subject'] = SUBJECT

body = f'O IP público é: {IP}'
msg.attach(MIMEText(body, 'plain'))

# Enviar o e-mail
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Iniciar a conexão TLS
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Falha ao enviar o e-mail: {e}")
