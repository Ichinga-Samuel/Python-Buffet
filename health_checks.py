#!/usr/bin/env/ python3

import shutil
import psutil


def cpu_check():
    return psutil.cpu_percent(1) < 75


def diskusage():
    du = shutil.disk_usage('/')
    return ((du.free / du.total) * 100) > 75


if not diskusage() or not cpu_check():
    print('Error')
else:
    print('Everything is Fine')
