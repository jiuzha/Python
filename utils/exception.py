#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:JiuZha
# datetime:2019/3/10 16:12

class ParamError(Exception):
    """
    param is invalid
    """
    def __init__(self,msg=''):
        Exception.__init__(self,msg)

class DownError(Exception):
    """
    down error
    """
    def __init__(self,msg=''):
        Exception.__init__(self,msg)

class DirError(Exception):
    """
    dir create/delete and so on error
    """
    def __init__(self,msg=''):
        Exception.__init__(self,msg)

class FileIOError(Exception):
    """
    file io error
    """
    def __init__(self,msg=''):
        Exception.__init__(self,msg)

class SpaceLackError(Exception):
    """
    disk space is lack
    """
    def __init__(self,msg=''):
        Exception.__init__(self,msg)

class Md5NotMatchError(Exception):
    """
    md5 not match
    """
    def __init__(self,msg=''):
        Exception.__init__(self,msg)


class ReadTimeOutError(Exception):
    """
    read http response timeout
    """
    def __init__(self,msg=''):
        Exception.__init__(self,msg)


class NeedBack(Exception):
    """
    need back source to download
    """

    def __init__(self, msg=''):
        Exception.__init__(self, msg)



