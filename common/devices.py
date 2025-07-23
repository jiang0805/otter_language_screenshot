import os
import re
import wda
import subprocess
import uiautomator2 as u2
import json


def get_android_device_list() -> list:
    """
    先尝试从adb获取设备信息
    如果有异常则返回[]（空）
    如果返回了[]则尝试从U2的connect_usb()方法获取信息
    return:
        [{
            "os": "android",
            "serial": "",
            "name": "",
        },...]
    """
    devices = get_device_info_from_adb()
    if not devices:
        devices = get_device_info_from_u2()
    return devices


def get_ios_device_list() -> list:
    devices = get_device_info_from_tidevice()
    if not devices:
        devices = get_device_info_from_wda()
    return devices

def get_device_info_from_adb() -> list:
    result = []
    try:
        output = subprocess.check_output("adb devices -l", shell=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"ADB command failed with error: {e.returncode}")
        return result

    device_list = [line for line in output.split('\n') if line and not line.lower().startswith('list of devices')]

    for info_str in device_list:
        match = re.match(r'(\S+)\s.*model:(\S+)', info_str)
        if match:
            serial, name = match.groups()
            device = {
                "os": "android",
                "serial": serial,
                "name": name,
            }
            result.append(device)
        else:
            print(f"Failed to parse device info from string: {info_str}")

    return result


def get_device_info_from_u2() -> list:
    try:
        device_info = u2.connect_usb().device_info
        device = {
            "os": "android",
            "serial": device_info["serial"],
            "name": device_info["model"],
        }
    except Exception as e:
        print(f"exception from u2: {e}")
        return []
    return [device]


def get_device_info_from_tidevice() -> list:
    result = []
    try:
        cmd = ['tidevice', 'list', '--json']
        terminal_output = subprocess.check_output(cmd)
        device_info_list = json.loads(terminal_output)
        # 过滤掉'conn_type': 'Network'的设备
        if device_info_list:
            device_filter = filter(lambda x: x['conn_type'] != 'network', device_info_list)
            for info in list(device_filter):
                result.append({
                    "os": "ios",
                    "serial": info['udid'],
                    "name": info['name'],
                })
    except:
        print("exception from tidevice")
        return []
    return result


def get_device_info_from_wda() -> list:
    result = []
    try:
        device_info = wda.USBClient().device_info()
        result.append({
            "os": "ios",
            "serial": device_info['uuid'],
            "name": device_info['name'],
        })
    except:
        print("exception from wda")
        return []
    return result

class Device:
    def __init__(self, os: str, name: str, serial: str):
        self.os = os
        self.name = name
        self.serial = serial

    def get_path(self):
        test_report_path = os.path.join(os.getcwd(), 'TestReport' + os.sep + self.name)
        if not os.path.exists(test_report_path):
            os.makedirs(test_report_path)
        return test_report_path

    def get_tmp_path(self):
        tem_path = os.path.join(os.getcwd(), 'temp' + os.sep + self.name)
        if not os.path.exists(tem_path):
            os.makedirs(tem_path)
        return tem_path


def get_device_list() -> [Device]:
    """
    返回设备列表，列表中是一组Device实例
    """
    result = []
    android_devices = get_android_device_list()
    ios_devices = get_ios_device_list()
    devices = android_devices + ios_devices
    if not devices:
        return []

    for device_info in devices:
        device = Device(os=device_info['os'], name=device_info['name'], serial=device_info['serial'])
        result.append(device)
    return result
