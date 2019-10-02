# -*- coding: utf-8 -*-

# @Author: Manuel Rodriguez <valle>
# @Date:   06-Feb-2018
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-09-13T01:42:28+02:00
# @License: Apache license vesion 2.0

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.config import Config
from components.gridbuttons import GridButtons

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.utils import get_color_from_hex, get_hex_from_color
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import ObjectProperty, AliasProperty, OptionProperty

Config.set("graphics", "width", "350")
Config.set("graphics", "resizable", False)

Builder.load_string('''
#:import . components.pagenavigations
<FloatControl>:

<ValleInput>:
    canvas:
        Color:
            rgba: root.bg_color
        Rectangle:
            pos: root.pos
            size: root.size
    anchor_x: 'center'
    anchor_y: 'center'

    Label:
        color: root.color
        text: root.help


<ValleTextInput>:

<ValleForm>:
    _form_content: __form_content__
    canvas:
        Color:
            rgba: root.bg_color
        Rectangle:
            pos: root.pos
            size: root.size
    ScrollView:
        GridLayout:
            id: __form_content__
            cols: 1
            size_hint: 1, None
            spacing: dp(5)


<Main>:
    id_page: 'test_forms'
    title: 'Test forms'
    ValleForm:
        ValleTextInput:
            color: "#ff00ffff"



''')

class FloatControl(RelativeLayout):
    pass

class ValleForm(RelativeLayout):
    bg_color = ObjectProperty((1,1,1,1))
    size_control = ObjectProperty(dp(70))

    def on_bg_color(self, w, val):
        if "#" in val:
            val = "".join(val)
            self.bg_color = get_color_from_hex(val)
        else:
            self.bg_color = val

    def add_widget(self, w):
        if hasattr(w, "tipo_input"):
            self._form_content.add_widget(w)
            self._form_content.height  + int(self.size_control)
        else:
            super(ValleForm, self).add_widget(w)


class ValleInput(AnchorLayout, ButtonBehavior):
    color = ObjectProperty((1,1,1,1))
    bg_color = ObjectProperty((1,1,1,1))
    help = StringProperty("Hollaaaaaa")
    

    tipo_input = OptionProperty("Text", options=("Text", "Password",
                                "Numeric", "Color", "Date"))

    def on_color(self, w, val):
        if "#" in val:
            val = "".join(val)
            self.color = get_color_from_hex(val)
        else:
            self.color = val


    def on_bg_color(self, w, val):
        if "#" in val:
            val = "".join(val)
            self.bg_color = get_color_from_hex(val)
        else:
            self.bg_color = val


class ValleTextInput(ValleInput):
    pass


class Main(AnchorLayout):

    def on_click(self, nav):
        self.manager.navigate(nav)

class AppMain(App):
    def build(self):
        self.title = "Text input forms"
        return Main()


if __name__ == '__main__':
    AppMain().run()
