import time

import pytest
from common.decorator import *
from pageObject import init


class TodayPage(Base):
    @allure.step('点击today页面中间的海獭')
    @step
    def today_otter_aichat(self):
        print("case start")
        log.i('today->ai对话')
        print(f'当前驱动实例：{self.s}')
        if self.is_ios():
            el = self.s.xpath("//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[1]/Other[2]")
            print(f"元素是否存在：{el.exists}")
            el.click()
        # if self.is_ios():
            # self.s.tap_hold(0.483, 0.365)
            # self.s.xpath("//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[1]/Other[2]").click()
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_aichat_back(self):
        log.i('today->ai对话->返回today')
        print('返回主界面')
        if self.is_ios():
            self.s.xpath("//Button").click()
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_watch_button(self):
        log.i('today->右上角手表按钮')
        if self.is_ios():
            self.s.xpath("//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[1]/Image[1]").click()
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_watch_button_back(self):
        log.i('today->右上角手表按钮->返回')
        if self.is_ios():
            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Image[1]").click()
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_data_button(self):
        log.i('today->右上角日历按钮')
        if self.is_ios():
            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[1]/Image[2]").click()
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_data_button_back(self):
        log.i('today->右上角日历按钮->返回')
        if self.is_ios():
            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Image[1]").click()
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_mail_button(self):
        log.i('today->右上角信封按钮')
        if self.is_ios():
            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[1]/Image[3]").click()
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_sleep(self):
        log.i('today->点击睡眠模块（右1区域）')
        if self.is_ios():
            self.s.tap_hold(0.758, 0.684)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_page_back(self):
        log.i('today->模块详情页->返回')
        if self.is_ios():
            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Image[1]").click()
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_task(self):
        log.i('today->点击目标模块（左1区域）')
        if self.is_ios():
            self.s.tap_hold(0.274, 0.69)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def otter_tab1(self):
        log.i('otter->点击tab1')
        if self.is_ios():
            self.s.tap_hold(0.169, 0.929)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_rings(self):
        log.i('today->点击三环模块（左2区域）')
        if self.is_ios():
            self.s.tap_hold(0.256, 0.798)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_calorie(self):
        log.i('today->点击卡路里模块（右2区域）')
        if self.is_ios():
            self.s.tap_hold(0.722, 0.811)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_water(self):
        log.i('today->点击喝水模块（左3区域）')
        if self.is_ios():
            self.s.tap_hold(0.28, 0.386)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_step(self):
        log.i('today->点击步数模块（右3区域）')
        if self.is_ios():
            self.s.tap_hold(0.712, 0.327)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_cycle(self):
        log.i('today->点击生理周期模块（右4区域）')
        if self.is_ios():
            self.s.tap_hold(0.731, 0.459)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_weight(self):
        log.i('today->点击体重模块（左4区域）')
        if self.is_ios():
            self.s.tap_hold(0.208, 0.512)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_mood(self):
        log.i('today->点击心情模块（右5区域）')
        if self.is_ios():
            self.s.tap_hold(0.74, 0.561)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_mood_friend(self):
        log.i('today->点击心情模块（右5区域）->好友')
        if self.is_ios():
            self.s.tap_hold(0.728, 0.181)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_REE_bodyMetrics(self):
        log.i('today->点击基础代谢模块（身体指标）')
        if self.is_ios():
            self.s.tap_hold(0.74, 0.561)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_aerobicFitness_bodyMetrics(self):
        log.i('today->点击有氧适能模块（身体指标）')
        if self.is_ios():
            self.s.tap_hold(0.465, 0.379)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_spO2_bodyMetrics(self):
        log.i('today->点击血氧模块（身体指标）')
        if self.is_ios():
            self.s.tap_hold(0.489, 0.545)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_wristTemp_bodyMetrics(self):
        log.i('today->点击手腕温度模块（身体指标）')
        if self.is_ios():
            self.s.tap_hold(0.45, 0.718)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_RHR_bodyMetrics(self):
        log.i('today->点击静息心率模块（身体指标）')
        if self.is_ios():
            self.s.tap_hold(0.483, 0.84)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_resp_bodyMetrics(self):
        log.i('today->点击呼吸频率模块（身体指标）')
        if self.is_ios():
            self.s.tap_hold(0.474, 0.594)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_resp_bodyMetrics(self):
        log.i('today->点击呼吸频率模块（身体指标）')
        if self.is_ios():
            self.s.tap_hold(0.371, 0.745)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def today_otter_back_bodyMetrics(self):
        log.i('today->身体指标->进入会员页面->返回')
        if self.is_ios():
            time.sleep(2)
            self.s.tap_hold(0.066, 0.091)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'



page = TodayPage()

def today():
    page.today_otter_aichat()
    page.today_otter_aichat_back()
    page.today_otter_watch_button()
    page.today_otter_watch_button_back()
    page.today_otter_data_button()
    page.today_otter_data_button_back()
    page.today_otter_task()
    page.otter_tab1()
    page.today_otter_rings()
    page.swipe_up()
    page.today_otter_page_back()
    page.today_otter_sleep()
    page.swipe_up()
    page.swipe_up()
    page.today_otter_page_back()
    page.today_otter_calorie()
    page.today_otter_page_back()
    page.swipe_up()
    page.today_otter_step()
    page.today_otter_page_back()
    page.today_otter_water()
    page.today_otter_page_back()
    page.today_otter_cycle()
    page.today_otter_page_back()
    page.today_otter_mood()
    page.today_otter_mood_friend()
    page.today_otter_page_back()
    page.today_otter_REE_bodyMetrics()
    page.today_otter_page_back()
    page.swipe_up()
    # page.today_otter_aerobicFitness_bodyMetrics()
    # page.today_otter_back_bodyMetrics()
    # page.today_otter_spO2_bodyMetrics()
    # page.today_otter_back_bodyMetrics()
    # page.today_otter_wristTemp_bodyMetrics()
    # page.today_otter_back_bodyMetrics()
    # page.today_otter_RHR_bodyMetrics()
    # page.today_otter_back_bodyMetrics()
    #没有做弹窗的处理，这块先不看
    page.swipe_up()
    page.today_otter_resp_bodyMetrics()
    page.swipe_down()




# def today_second_screen():
#     page.today_otter_page_back()