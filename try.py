from common.devices import get_device_list
import wda
# from common.decorator import *
#
#
#
s = wda.USBClient().session()
# s.xpath(
#     '//Table/Cell/StaticText[@name="繁體中文"]').click()
# s.xpath('//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[6]/Image[2]').click()
s.xpath(
    '//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[8]/Image[2]').click()

# s.xpath(
#                 "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[7]/Image[2]").click()
# s.xpath(
#                 "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[13]/Image[2]").click()
# s(textContains="我已阅读并同意《用户协议》").click()
# s.xpath("//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other").click()
# s.tap_hold(0.861, 0.211)   # tap/press 根据你的 wda 版本，tap支持百分比
# s.swipe(0.5, 0.8, 0.5, 0.2)  #上划页面
# s.swipe_down()
# s.swipe_right()
# assert s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
# s.xpath("//ScrollView").click()
# if __name__ == '__main__':
#     # get_ios_device_list()
#     get_device_list()


# import time
# import uiautomator2 as u2
# import wda
# from common.decorator import *
#
# # 模拟你的 Device 结构
# class Device:
#     def __init__(self, name, serial, os):
#         self.name = name
#         self.serial = serial
#         self.os = os
#
# # 精简版 Base 类（去除类变量，全部实例变量）
# class Base:
#     def __init__(self, device):
#         self.device = device
#         self.s = None
#         self.set_driver(device)
#
#     def set_driver(self, device):
#         print(f'[Base] 初始化设备驱动：{device.name}, OS: {device.os}')
#         if device.os == 'ios':
#             # 真机环境请确保连接无误
#             self.s = wda.USBClient().session()
#         else:
#             self.s = u2.connect(device.serial)
#         print(f'[Base] 驱动实例: {self.s}')
#
#     def is_ios(self):
#         return self.device.os.lower() == 'ios'
#
#     def start_app(self, pkg_name):
#         print(f'[Base] 启动应用: {pkg_name}')
#         self.s.app_start(pkg_name)
#         time.sleep(2)  # 等待APP启动
#
#     # 点击示例函数
#     def today_otter_aichat(self):
#         print('[Base] 进入 today_otter_aichat')
#         if self.is_ios():
#             el = self.s.xpath("//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[1]/Other[2]").click()
#             print(f'[Base] 元素是否存在: {el.exists}')
#             if el.exists:
#                 print('[Base] 进行点击操作')
#                 el.click()
#             else:
#                 print('[Base] iOS元素未找到')
#         else:
#             el = self.s(resourceId='app.podcast.cosmos:id/stvTitle')  # Android示例
#             print(f'[Base] 元素是否存在: {el.exists}')
#             if el.exists:
#                 print('[Base] 进行滑动操作')
#                 el.swipe("left")
#             else:
#                 print('[Base] Android元素未找到')
#         print('[Base] today_otter_aichat执行结束')
#
# def main():
#     # 设备示例（请替换成你的设备 Serial 和 OS）
#     device = Device(name='QA的iPhone', serial='00008120-001E311022E0C01E', os='ios')
#     base = Base(device)
#     base.start_app('com.ruguoapp.otterlife')  # 替换成你的包名
#     # @step
#     base.today_otter_aichat()
#     print('测试结束')
#
# if __name__ == '__main__':
#     main()

