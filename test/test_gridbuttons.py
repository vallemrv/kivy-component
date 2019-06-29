# @Author: Manuel Rodriguez <valle>
# @Date:   2019-05-05T20:01:27+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-05-13T23:11:56+02:00
# @License: Apache License v2.0
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kivy.properties import (NumericProperty, ListProperty, StringProperty,
                             BooleanProperty, ObjectProperty)
from components.buttons import ButtonImg, ButtonColor, ButtonIcon
from kivy.utils import get_hex_from_color

from kivy.app import App

from kivy.uix.anchorlayout import AnchorLayout
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder
from kivy.logger import Logger
import components.resources as res

Builder.load_string('''
#:import res components.resources
#:import GridButtons components.gridbuttons
#:import ButtonColor components.buttons

<TestWidget>:
    anchor_x: 'center'
    anchor_y: 'center'
    size_hint: 1, 1
    contador: 0
    buttons: []
    GridButtons:
        title_size: '50dp'
        title: 'Prueba de botonera'
        font_size: '35dp'
        selectable: False
        buttons: root.buttons




''')





class TestWidget(AnchorLayout):
    pass


class Test(App):
    buttons = []
    def __init__(self, **kargs):
        super(Test, self).__init__(**kargs)
        self.title = "Test FloatButtons"


    def build(self):
        test_botonera = TestWidget()
        for x in range(1, 10):
            test_botonera.buttons.append({"text": "Button %s" % x, "bg_color": [0,0,1,1]})
        return test_botonera


if __name__ == '__main__':
    Test().run()
