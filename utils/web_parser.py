# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
# import kindlestrip
import os

from utils.config import BaseConf
from utils.config import handle_main
from utils.timer import exe_time


class PageHandler(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/55.0.2883.95 "
                          "Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;"
                      "q=0.9,image/webp,*/*;"
                      "q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
            # "Cache-Control": "max-age=0",
        }

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
    path = './test.html'
    ph = PageHandler()
    ph.run(url)

