#Enviando e-mail com Python
# Alysson Milet
# github.com/alyssonmilet

#Bibliotecas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#Aplicativo

try: 
    destinatario = str(input("Qual endereço de envio:"))
    mensagem = str(input("Digite a mensagem que deseja enviar:"))

    host = "smtp.gmail.com"
    porta = "587"
    login = "emaildeexemplo.python@gmail.com"
    senha = "123@#$345
    
    servidor = smtplib.SMTP(host,porta)

    servidor.ehlo()
    servidor.starttls()

    servidor.login(login,senha)

    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = destinatario
    email_msg['Subject'] = "Meu e-mail enviado"
    email_msg.attach(MIMEText(mensagem,'plain'))
    # email_msg.attach(MIMEText(mensagem,'html'))

    servidor.sendmail(email_msg['From'],email_msg['To'], email_msg.as_string())
        
    servidor.quit()
    print(f'E-mail enviado com sucesso para {destinatario}')

except smtplib.SMTPException:
    print("Erro ao enviar e-mail")
