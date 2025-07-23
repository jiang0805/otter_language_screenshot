# -*- coding:utf-8 -*-
# !/usr/bin/python
# report.py
# Created by Vic on 2019-10-11
# Python: 3.7.2


import datetime
import json
import os
import shutil
import zipfile

import requests
from jinja2 import Environment, FileSystemLoader

from common.devices import Device

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, )),
    trim_blocks=False)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html(path_list):
    """
    以common/index.html 为模板生成 index.html
    :param path_list:
    :return:
    """
    name = "./TestReport/index.html"
    urls = path_list
    context = {
        'urls': urls
    }
    with open(name, 'w', encoding="utf-8") as f:
        html = render_template('index.html', context)
        f.write(html)


def _get_report_info(device: Device):
    """
    获取每个设备的测试报告内容参数
    :param device:
    :return:
    """
    report = os.path.join(device.get_path(), "html/data/behaviors.csv")
    time_data = os.path.join(device.get_path(), "html/data/behaviors.json")
    behaviors_list = []
    result = {}

    with open(report, 'r', encoding='utf-8') as fb:
        for value in fb.readlines():
            data = value.replace("\"", '').replace("\n", '')
            behaviors_list.append([i for i in data.split(',')])

    with open(time_data, 'r', encoding='utf-8') as fb:
        time_list = json.load(fb)['children']

    if len(time_list) == 1:
        duration = time_list[0]['children'][0]['time']['duration']
        result['duration'] = datetime.timedelta(seconds=duration // 1000)
    elif time_list:
        duration = 0
        for case_time in time_list:
            if case_time:
                for time in case_time['children']:
                    duration = duration + time['time']['duration']
        result['duration'] = datetime.timedelta(seconds=duration // 1000)

    if behaviors_list:
        total = 0
        win = 0
        failed = 0
        error = 0
        skipped = 0
        unknown = 0

        for index in range(1, len(behaviors_list)):
            behaviors_list[index].reverse()
            for ele in range(0, 5):
                if behaviors_list[index][ele]:
                    total = total + int(behaviors_list[index][ele])
            win = win + int(behaviors_list[index][2])
            failed = failed + int(behaviors_list[index][4])
            error = error + int(behaviors_list[index][3])
            skipped = skipped + int(behaviors_list[index][1])
            unknown = unknown + int(behaviors_list[index][0])

        result["sum"] = total
        result["pass"] = win
        result["failed"] = failed
        result["error"] = error
        result["skipped"] = skipped
        result["unknown"] = unknown
        result["passrate"] = '{:.2f}%'.format(win / total * 100)
    return result


def create_statistics_report(devices: [Device]):
    """
    根据运行设备的数量 将所有设备的报告在一个HTML中展示
    路径为：./TestReport/index.html
    :param devices:
    :return:
    """
    report_path_list = []
    for device in devices:
        if not os.path.isfile(os.path.join(device.get_path(), 'html/index.html')):
            return
        tmp_dic = {'urls': os.path.split(device.get_path())[1] + "/html/index.html",
                   'name': device.name + " 自动化测试报告"}
        tmp_dic.update(_get_report_info(device))
        report_path_list.append(tmp_dic)
    create_index_html(report_path_list)


def backup_report(report_path, backup_path, time):
    """
    备份报告到 TestReport_History 文件夹
    :param report_path:
    :param backup_path:
    :param time:
    :return:
    """
    if not os.path.exists(backup_path):
        os.mkdir(backup_path)
    if not os.path.exists(report_path):
        pass
    else:
        try:
            shutil.move(report_path, os.path.join(backup_path, 'Report_' + time))
        except PermissionError as e:
            raise e
        print('备份TestReport成功')


def _get_zip_file(input_path, file_lists):
    """
    对目录进行深度优先遍历
    :param input_path:
    :param file_lists:
    :return:
    """
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path + '/' + file):
            _get_zip_file(input_path + '/' + file, file_lists)
        else:
            file_lists.append(input_path + '/' + file)


def upload_zip_file(input_path, output_path, output_name):
    """
    压缩文件
    :param input_path: 压缩的文件夹路径
    :param output_path: 解压（输出）的路径
    :param output_name: 压缩包名称
    :return:
    """
    f = zipfile.ZipFile(output_path + '/' + output_name, 'w', zipfile.ZIP_DEFLATED)
    file_lists = []
    _get_zip_file(input_path, file_lists)
    for file in file_lists:
        f.write(file)
    # 调用了close方法才会保证完成压缩
    f.close()

    # 上传zip文件到pikachu
    try:
        url = "https://pikachu.midway.run/ui/upload-data/"
        files = {'test_data_files': open('TestReport_History/' + output_name, 'rb')}
        payload = {'Product': '1'}
        result = requests.request("POST", url, data=payload, files=files)

        print(result.status_code)
        print(result.content)
    except requests.exceptions.SSLError as e:
        print(e)

    return output_path + r"/" + output_name
