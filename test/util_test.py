# -*- coding: utf-8 -*-

import unittest
import os

from utils.web_parser import PageHandler


class TestWebParser(unittest.TestCase):

    def clean_tmp_dir(self, path):
        os.remove(path)
        os.removedirs(os.path.dirname(path))

    def test_save_file_without_dir(self):
        filename = 'test.txt'
        dirname = 'tmp'
        path = os.path.join(os.path.abspath('.'), dirname, filename)
        if os.path.exists(path):
            os.remove(path)
        if os.path.exists(os.path.dirname(path)):
            os.removedirs(os.path.dirname(path))
        test_ph = PageHandler()
        text = 'test save file without dir'
        test_ph._save_file(path, text)
        self.assertTrue(os.path.exists(path))
        self.clean_tmp_dir(path)

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
        self.clean_tmp_dir(path)

    def test_save_file_with_file_exists(self):
        filename = 'test.txt'
        dirname = 'tmp'
        path = os.path.join(os.path.abspath('.'), dirname, filename)
        if not os.path.exists(path):
            os.mknod(path)
        if not os.path.exists(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))
        test_ph = PageHandler()
        text = 'test save file with file exists'
        test_ph._save_file(path, text)
        self.assertTrue(os.path.exists(path))
        self.clean_tmp_dir(path)

