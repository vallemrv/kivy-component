# -*- coding: utf-8 -*-

# @Author: Manuel Rodriguez <valle>
# @Date:   06-Feb-2018
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-07-05T22:43:35+02:00
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

Config.set("graphics", "width", "350")
Config.set("graphics", "resizable", False)

Builder.load_string('''
#:import . components.pagenavigations

<Main>:
    id_page: 'test_forms'
    title: 'Test forms'
    Form:


''')

class Main(AnchorLayout):

    def on_click(self, nav):
        self.manager.navigate(nav)

class AppMain(App):
    def build(self):
        self.title = "Text components"
        return Main()


if __name__ == '__main__':
    AppMain().run()
