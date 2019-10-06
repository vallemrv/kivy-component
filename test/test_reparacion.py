# @Author: Manuel Rodriguez <valle>
# @Date:   2019-10-07T00:33:36+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-07T01:11:44+02:00
# @License: Apache License v2.0



import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder
from kivy.logger import Logger

from components.pagenavigations import PageManager
from components.floatbuttons import FloatButton
import components.resources as res


Builder.load_string('''
#:import . components.pagenavigations

<TestWidget>:
    Page:
        title: 'Test Reparacion'
        FloatButtonsGroup:
            orientation: 'horizontal'
            FloatButton:
            FloatButton:
            FloatButton:
''')



class TestWidget(PageManager):
    pass


class Test(App):
    def __init__(self, **kargs):
        super(Test, self).__init__(**kargs)
        self.title = "Test Reparacion"


    def build(self):
        return TestWidget()


if __name__ == '__main__':
    Test().run()
