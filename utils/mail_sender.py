# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

from utils import parse_config


class MailSender(object):

    def __init__(self):
        mail_sender = parse_config('mail_sender')
        self.from_addr = mail_sender['username']
        self.password = mail_sender['pwd']
        self.smtp_server = mail_sender['smtp_server']
        self.ssl_port = mail_sender['ssl_port']

    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send_mail(self):
        to_addr = input('To: ')

        msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
        msg['From'] = self._format_addr('Python爱好者 <%s>' % self.from_addr)
        msg['To'] = self._format_addr('管理员 <%s>' % to_addr)
        msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

        server = smtplib.SMTP_SSL(self.smtp_server, self.ssl_port)
        server.set_debuglevel(1)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [to_addr], msg.as_string())
        server.quit()


if __name__ == '__main__':
    mail_sender = MailSender()
    mail_sender.send_mail()
