#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import platform


def SystemSpe():
    plat = platform.platform()
    if plat.startswith("Windows"):
        return "\\"
    return "/"
