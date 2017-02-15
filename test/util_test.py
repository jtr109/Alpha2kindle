# -*- coding: utf-8 -*-

import unittest
import os

from utils.web_parser import PageHandler
from utils.mail_sender import MailSender


class TestWebParser(unittest.TestCase):

    @staticmethod
    def _create_temp_file(path):
        if not os.path.exists(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))
        if not os.path.exists(path):
            open(path, 'a')
            # os.mknod(path)

    @staticmethod
    def _remove_temp_dir(path):
        if os.path.exists(path):
            os.remove(path)
        if os.path.exists(os.path.dirname(path)):
            os.removedirs(os.path.dirname(path))

    def test_save_file_without_dir(self):
        filename = 'test.txt'
        dirname = 'tmp'
        path = os.path.join(os.path.abspath('.'), dirname, filename)
        self._remove_temp_dir(path)
        test_ph = PageHandler()
        text = 'test save file without dir'
        test_ph._save_file(path, text)
        self.assertTrue(os.path.exists(path))
        self._remove_temp_dir(path)

    def test_save_file_without_file(self):
        filename = 'test.txt'
        dirname = 'tmp'
        path = os.path.join(os.path.abspath('.'), dirname, filename)
        if os.path.exists(path):
            os.remove(path)
        if not os.path.exists(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))
        test_ph = PageHandler()
        text = 'test save file without file'
        test_ph._save_file(path, text)
        self.assertTrue(os.path.exists(path))
        self._remove_temp_dir(path)

    def test_save_file_with_file_exists(self):
        filename = 'test.txt'
        dirname = 'tmp'
        path = os.path.join(os.path.abspath('.'), dirname, filename)
        self._create_temp_file(path)
        test_ph = PageHandler()
        text = 'test save file with file exists'
        test_ph._save_file(path, text)
        self.assertTrue(os.path.exists(path))
        self._remove_temp_dir(path)


class TestMailSender(unittest.TestCase):

    def test_file_info_with_txt(self):
        filename = 'test.txt'
        dirname = 'tmp'
        path = os.path.join(os.path.abspath('.'), dirname, filename)
        TestWebParser._create_temp_file(path)
        ret = {'_maintype': 'text', '_subtype': 'txt', 'filename': filename}
        self.assertEqual(MailSender._file_info(path), ret)
        TestWebParser._remove_temp_dir(path)

    def test_file_info_with_html(self):
        filename = 'test.html'
        dirname = 'tmp'
        path = os.path.join(os.path.abspath('.'), dirname, filename)
        TestWebParser._create_temp_file(path)
        ret = {'_maintype': 'text', '_subtype': 'html', 'filename': filename}
        self.assertEqual(MailSender._file_info(path), ret)
        TestWebParser._remove_temp_dir(path)
