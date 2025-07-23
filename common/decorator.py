import os
import time

import allure
import requests

from functools import wraps

import wda

import readConfig
from common.log import Log
from pageObject.base import Base
from PIL import Image


log = Log()


def _screenshot(name=''):
    if name:
        date_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screenshot_name = name + '-' + date_time + '.PNG'
        path = os.path.join(Base().get_path(), screenshot_name)
    else:
        temp_path = os.path.join(Base().get_path(), 'temp')
        if not os.path.exists(temp_path):
            os.mkdir(temp_path)
        screenshot_name = str(round(time.time() * 1000)) + '.PNG'
        path = os.path.join(temp_path, screenshot_name)

    driver = Base().get_driver()
    driver.screenshot(path)

    # 压缩图片大小，长宽到原本的0.3，iOS大概只有原本十分之一大小，Android大约二分之一
    img = Image.open(path)
    w, h = img.size
    img_resize = img.resize((int(w * 0.3), int(h * 0.3)))
    img_resize.save(path)

    return path

def step(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'@@@ 进入装饰器')
        try:
            log.i('--> %s' % func.__qualname__)
            print(f'@@@ 进入装饰器-try--> %s' % func.__qualname__)
            res = func(*args, **kwargs)
        except requests.ConnectionError:
            print("ConnectionError")
            reset_driver(args[0])
            res = func(*args, **kwargs)
        except Exception as e:
            log.e('\t<-- %s, %s, %s', func.__qualname__, 'Exception', e)
            raise
        finally:
            time.sleep(1)
            add_attach(func.__qualname__)
            _screenshot()
        return res

    return wrapper

    # def step(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             log.i('--> %s' % func.__qualname__)
#             return func(*args, **kwargs)
#         except requests.ConnectionError:
#             print("ConnectionError")
#             reset_driver(args[0])
#             func(*args, **kwargs)
#         except Exception as e:
#             log.e('\t<-- %s, %s, %s', func.__qualname__, 'Exception', e)
#             raise Exception(e)
#         finally:
#             time.sleep(1)
#             add_attach(func.__qualname__)
#             _screenshot()  # 截图

    return wrapper

def case(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.d('\n--> %s', func.__qualname__)
            ret = func(*args, **kwargs)
            log.d('<-- %s, %s', func.__qualname__, 'Success')
            return ret
        except wda.WDAElementNotFoundError:
            print("WDAElementNotFoundError")
            log.d('\n--> %s', func.__qualname__)
            ret = func(*args, **kwargs)
            log.d('<-- %s, %s', func.__qualname__, 'Success')
            return ret
        except Exception as e:
            log.e('<-- %s, %s, %s\n', func.__qualname__, 'Exception', e)
            raise Exception(e)
        # finally:
        #     gif_name = _create_gif() import subprocess
        #
        # import pytest
        #
        # from common.devices import Device
        #
        #
        # def case_to_run(device: Device):
        #     temp_allure_path = device.get_tmp_path()
        #     html_report_path = device.get_path() + '/html'
        #
        #     # 2022/08/10 整体运行完毕后，失败的case一起重新跑一遍
        #     # 下面3个命令，第一个手动标记运行case，第二个执行核心case，第三个执行全部case且优先执行上一次失败的
        #     # args = ['-m', 'vic', '-W', 'ignore::DeprecationWarning', '-v', '-s', '--alluredir', temp_allure_path]
        #     args = ['-m', 'all', '-W', 'ignore::DeprecationWarning', '-v', '-s', '--alluredir', temp_allure_path]
        #     # args = ['-m', 'core', '-W', 'ignore::DeprecationWarning', '-v', '-s', '--alluredir', temp_allure_path]
        #     # args = ['--lf', '--reruns', '1', '-W', 'ignore::DeprecationWarning', '-v', '-s', '--alluredir', temp_allure_path]
        #     exit_code = pytest.main(args).name
        #
        #     # 生成html
        #     cmd = f'allure generate "{temp_allure_path}" -o "{html_report_path}" --clean'
        #     subprocess.Popen(cmd, shell=True).communicate()
        #     return exit_code
        #
        # # if __name__ == '__main__': # 生成gif 并删除tmp文件夹
        #     if gif_name:
        #         with open(gif_name, mode='rb') as f:
        #             file = f.read()
        #         allure.attach(file, "case.gif", attachment_type=allure.attachment_type.GIF)

    return wrapper


def reset_driver(device):
    base_page = Base()
    base_page.set_driver(device)
    base_page.start_app(readConfig.ReadConfig().get_pkg_name())

def add_attach(name=''):
    file_path = _screenshot(name)
    file_name = os.path.basename(file_path)
    with open(file_path, mode='rb') as f:
        file = f.read()
    allure.attach(file, file_name, attachment_type=allure.attachment_type.PNG)
    os.remove(file_path)
