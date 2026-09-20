import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import pyautogui
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

try:
    print("Aguarde.. seu e-mail está sendo enviado!")
    #confugurações do servidor de e-mail
    servidor_email = smtplib.SMTP ('smtp.gmail.com', 587)
    servidor_email.starttls ()
    #servidor_email.login ('seu email', 'sua senha de app')
    servidor_email.login ('ramongegomesfranca@gmail.com', 'senha do app')

    #montar o email
    remetente = 'ramongegomesfranca@gmail.com'
    destinatarios = ['email dos destinatarios']
    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = ', '.join(destinatarios)
    mensagem['Subject'] = 'Teste de envio de e-mail com Python'

    corpo_email = 'Olá, este é um teste de envio de e-mail com Python.'
    mensagem.attach(MIMEText(corpo_email, 'plain'))

    #envio
    servidor_email.sendmail (remetente, destinatarios, mensagem.as_string())

    print("E-mail enviado com sucesso!")

except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")