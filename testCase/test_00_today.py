import pytest
from pageObject import init, today, tab4, task, acticity
from common.decorator import *


@pytest.mark.all
@allure.feature('today')
class TestLogin(Base):
    @classmethod
    def setup_method(self,cls):
        init.launch_app()
        log.i('启动App')  # 将App登录状态处理成未登录的状态

    @classmethod
    def teardown_class(cls):
        log.i('运行完case后关闭App')
        init.close_app()

    @allure.description("检查登录页面")
    @case
    def test_01_check_today(cls):
        today.today()
        acticity.activity()
        task.task()
        tab4.tab4()
        tab4.chinese()
        init.launch_app()
        today.today()
        acticity.activity()
        task.task()
        tab4.tab4()
        tab4.korean()
        init.launch_app()
        today.today()
        acticity.activity()
        task.task()
        tab4.tab4()
        tab4.spanish()
        init.launch_app()
        today.today()
        acticity.activity()
        task.task()
        tab4.tab4()
        tab4.japanese()



        #调试代码
        tab4.tttt()
        init.launch_app()
        today.today()


    @allure.description("检查登录页面")
    def test_dummy(self):
        print("test dummy executed")


