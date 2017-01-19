# -*- coding: utf-8 -*-

import os
import configparser



if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('build.ini')
    mail_sender = config['mail_sender']
    print(mail_sender['username'])
