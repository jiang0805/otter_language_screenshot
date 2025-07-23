from common.decorator import *


class TaskPage(Base):
    @step
    def otter_tab3(self):
        log.i('tab3 task页')
        if self.is_ios():
            self.s.tap_hold(0.619, 0.926)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def add_task(self):
        log.i('task页->创建任务按钮')
        if self.is_ios():
            self.s.tap_hold(0.489, 0.843)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    # @step
    # def close_task(self):
    #     log.i('task页->创建任务按钮->关闭')
    #     if self.is_ios():
    #         self.s.xpath(
    #             "//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Image[1]").click()
    #     else:
    #         self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
    #         assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
    #         assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
    #         assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def hat_task(self):
        log.i('task页->点击海獭，拉起装备页面')
        if self.is_ios():
            self.s.tap_hold(0.525, 0.33)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'


page = TaskPage()

def task():
    page.otter_tab3()
    page.add_task()
    page.close_task()
    page.hat_task()
    page.close_task()