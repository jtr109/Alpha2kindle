# -*- coding: utf-8 -*-

import requests
# from requests.utils import quote

from utils.timer import exe_time


class PageHandler(object):
    def __init__(self, url):
        self.payload = {'url': url}
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
            "Cache-Control": "max-age=0",
        }

        self.url = url

    @exe_time
    def get_page(self):
        # url = quote(target_url, safe='')
        r = requests.get("https://www.instaparser.com/preview",
                         params=self.payload, headers=self.headers)
        # return r.url
        if r.status_code == 200:
            return True
        else:
            return False


if __name__ == '__main__':

    target_url = "http://blog.instapaper.com/post/137288701461"

    page = PageHandler(target_url)
    print(page.get_page())

