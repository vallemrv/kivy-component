# @Author: Manuel Rodriguez <valle>
# @Date:   2019-05-05T20:01:27+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-05-10T01:31:33+02:00
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
#:import LabelColor components.labels
#:import FloatButton components.floatbuttons

<TestWidget>:
    anchor_x: 'center'
    anchor_y: 'center'
    size_hint: 1, 1
    contador:0
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

        LabelColor:
            text: "LabelColor simple"
            bg_color: 1,1,.5,1
            border_size: '5dp'
        LabelIcon:
            text: "LabelIcon simple"
            bg_color: 1,.5,.5,1
            border_size: '5dp'
            icon: res.FA_CUBE

        LabelColor:
            id: _label_color
            clicable: True
            text: "LabelColor clicable"
            bg_color: 1,.5,.5,1
            border_size: '5dp'
            on_press:
                root.contador += 1
                _float_click.show_label()
                _float_click.text = ("Click %s" % root.contador)
                self.text = ("Click %s" % root.contador)

        LabelIcon:
            id: _label_icon
            text: "LabelIcon clicable"
            clicable: True
            bg_color: 1, 0, .5, .4
            border_size: '5dp'
            icon: res.FA_CHECK
            on_press:
                root.contador += 1
                _float_click.show_label()
                _float_click.text = ("Click %s" % root.contador)
                self.text = ("Click %s" % root.contador)
    FloatButton:
        icon: res.FA_REFRESH
        on_release:
            _float_label.show_label()
            root.contador = 0
            _label_icon.text = "LabelIcon clicable"
            _label_color.text = "LabelColor simple"


    FloatLabel:
        id: _float_label
        text: "Refresh labels"
        position: 'bottom'

    FloatLabel:
        id: _float_click
        bg_color: 1, 1, 1, 1
        text: "Cliclando labels"
        position: 'top'
        duration: 1

''')

class TestWidget(AnchorLayout):
    pass


class Test(App):
    def __init__(self, **kargs):
        super(Test, self).__init__(**kargs)
        self.title = "Test Labels"


    def build(self):
        return TestWidget()


if __name__ == '__main__':
    Test().run()
