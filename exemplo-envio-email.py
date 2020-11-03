#importacoes
# coding: utf-8
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib

'''objeto necessario para prototipar
as conf iniciais da mensagem'''
msg = MIMEMultipart()

'''conteudo da mensagem'''
message = "Deu certo "

'''senha do email remetente'''
password = <"senhaacesso">
'''rementente'''
msg['From'] = <"fulandodetal@gmail.com">
'''destinatario'''
msg['To'] = <"fulandodetal2@gmail.com">
'''titulo da mensagem'''
msg['Subject'] = "test"

#carregando a imagem na mensagem
with open("house", 'rb') as fp:
    img = MIMEImage(fp.read())
    fp.close()
msg.attach(img)



'''carrega o corpo da mensagem no prototipo de mensagem'''
msg.attach(MIMEText(message,_subtype='plain'))

'''Servidor SMTP Hotmail'''
#server = smtplib.SMTP('smtp.live.com: 25')

'''Permite que você envie mensagens apenas para usuários do Gmail ou do G Suite. Esta opção não exige autenticação.'''
#server = smtplib.SMTP('aspmx.l.google.com: 25')

'''Você pode enviar e-mails para qualquer pessoa dentro ou fora da sua organização.
Esta opção exige que você faça a autenticação com a conta e a senha do Gmail ou do G Suite. '''
server = smtplib.SMTP(host='smtp.gmail.com', port = 587)


#da start no tls que eh pre-requisito (gmail)
server.starttls()

server.login(msg['From'], password)

'''envia o email'''
#server.sendmail(msg['From'],msg['To'],msg.as_string())

#fecha conexao com servidor SMTP
server.quit()

#print("successfully sent email to %s:" % (msg['To']))

import sys
sys.stdin
