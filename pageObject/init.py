from common.decorator import *

from readConfig import ReadConfig

pkg_name = ReadConfig().get_pkg_name()

class Init(Base):
    @step
    def activate_app(self):
        # log.i("启动App")
        self.s.app_start(pkg_name)

    @step
    def terminate_app(self):
        log.i("关闭App")
        self.s.app_stop(pkg_name)

    @step
    def page_back(self):
        log.i('返回上一页')
        if self.is_ios():
            if self.s(nameContains='返回', className='Button').exists:
                self.s(nameContains='返回', className='Button').click()
            else:
                self.s.swipe_right()
        else:
            self.s.press('back')


page = Init()

def launch_app():
    page.activate_app()


def close_app():
    page.terminate_app()