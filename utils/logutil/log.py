#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:JiuZha
# datetime:2019/3/10 17:12

import os
import sys
import time
import logging
from logging import StreamHandler
from logging.handlers import RotatingFileHandler

# import env
# import exception
# import paramparser

version = "1.0.1"

LOG_LEVEL_DEBUG = "DEBUG"
LOG_LEVEL_INFO = "INFO"

LOG_NAME_CLIENT = "client"
LOG_NAME_SERVER = "server"

client_logger = None
server_logger = None

def _build_logger(usr_name,log_name,log_file,log_level,fmt,maxb_ytes = 20 * 1024,backup_count = 20):
    log_dir = usr_name + "logs" + os.sep
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    if not os.path.isdir(log_dir):
        pass
        # raise exception.DirError("dir:{} not found.".format(log_dir))
    log_path =os.path.join(log_dir,log_name)

    tmp_logger = logging.getLogger(log_name)
    tmp_logger.propagate = False
    if log_level ==LOG_LEVEL_DEBUG:
        tmp_logger.setLevel(logging.DEBUG)
    else:
        tmp_logger.setLevel(logging.INFO)
    # if paramparser.cmdparam.console and log_name == LOG_NAME_CLIENT:
    #     console_handler = StreamHandler(sys.stdout)
    #     console_handler.setFormatter(logging.Formatter(fmt))
    #     tmp_logger.addHandler(console_handler)
    file_handler =RotatingFileHandler(log_path,maxBytes=maxb_ytes,backupCount=backup_count)
    file_handler.setFormatter(logging.Formatter(fmt))
    tmp_logger.addHandler(file_handler)
    return tmp_logger

def init_log(name):
    global client_logger
    global server_logger
    fmt = '[%(asctime)s] %(levelname)s sign:' +' lineno:%(lineno)d : %(message)s'
    if name == LOG_NAME_CLIENT:
        client_logger = _build_logger(env.usr_home, "client", "dfclient.log", LOG_LEVEL_INFO, fmt)
    elif name == LOG_NAME_SERVER:
        server_logger = _build_logger(env.usr_home, "server", "dfserver.log", LOG_LEVEL_INFO, fmt)
