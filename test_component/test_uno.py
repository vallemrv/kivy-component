# -*- coding: utf-8 -*-

# @Author: Manuel Rodriguez <valle>
# @Date:   06-Feb-2018
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 09-Feb-2018
# @License: Apache license vesion 2.0

import os
import sys
import names
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.config import Config

Config.set("graphics", "width", "350")

Builder.load_string('''
#:import res components.resources
#:import PageManager components.pagenavigations
#:import MainPage components.pagenavigations
#:import Page components.pagenavigations
#:import MenuListView components.listview
#:import LabelIcon components.labels
#:import GridButtons components.gridbuttons
#:import ImputForm components.inputform
<BotonMenu@LabelIcon>:
    orientation: "horizontal"
    icon_align: "center"
    icon: res.FA_ANGLE_RIGHT
    bg_color: "#a49696"


<Main>:
    manager: _manager
    PageManager:
        id: _manager
        MainPage:
            title: "Menu"
            MenuListView:
                spacing: 0
                BotonMenu:
                    text: "Test botonera"
                    on_release: root.on_click("botonera")
                BotonMenu:
                    text: "Test selector"
                    on_release: root.on_click("selectable")
                BotonMenu:
                    text: "Test botones"
                    on_release: root.on_click("botones")
                BotonMenu:
                    text: "Test input form"
                    on_release: root.on_click("inputform")
                BotonMenu:
                    text: "Float group"
                    on_release: root.on_click("floatgroup")
        Page:
            id_page: "botonera"
            title: "Test botonera"
            GridButtons:
                buttons: [{"text": "Boton 1"}, {"text": "Boton 2"}, {"text": "Boton 3"}, {"text": "Boton 4"}]
        Page:
            id_page: "selectable"
            title: "Test selectable"
            GridButtons:
                selectable: True
                buttons: [{"text": "Boton 1"}, {"text": "Boton 2"}, {"text": "Boton 3"}, {"text": "Boton 4"}]
        Page:
            id_page: "botones"
            title: "Test botones"
            GridButtons:
                cols: 2
                ButtonIcon:
                    text: "Button Icon"
                    icon: res.FA_USERS
                ButtonIcon:
                    text: "Button Icon"
                    icon: res.FA_CHECK
                ButtonColor:
                    text: "Button Color"
                    bg_color: "#10e6a2"
                ButtonImg:
                    text: "Button Img"
                    src: 'descarga.png'
                ButtonImg:
                    text: "Button Img"
                    src: 'descarga.png'
                ButtonIcon:
                    icon: res.FA_BOOKS
                    icon_align: "center"
                    bg_color: "#eb4409"

        Page:
            id_page: "inputform"
            title: "Test form"
            InputForm:
            

        Page:
            id_page: "floatgroup"
            title: "Test float"

''')



class Main(AnchorLayout):
    def on_click(self, nav):
        self.manager.navigate(nav)


class AppMain(App):
    def build(self):
        self.title = "Text components"
        m = Main()
        m.color = "#566100"
        return Main()


if __name__ == '__main__':
    AppMain().run()
