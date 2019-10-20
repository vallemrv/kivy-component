# -*- coding: utf-8 -*-

# @Author: Manuel Rodriguez <valle>
# @Date:   10-May-2017
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-19T02:08:06+02:00
# @License: Apache license vesion 2.0

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import (BooleanProperty, StringProperty, AliasProperty,
                             ObjectProperty, NumericProperty, ListProperty)
from kivy.lang import Builder
from kivy.metrics import dp
from components.buttons import ButtonColor, ButtonIcon, ButtonImg
from math import ceil
from datetime import datetime
from components.resources import Res as res

Builder.load_string('''
#:import res components.resources
#:import ButtonColor components.buttons


<GridButtons>:
    __header__: _header
    __button_salir__: _button_salir
    __content__: _content
    __main_content__: _main_content
    canvas:
        Color:
            rgba: root.bg_color
        Rectangle:
            pos: root.pos
            size: root.size
    BoxLayout:
        size_hint: .95, .95
        orientation: 'vertical'
        spacing: '10dp'
        id: _main_content
        BoxLayout:
            anchor_x: 'right'
            anchor_y: "top"
            size_hint: 1, .1
            id: _header
            Label:
                size_hint: .8, 1
                text: root.title
                color: 0,0,0,1
                font_size: root.title_size
            ButtonIcon:
                size_hint: .2, 1
                icon: res.FA_CHECK
                icon_size: '5dp'
                font_size: '10dp'
                icon_align: 'center'
                text: "Terminar"
                color: 0,0,0,1
                id: _button_salir
                bg_color: '#92CAF1'
                on_press: root.salir()
        GridLayout:
            cols: root.cols
            size_hint: 1,.9
            id: _content


''')
class GridButtons(AnchorLayout):
    bg_color = ObjectProperty([1,1,1,1])
    cols = NumericProperty(1)
    buttons = ListProperty([])
    selectable = BooleanProperty(True)
    column_color = StringProperty("bg_color")
    column_text = StringProperty("text")
    action_buttons = ObjectProperty(None)
    title = StringProperty("Titulo")
    hide_title = BooleanProperty(False)
    font_size = NumericProperty('25dp')
    title_size = NumericProperty('35dp')
    auto = BooleanProperty(True)

    def get_count(self):
        return len(self.__buttons_fisic__)
    count = AliasProperty(get_count, bind=["__buttons_fisic__"])


    __item_selected__ = ListProperty([])
    __buttons_fisic__ = ListProperty([])


    def on___buttons_fisic__(self, w, val):
        num = len(self.__buttons_fisic__)
        if self.auto:
            if num < 4:
                self.cols = 1
            elif num >= 4 and num <= 6:
                self.cols = 2
            elif num >= 6 and num <= 9:
                self.cols = 3
            elif num >9:
                self.cols = 4

    def on___item_selected__(self, w, val):
        sel = len(self.__item_selected__)
        if sel > 0:
            self.__button_salir__.text = "Sel %s" % sel
        else:
            self.__button_salir__.text = "Terminar"

    def on_hide_title(self, w, val):
        if  val:
            self.__main_content__.remove_widget(self.__header__)

    def on_selectable(self, w, val):
        if not val:
            self.__header__.remove_widget(self.__button_salir__)

    def add_widget(self, w):
        if type(w) in [ButtonColor, ButtonIcon, ButtonImg]:
            self.__buttons_fisic__.append(w)
            w.selectable = self.selectable
            w.font_size = self.font_size
            w.bind(on_press=self.on_press)
            self.bind(font_size=w.setter("font_size"))
            self.bind(selectable=w.setter('selectable'))
            self.__content__.add_widget(w)
        else:
            super(GridButtons, self).add_widget(w)

    def on_buttons(self, w, val):
        self.__content__.clear_widgets()
        self.__buttons_fisic__ = []
        for btn in self.buttons:
            btnC = ButtonColor(tag=btn,   selectable=self.selectable)
            self.__buttons_fisic__.append(btnC)
            if "selected" in btn:
                btnC.selected = btn.get("selected")
                self.__item_selected__.append(btnC)
            if self.column_text in btn:
                btnC.text=btn.get(self.column_text)
            if self.column_color in btn:
                btnC.bg_color = btn.get(self.column_color)
            if "icon" in btn:
                btnC.font_name = res.FONT_AWESOME
                btnC.text = btn.get("icon")
            btnC.font_size = self.font_size
            btnC.bind(on_press=self.on_press)
            self.bind(selectable=btnC.setter('selectable'))
            self.__content__.add_widget(btnC)


    def on_press(self, btn):
        if self.selectable and hasattr(btn, 'selected'):
            if not btn.selected:
                self.__item_selected__.append(btn)
            else:
                self.__item_selected__.remove(btn)
        elif self.action_buttons:
            self.action_buttons([btn])

    def salir(self):
        if self.action_buttons:
            self.action_buttons(self.__item_selected__)
