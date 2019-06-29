# @Author: Manuel Rodriguez <valle>
# @Date:   2019-05-05T20:01:27+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-05-09T01:17:25+02:00
# @License: Apache License v2.0


import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.config import Config

Config.set("graphics", "width", "300")

Builder.load_string('''
#:import res components.resources
#:import Buttons components.buttons
#:import FloatButton components.floatbuttons


<TestWidget>:
    anchor_x: 'center'
    anchor_y: 'center'
    size_hint: 1, 1
    canvas:
        Color:
            rgba: 1,0,0,.5
        Rectangle:
            size: root.size
            pos: root.pos
    BoxLayout:
        orientation: 'vertical'
        size_hint: .9, .9
        spacing: dp(5)
        ButtonImg:
            bg_color: 1, .5, 1, 1
            src: "descarga.png"
            text: 'Boton img'
        ButtonIcon:
            icon: res.FA_EDIT
            text: "Boton icon"
            color: 1,0,1,1
            icon_size: dp(20)
        ButtonIcon:
            text: "Boton icon align rigth"
            icon: res.FA_ANGLE_RIGHT
            icon_align: 'right'
            on_release: print('Presionado boton right')
        ButtonIcon:
            text: "Boton icon align left"
            icon: res.FA_ANGLE_LEFT
            icon_align: 'left'
        ButtonColor:
            text: "Boton color #994411FF"
            bg_color: '#994411FF'
        ButtonColor:
            text: "Selectable"
            selectable: True
            bg_color: '#554411FF'
    FloatButton:
        contador: 0
        on_release:
            self.contador += 1
            print("presionado el FloatButton "+ str(self.contador))
        on_press:
            self.contador += 1
            print("presionado el FloatButton "+ str(self.contador))


''')

class TestWidget(AnchorLayout):
    pass


class Test(App):
    def __init__(self, **kargs):
        super(Test, self).__init__(**kargs)
        self.title = "Test Buttons"


    def build(self):
        return TestWidget()


if __name__ == '__main__':
    Test().run()
