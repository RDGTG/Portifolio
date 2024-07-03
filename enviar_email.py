# Importe o módulo `cgi` para processar os dados do formulário
import cgi
import smtplib
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, corpo):
    remetente = ''
    senha = ''

    msg = MIMEText(corpo)
    msg['Subject'] = assunto
    msg['From'] = remetente
    msg['To'] = destinatario

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(remetente, senha)
            server.sendmail(remetente, destinatario, msg.as_string())
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")

# Processamento dos dados do formulário
form = cgi.FieldStorage()
nome = form.getvalue('nome')
email = form.getvalue('email')
assunto = form.getvalue('assunto')
mensagem = form.getvalue('mensagem')

# Exemplo de uso:
destinatario = 'Trodrigo350@gmail.com'
enviar_email(destinatario, assunto, mensagem)
