from uiautomator2 import Settings

from common.decorator import *


class Tab4Page(Base):

    @allure.step('点击settings')
    @step
    def otter_tab4(self):
        log.i('tab4 设置页')
        if self.is_ios():
            self.s.tap_hold(0.848, 0.931)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def about_you_settings(self):
        log.i('设置页->关于你')
        if self.is_ios():
            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[5]/Image[2]").click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def win_premium_settings(self):
        log.i('设置页->赢免费会员')
        if self.is_ios():
            el = self.s.xpath('//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[6]/Image[2]')
            print("win",el.exists)
            # self.s.tap_hold(0.867, 0.24)
            self.s.xpath('//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[6]/Image[2]').wait(3)
            self.s.xpath('//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[6]/Image[2]').click()
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def language_settings(self):
        log.i('设置页->切换语言')
        if self.is_ios():
            el=self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[7]/Image[2]")
            print("language",el.exists)

            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[7]/Image[2]").click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def settings_language_settings(self):
        log.i('设置页->切换语言->跳转系统设置')
        if self.is_ios():
            self.s.xpath(
                "//CollectionView/Cell[8]").click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    def settings_english_settings(self):
        log.i('设置页->切换语言->跳转系统设置->切换英语')
        if self.is_ios():
            self.s.xpath(
                '//Table/Cell/StaticText[@name="English"]').click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    def settings_japanese_settings(self):
        log.i('设置页->切换语言->跳转系统设置->切换日语')
        if self.is_ios():
            self.s.xpath(
                '//Table/Cell/StaticText[@name="日本語"]').click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    def settings_spanish_settings(self):
        log.i('设置页->切换语言->跳转系统设置->切换西班牙语')
        if self.is_ios():
            self.s.xpath(
                '//Table/Cell/StaticText[@name="Español"]').click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    def settings_korean_settings(self):
        log.i('设置页->切换语言->跳转系统设置->切换韩语')
        if self.is_ios():
            self.s.xpath(
                '//Table/Cell/StaticText[@name="한국어"]').click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'


    def settings_chinese_traditional_settings(self):
        log.i('设置页->切换语言->跳转系统设置->切换繁体中文')
        if self.is_ios():
            self.s.xpath(
                '//Table/Cell/StaticText[@name="繁體中文"]').click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    def settings_chinese_settings(self):
        log.i('设置页->切换语言->跳转系统设置->切换简体中文')
        if self.is_ios():
            self.s.xpath(
                '//Table/Cell/StaticText[@name="简体中文"]').click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    def settings_german_settings(self):
        log.i('设置页->切换语言->跳转系统设置->切换德语')
        if self.is_ios():
            self.s.xpath(
                '//Table/Cell/StaticText[@name="Deutsch"]').click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    def settings_portuguese_settings(self):
        log.i('设置页->切换语言->跳转系统设置->切换葡萄牙语')
        if self.is_ios():
            self.s.xpath(
                '//Table/Cell/StaticText[@name="Português (Brasil)"]').click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    def settings_france_settings(self):
        log.i('设置页->切换语言->跳转系统设置->切换法语')
        if self.is_ios():
            self.s.xpath(
                '//Table/Cell/StaticText[@name="Français"]').click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def noti_settings(self):
        log.i('设置页->通知')
        if self.is_ios():
            self.s.xpath('//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[8]/Image[2]').click()
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def units_settings(self):
        log.i('设置页->单位')
        if self.is_ios():
            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[9]/Image[2]").click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def friend_settings(self):
        log.i('设置页->好友')
        if self.is_ios():
            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[10]/Image[2]").click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'


    @step
    def share_redbook_settings(self):
        log.i('设置页->小红书')
        if self.is_ios():
            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[11]/Image[2]").click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def watch_apple_settings(self):
        log.i('设置页->其他->苹果手表同步')
        if self.is_ios():
            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[13]/Image[2]").click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def updatelog_settings(self):
        log.i('设置页->其他->更新日志')
        if self.is_ios():
            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[14]/Image[2]").click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def qa_settings(self):
        log.i('设置页->其他->常见问题')
        if self.is_ios():
            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[15]/Image[2]").click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def feedback_settings(self):
        log.i('设置页->其他->问题反馈')
        if self.is_ios():
            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[16]/Image[2]").click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def agreenment_privacy_settings(self):
        log.i('设置页->其他->隐私协议')
        if self.is_ios():
            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[17]/Image[2]").click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def agreenment_user_settings(self):
        log.i('设置页->其他->用户协议')
        if self.is_ios():
            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Other[18]/Image[2]").click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def close_agreenment_settings(self):
        log.i('设置页->其他->用户协议->关闭协议')
        if self.is_ios():
            self.s.xpath(
                "//Button").click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def back_page_settings(self):
        log.i('设置页->关闭二级页面')
        if self.is_ios():
            self.s.xpath(
                "//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Button[1]").click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def unit_back_page_settings(self):
        log.i('设置页->关闭单位二级页面')
        if self.is_ios():
            self.s.xpath(
                "//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Image[1]").click()

        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

    @step
    def watch_back_page_settings(self):
        log.i('设置页->关闭watch弹窗')
        if self.is_ios():
            self.s.swipe(0.5, 0.3, 0.5, 0.8)
            self.s.tap(0.501, 0.347)
        else:
            self.swipe_left(self.s(resourceId='app.podcast.cosmos:id/stvTitle'))
            assert self.s(text='锋芒榜').info['selected'], '点击锋芒榜，锋芒榜未处于选中状态'
            assert not self.s(text='最热榜').info['selected'], '点击锋芒榜，最热榜未处于不选中状态'
            assert not self.s(text='新星榜').info['selected'], '点击锋芒榜，新星榜未处于不选中状态'

page = Tab4Page()

def tab4():
    page.otter_tab4()
    page.about_you_settings()
    page.back_page_settings()
    page.swipe_up()
    time.sleep(1)
    page.win_premium_settings()
    page.swipe_right()
    page.noti_settings()
    page.unit_back_page_settings()
    page.units_settings()
    page.unit_back_page_settings()
    page.friend_settings()
    page.unit_back_page_settings()
    page.swipe_up()
    page.watch_apple_settings()
    time.sleep(1)
    page.watch_back_page_settings()
    time.sleep(1)
    # page.swipe_up()
    page.updatelog_settings()
    page.close_agreenment_settings()
    page.qa_settings()
    page.close_agreenment_settings()
    page.feedback_settings()
    page.close_agreenment_settings()
    page.agreenment_privacy_settings()
    page.close_agreenment_settings()
    page.agreenment_user_settings()
    page.close_agreenment_settings()

def chinese():
    page.otter_tab4()
    page.swipe_down()
    page.language_settings()
    page.settings_language_settings()
    page.settings_chinese_settings()

def chinese_traditional():
    page.otter_tab4()
    page.swipe_down()
    page.language_settings()
    page.settings_language_settings()
    page.settings_chinese_traditional_settings()

def spanish():
    page.otter_tab4()
    page.swipe_down()
    page.language_settings()
    page.settings_language_settings()
    page.settings_spanish_settings()

def korean():
    page.otter_tab4()
    page.swipe_down()
    page.language_settings()
    page.settings_language_settings()
    page.settings_korean_settings()

def japanese():
    page.otter_tab4()
    page.swipe_down()
    page.language_settings()
    page.settings_language_settings()
    page.settings_japanese_settings()

def france():
    page.otter_tab4()
    page.swipe_down()
    page.language_settings()
    page.settings_language_settings()
    page.settings_france_settings()

def german():
    page.otter_tab4()
    page.swipe_down()
    page.language_settings()
    page.settings_language_settings()
    page.settings_german_settings()

def portuguese():
    page.otter_tab4()
    page.swipe_down()
    page.language_settings()
    page.settings_language_settings()
    page.settings_portuguese_settings()

def tttt():
    page.otter_tab4()
    page.swipe_up()
    page.win_premium_settings()
    page.swipe_right()
    page.language_settings()
    page.settings_language_settings()
    page.settings_korean_settings()

