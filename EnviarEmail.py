import smtplib
# Biblioteca SMTP para envio de e-mails

from email.mime.multipart import MIMEMultipart
#
from email.mime.text import MIMEText
#


#Programa
# SMTP - Protocolo de envio de e-mail
#dados iniciais
destinatario = str(input("Qual endereço de envio:"))
mensagem = str(input("Digite a mensagem que deseja enviar:"))


# 1 - Iniciar o servidor SMTP
host = "smtp.gmail.com"
porta = "587"
login = "emaildeexemplo.python@gmail.com"
senha = "123@#$345"

servidor = smtplib.SMTP(host,porta)

servidor.ehlo()
servidor.starttls()

servidor.login(login,senha)

# 2 - Contruir a mensagem do tipo MIME


email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = destinatario
email_msg['Subject'] = "Meu e-mail enviado"
email_msg.attach(MIMEText(mensagem,'plain'))
# email_msg.attach(MIMEText(mensagem,'html'))



# 3 - Enviar o e-mail
servidor.sendmail(email_msg['From'],email_msg['To'], email_msg.as_string())
servidor.quit()
print(f'E-mail enviado com sucesso para {destinatario}')
