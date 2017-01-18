# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
# import kindlestrip
import os
from celery import Celery

from utils.config import CURCONF
from utils.timer import exe_time


celery_app = Celery('web_parser', broker=CURCONF.REDIS_URL)


class PageHandler(object):
    def __init__(self):
        self.headers = CURCONF.HEADERS

    @exe_time
    def run(self, url):
        text_info = self._parse_html(url)  # parsed html
        if text_info is not None:
            self._gen_file(text_info)
        else:
            pass

    def _parse_html(self, url):
        payload = {'url': url}
        r = requests.get("https://www.instaparser.com/preview",
                         params=payload, headers=self.headers)
        doctype = "<!DOCTYPE HTML>"
        if r.status_code == 200 and doctype in r.text:
            ret = dict(extension='html', text=r.text)
            return ret
        else:  # todo: add a checker to alert if not 200
            return None

    def _gen_file(self, text_info):
        uid = 1  # todo: generate uuid or title as filename
        tmp_dir = os.path.join(os.path.abspath('..'), 'tmp')
        filename = str(uid) + '.' + text_info.get('extension')
        path = os.path.join(tmp_dir, filename)
        print("Save path: %s" % path)
        self._save_file(path, text_info.get('text'))

    def _save_file(self, path, text):
        try:
            f = open(path, 'w', encoding='utf-8')
        except FileNotFoundError as e:
            # print("No such dir, creating.")
            file_dir = os.path.dirname(path)
            os.mkdir(file_dir)
            f = open(path, 'w', encoding='utf-8')
        finally:
            f.write(text)
            f.close()


if __name__ == '__main__':

    url = "http://blog.instapaper.com/post/137288701461"
    ph = PageHandler()
    ph.run(url)

