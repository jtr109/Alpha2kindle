# -*- coding: utf-8 -*-

import configparser


def parse_config(key):
    config = configparser.ConfigParser()
    build_config = 'build.ini'
    config.read(build_config)
    return config[key]  # raise error if the key not exist in config file
