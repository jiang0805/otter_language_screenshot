import subprocess

import pytest

from common.devices import Device


def case_to_run(device: Device):
    temp_allure_path = device.get_tmp_path()
    html_report_path = device.get_path() + '/html'

    # 2022/08/10 整体运行完毕后，失败的case一起重新跑一遍
    # 下面3个命令，第一个手动标记运行case，第二个执行核心case，第三个执行全部case且优先执行上一次失败的
    # args = ['-m', 'vic', '-W', 'ignore::DeprecationWarning', '-v', '-s', '--alluredir', temp_allure_path]
    args = ['-m', 'all', '-W', 'ignore::DeprecationWarning', '-v', '-s', '--alluredir', temp_allure_path]
    # args = ['-m', 'core', '-W', 'ignore::DeprecationWarning', '-v', '-s', '--alluredir', temp_allure_path]
    # args = ['--lf', '--reruns', '1', '-W', 'ignore::DeprecationWarning', '-v', '-s', '--alluredir', temp_allure_path]
    # exit_code = pytest.main(args).name
    exit_code = pytest.main(args)

    # 生成html
    cmd = f'allure generate "{temp_allure_path}" -o "{html_report_path}" --clean'
    subprocess.Popen(cmd, shell=True).communicate()
    return exit_code

# if __name__ == '__main__':
