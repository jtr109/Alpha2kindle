# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
import os

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

    @staticmethod
    def _file_info(path):
        if os.path.exists(path):
            filename = os.path.split(path)[1]
            name, extension = os.path.splitext(filename)
            if extension[0] == '.':
                extension = extension[1:]
            filetype = {
                'text': ['txt', 'html'],
                'image': ['jpeg', 'jpg', 'png'],
            }
            if extension in filetype['text']:
                return {'_maintype': 'text', '_subtype': extension,
                        'filename': filename}
            elif extension in filetype['image']:
                return {'_maintype': 'image', '_subtype': extension,
                        'filename': filename}
            else:
                return None
        else:
            return None

    def send_mail(self, to_addr, attachment_path):
        msg = MIMEMultipart()
        msg['From'] = self._format_addr('Alpha2kindle <%s>' % self.from_addr)
        msg['To'] = self._format_addr('管理员 <%s>' % to_addr)
        msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

        msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
        with open(attachment_path, 'r', encoding='utf-8') as f:
            # todo: set defence for wrong path
            info = self._file_info(attachment_path)
            if info:
                mime = MIMEBase(info['_maintype'], info['_subtype'],
                                filename=info['filename'])
                # 加上必要的头信息:
                mime.add_header('Content-Disposition', 'attachment',
                                filename=info['filename'])
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                # 把附件的内容读进来:
                mime.set_payload(f.read())
                # 用Base64编码:
                encoders.encode_base64(mime)
                # 添加到MIMEMultipart:
                msg.attach(mime)

        server = smtplib.SMTP_SSL(self.smtp_server, self.ssl_port)
        server.set_debuglevel(1)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [to_addr], msg.as_string())
        server.quit()


if __name__ == '__main__':
    mail_sender = MailSender()
    to_addr = 'jtr_server@foxmail.com'
    tmp_dir = os.path.join(os.path.abspath('..'), 'tmp')
    filename = '1.html'
    path = os.path.join(tmp_dir, filename)
    mail_sender.send_mail(to_addr, path)
