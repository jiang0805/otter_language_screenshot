from pymobiledevice3.services.dvt.instruments.activity_trace_tap import ActivityTraceTap

from common.decorator import *


class AcitivityPage(Base):
    @step
    def otter_tab2(self):
        log.i('tab2 Activity页')
        if self.is_ios():
            self.s.tap_hold(0.365, 0.922)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def workout_acyivity(self):
        log.i('tab2 Activity->健身日历')
        if self.is_ios():
            self.s.tap_hold(0.522, 0.119)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def workout_month_acyivity(self):
        log.i('tab2 Activity->健身日历->月')
        if self.is_ios():
            self.s.tap_hold(0.719, 0.172)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def calendar_acyivity(self):
        log.i('tab2 Activity->今日拉起日历')
        if self.is_ios():
            self.s.tap_hold(0.148, 0.169)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def calendar_acyivity_close(self):
        log.i('tab2 Activity->今日拉起日历->close')
        if self.is_ios():
            self.s.swipe(0.5, 0.3, 0.5, 0.8)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def lunch_add_acyivity(self):
        log.i('tab2 Activity->添加午餐按钮')
        if self.is_ios():
            self.s.tap_hold(0.422, 0.656)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def all_add_acyivity(self):
        log.i('tab2 Activity->右下角添加按钮')
        if self.is_ios():
            self.s.tap_hold(0.815, 0.806)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def all_add_close_acyivity(self):
        log.i('tab2 Activity->右下角添加按钮->关闭浮窗')
        if self.is_ios():
            self.s.xpath(
                "//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Image[9]").click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def weight_add_acyivity(self):
        log.i('tab2 Activity->体重添加按钮')
        if self.is_ios():
            self.s.tap_hold(0.87, 0.426)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def page_close_acyivity(self):
        log.i('tab2 Activity->详情页或抽屉的关闭按钮')
        if self.is_ios():
            self.s.xpath("//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Image[1]").click()
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def workout_add_acyivity(self):
        log.i('tab2 Activity->健身添加按钮')
        if self.is_ios():
            self.s.tap_hold(0.882, 0.58)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'


page = AcitivityPage()

def activity():
    page.otter_tab2()
    page.calendar_acyivity()
    time.sleep(1)
    page.calendar_acyivity_close()
    page.lunch_add_acyivity()
    page.all_add_close_acyivity()
    page.all_add_acyivity()
    page.weight_add_acyivity()
    page.swipe_up()
    page.weight_add_acyivity()
    page.page_close_acyivity()
    page.workout_add_acyivity()
    page.page_close_acyivity()
    page.workout_acyivity()
    page.workout_month_acyivity()