import uiautomator2 as u2
import wda

import readConfig


class Base:

    # def __init__(self, device):
    #     self.device = device
    #     self.s = None
    #     self.set_driver(device)

    @classmethod
    def set_driver(cls, device):
        print("run_device:", device.name)
        cls.device = device
        if device.os == 'ios':
            cls.s = wda.USBClient().session()
        else:
            cls.s = u2.connect(device.serial)

    def get_driver(self):
        return self.s

    def get_device(self):
        return self.device

    def is_ios(self):
        return self.device.os == 'ios'

    def start_app(self, pkg_name):
        self.s.app_start(pkg_name)

    @classmethod
    def set_path(cls, ps):
        cls.path = ps

    def get_path(self):
        return self.path

    def element_swipe(self, element, direction):
        """
        从UI对象的中心向其边缘滑动
        :param element: UI element
        :param direction: one of ("left", "right", "up", "down")
        """
        assert direction in ("left", "right", "up", "down")

        if self.is_ios():
            x_left, y_up, width, height = element.bounds
            x_center, x_right = int(x_left + width / 2), x_left + width
            y_center, y_down = int(y_up + height / 2), y_up + height

            if direction == 'up':
                self.s.swipe(x_center, y_center, x_center, y_up)
            elif direction == 'down':
                self.s.swipe(x_center, y_center, x_center, y_down)
            elif direction == 'left':
                self.s.swipe(x_center, y_center, x_left, y_center)
            elif direction == 'right':
                self.s.swipe(x_center, y_center, x_right, y_center)
        else:
            element.swipe(direction)

    def swipe_up(self, element=None):
        if element:
            self.element_swipe(element, 'up')
        else:
            self.s.swipe(0.5, 0.8, 0.5, 0.2)

    def swipe_down(self, element=None):
        if element:
            self.element_swipe(element, 'down')
        else:
            self.s.swipe(0.5, 0.2, 0.5, 0.8)

    def swipe_left(self, element=None):
        if element:
            self.element_swipe(element, 'left')
        else:
            self.s.swipe(0.8, 0.5, 0.2, 0.5)

    def swipe_right(self, element=None):
        if element:
            self.element_swipe(element, 'right')
        else:
            self.s.swipe(0.2, 0.5, 0.8, 0.5)

    def reset_driver(self,device):
        base_page = Base()
        base_page.set_driver(device)
        base_page.start_app(readConfig.ReadConfig().get_pkg_name())
