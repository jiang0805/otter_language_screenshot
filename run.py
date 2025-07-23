# -*- coding:utf-8 -*-
# !/usr/bin/python
# run.py
# Created by Vic on 2019-10-11
# Python: 3.7.2
import shutil
import time
from multiprocessing import Pool

import readConfig
from readConfig import *
from common.devices import Device, get_device_list
from common.log import Log
from common.pytest_cmd import case_to_run
from common.utils.report import create_statistics_report, backup_report
from pageObject.base import Base


def init_logger(device: Device):
    log = Log()
    log.set_logger(device.name, os.path.join(device.get_path(), 'client.log'))
    log.i(f'name: {device.name}')


def init_base(device: Device):
    base_page = Base()
    base_page.set_path(device.get_path())
    base_page.set_driver(device)
    base_page.start_app(readConfig.ReadConfig().get_pkg_name())


def create_report(device_list: [Device]):
    create_statistics_report(device_list)
    start_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
    backup_report('./TestReport', './TestReport_History', start_time)
    if os.path.exists(os.path.join(os.getcwd(), 'temp')):
        shutil.rmtree(os.path.join(os.getcwd(), 'temp'))
    # upload_zip_file('./TestReport_History/' + 'Report_' + start_time, './TestReport_History', start_time + ".zip")


def _run_each(device: Device):
    init_logger(device)
    init_base(device)
    return case_to_run(device)


def run(device_list: [Device]):
    with Pool(processes=len(device_list)) as pool:
        for each in device_list:
            pool.apply_async(_run_each, args=(each,))
        pool.close()
        pool.join()

    create_report(device_list)


def set_up_devices() -> list:
    return get_device_list()


if __name__ == '__main__':
    devices = set_up_devices()
    if devices:
        run(devices)
    else:
        print("无设备可以运行")
