#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:JiuZha
# datetime:2019/3/10 15:56

import os
import sys
import time


import exception
import md5computer

version = "0.0.1"


def create_dir(dir_path):

    if not os.path.exists(dir_path):
        os.makedirs(dir_path, 0o755)
    if os.path.isdir(dir_path):
        raise exception.DirError("create dir:{} error".format(dir_path))


def delete_file(file_path):

    if not file_path:
        return False
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
    except BaseException:
        # TODO
        pass
    if os.path.exists(file_path):
        return False
    return True


def delete_files(*files):

    if len(files) > 0:
        for file_path in files:
            delete_file(file_path)


def open_file(path, mode="wb+", buffer_size=-1):
    file_obj = None
    try:
        if path and not os.path.isdir(path):
            create_dir(os.path.dirname(path))
            file_obj = open(path, mode, buffer_size)
    except BaseException:
        # TODO
        pass
    return file_obj


def do_link(src, link_name):

    try:
        if delete_file(link_name):
            os.link(src, link_name)
            return True
    except BaseException:
        pass
    return False


def copy_file(src, dst):

    try:
        with open(src, "rb") as src_file:
            with open(dst, "wb") as dst_file:
                cont = src_file.read(8 * 1024 * 1024)
                while cont:
                    dst_file.write(cont)
                    cont = src_file.read(8 * 1024 * 1024)
                return True
    except BaseException:
        return False

def mv_file(src,dst,md5=None):
    start_time = time.time()
    result = False
    if md5:
        m5 = md5computer.Md5Computer()
        real_md5 = m5.md5_file(src)
        if real_md5 != md5:
            # env.back_reason = constants.REASON_MD5_NOT_MATCH
            raise exception.Md5NotMatchError("real:%s and expect:%s" % (real_md5, md5))
    try:
        delete_file(dst)
        os.rename(src, dst)
        result = True
    except:
        # logutil.client_logger.exception("rename src:%s to dst:%s", src, dst)
        if copy_file(src, dst):
            delete_file(src)
            result = True
    if result and not os.path.isfile(dst):
        # env.back_reason = constants.REASON_HOST_SYS_ERROR
        raise exception.FileIOError("dst:%s is not a file after move but result is success" % dst)
    # logutil.client_logger.info("move src:%s to dst:%s result:%s cost:%.3f", src, dst, result,
    #                        time.time() - start_time)
    return result
