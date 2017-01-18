# -*- coding: utf-8 -*-


class BaseConf(object):
    HEADERS = {
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


CURCONF = BaseConf
