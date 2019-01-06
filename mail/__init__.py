import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .format import *

today = datetime.now()
yesterday = today - timedelta(1)

with open('config.json', 'r') as f:
    config = json.load(f)


def send(target, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(config['MAIL']['USERNAME'], config['MAIL']['PASSWORD'])

    server.sendmail(config['MAIL']['NAME'], target, msg)
    server.quit()


def prepare_mail(target, size, lg='en'):
    subject = 'SmlepNews on ' + today.strftime("%Y-%m-%d")

    msg = MIMEMultipart()
    msg['From'] = config['MAIL']['USERNAME']
    msg['To'] = target
    msg['Subject'] = subject
    msg['Charset'] = 'UTF-8'
    msg['Content-Type'] = 'text/plain; charset=UTF-8'

    body = ""
    body += format_weather(lg)
    body += '<br>'
    body += format_ph(size, lg)
    body += '<br>'
    body += format_gh(size, lg)
    body += '<br>'
    if lg == 'en':
        body += format_guardian(size)
    if lg == 'fr':
        body += format_figaro(size)

    msg.attach(MIMEText(body, 'html', 'utf-8'))

    send(target, msg.as_string())
