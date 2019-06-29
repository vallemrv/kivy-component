# @Author: Manuel Rodriguez <valle>
# @Date:   2019-05-05T20:01:27+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-05-09T01:15:55+02:00
# @License: Apache License v2.0


import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder
from kivy.logger import Logger

from components.floatbuttons import FloatButton
import components.resources as res


Builder.load_string('''
#:import res components.resources
#:import FloatButton components.floatbuttons
#:import LabelColor components.labels


<TestWidget>:
    anchor_x: 'center'
    anchor_y: 'center'
    size_hint: 1, 1
    contador: 0

    GridLayout:
        cols:2
        rows:2
        spacing: '10dp'
        orientation: "vertical"
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            canvas:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
            LabelColor:
                size_hint: .7,.7
                text: "FloatButtonGroup vertical sin animacion"
                color: "#000000"
                bg_color: "#ffffff"
            FloatButtonsGroup:
                orientation: "vertical"
                animate: False
                FloatButton:
                    icon: res.FA_SEARCH
                    bg_color: "#ffaa00ff"
                FloatButton:
                    icon: res.FA_HEART
                    bg_color: 1,0,.3,1
                FloatButton:
                    icon: res.FA_SPINNER
                    bg_color: 1,0,.3,1
                FloatButton:
                    icon: res.FA_USERS
                    bg_color: 1,0,.3,1
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            canvas:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
            LabelColor:
                size_hint: .7,.7
                text: "FloatButtonGroup horizontal con animacion"
                color: "#000000"
                bg_color: "#ffffff"
            FloatButtonsGroup:
                orientation: "horizontal"
                animate: True
                FloatButton:
                    icon: res.FA_BAN
                    bg_color: "#ffaa00ff"
                FloatButton:
                    icon: res.FA_CUBE
                    bg_color: 1,0,.3,1
                FloatButton:
                    icon: res.FA_CHART
                    bg_color: 1,0,.3,1
                FloatButton:
                    icon: res.FA_COGS
                    bg_color: 1,0,.3,1
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            canvas:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
            LabelColor:
                size_hint: .7,.7
                text: "FloatButton"
                color: "#000000"
                bg_color: "#ffffff"
            FloatButton:
                align: "bottom"
                icon: res.FA_DATABSE
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            canvas:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
            LabelColor:
                size_hint: .7,.7
                text: "FloatButton top size 35dp"
                color: "#000000"
                bg_color: "#ffffff"
            FloatButton:
                align: "top"
                button_size: '35dp'
                font_size: '10dp'
                icon: res.FA_DATABSE
''')



class TestWidget(AnchorLayout):
    pass


class Test(App):
    def __init__(self, **kargs):
        super(Test, self).__init__(**kargs)
        self.title = "Test FloatButtons"


    def build(self):
        return TestWidget()


if __name__ == '__main__':
    Test().run()
