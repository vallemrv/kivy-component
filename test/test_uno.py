# -*- coding: utf-8 -*-

# @Author: Manuel Rodriguez <valle>
# @Date:   06-Feb-2018
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-07-05T22:27:03+02:00
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
    PageManager:
        id: _manager
        Page:
            id_page: 'Menu'
            title:  'Hola caracola'
            ScrollView:
                size_hint: 1,1
                GridButtons:
                    id: _botonera
                    selectable: False
                    hide_title: True
                    size_hint: 1, None
                    cols: 1
                    on_width: self.height = self.count * dp(100)
                    ButtonColor:
                        text: "Test botones"
                        on_release: _manager.navigate("test_botones")
                    ButtonColor:
                        text: "Test floatbuttons"
                        on_release: _manager.navigate("test_floatbutton")
                    ButtonColor:
                        text: "Test labels"
                        on_release: _manager.navigate("test_labels")
                    ButtonColor:
                        text: "Test botnonera no selectable"
                        on_release: _manager.navigate("test_botonera")
                    ButtonColor:
                        text: "Test botonera selectable"
                        on_release: _manager.navigate("test_botonera_selectable")
                    ButtonColor:
                        text: "Test forms"
                        on_release: _manager.navigate("test_forms")


        Page:
            id_page: 'test_botones'
            title: 'Test botones'
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'center'
                BoxLayout:
                    size_hint: .9,.8
                    orientation: 'vertical'
                    GridLayout:
                        spacing: 5
                        cols:2
                        ButtonImg:
                            src: 'descarga.png'
                        ButtonColor:
                            text: 'Boton color'
                            bg_color: 1,.5,.5,1
                        ButtonIcon:
                            icon: res.FA_CHECK
                        ButtonIcon:
                            icon: res.FA_EDIT
                            text: "boton con texto"
                        ButtonIcon:
                            icon: res.FA_EUR
                        ButtonColor:
                            text: 'Boton_color'
                            bg_color: .9,.3,.5,1
                    ButtonIcon:
                        size_hint: 1,.2
                        icon: res.FA_LEMON
                        icon_align: 'left'
                        text: 'align left'

        Page:
            id_page: 'test_floatbutton'
            title: 'Test floatbuttons'
            LabelColor:
                text: 'FloatButton grupo y solitario.'
                color: 0,0,0,1
                bg_color: '#FFFFFF'
            FloatButton:
                align: 'top'
                button_size: dp(50)
            FloatButtonsGroup:
                FloatButton:
                    icon: res.FA_BOOKS
                FloatButton:
                    icon: res.FA_USERS
                FloatButton:
                    icon: res.FA_COGS
        Page:
            id_page: 'test_labels'
            title: 'Test labels'
            BoxLayout:
                orientation: 'vertical'
                LabelColor:
                    text: "label con color"
                    bg_color: .9,0,.9,1
                LabelColor:
                    clicable: True
                    text: 'Label clicable'
                    gb_color: .9,.9,0,1
                LabelIcon:
                    src: res.FA_ANGLE_LEFT
                    text: 'Label con icono'
                    icon_align: "left"

            FloatButton:
                on_press: _info.show_label()
            FloatLabel:
                position: 'top'
                id: _info
                text: 'Info: Me mola kivy'

        Page:
            id_page: 'test_botonera_selectable'
            title: 'Bontonera selectable'
            GridButtons:
                title: 'GridButtons'
                ButtonColor:
                    text: 'Test 1'
                ButtonColor:
                    text: 'text 2'
                ButtonColor:
                    text: 'text 3'
                ButtonColor:
                    text: 'text 4'
        Page:
            id_page: 'test_botonera'
            title: 'Test botonera'
            GridButtons:
                selectable: False
                title: 'GridButtons'
                title_size: dp(20)
                buttons:
                    [{"text": "Test_1"}, {"text": "Test_2"}, {"text": "Test_2"},
                    {"text": "Test_3"}, {"text": "Test_4"},{"text": "Test_5"},
                    {"text": "Test_6"},{"text": "Test_7"}, {"text": "Test_8"}]

        Page:
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
