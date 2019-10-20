# -*- coding: utf-8 -*-

# @Author: Manuel Rodriguez <valle>
# @Date:   09-Jul-2017
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-19T15:54:51+02:00
# @License: Apache license vesion 2.0

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.utils import get_color_from_hex, get_hex_from_color
from kivy.properties import (ObjectProperty, StringProperty, AliasProperty,NumericProperty,
                             ListProperty, BooleanProperty, OptionProperty)
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.graphics.instructions import InstructionGroup
from kivy.vector import Vector
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.logger import Logger
from components.resources import Res as res
from components.resources import get_kv

Builder.load_file(get_kv("buttons"))

class Decorators(AnchorLayout):
    def __init__(self, **kargs):
        super(Decorators, self).__init__(**kargs)

class ButtonBase(ButtonBehavior, Widget):
    #Para guardar datos en el boton y recuperarlas
    #despues en el evento.
    tag = ObjectProperty(None, allownone=True)
    #Colores del boton texto y fondo acepta hexadecimal y rgba
    bg_color = ObjectProperty([.5, .5, .5, 1])
    color = ObjectProperty([1, 1, 1, 1])
    font_size = ObjectProperty("20dp")
    border_size = NumericProperty('3dp')

    __container__ = ObjectProperty(None)
    __listchild__ = ListProperty([])
    __shape_up__ = ObjectProperty(None)
    __shape_down__ = ObjectProperty(None)


    def __init__(self, **kargs):
        super(ButtonBase, self).__init__(**kargs)

    def on_color(self, w, val):
        if "#" in val:
            val = "".join(val)
            self.color = get_color_from_hex(val)
        else:
            self.color = val


    def on_border_size(self, w, v):
        if self.__container__:
            self.__container__.size = (self.__container__.parent.width-self.border_size,
                                   self.__container__.parent.height-self.border_size)


    def on___container__(self, root, val):
        self.__container__.bind(pos=self.on___container___pos)
        self.__container__.size = (self.__container__.parent.width-self.border_size,
                               self.__container__.parent.height-self.border_size)


        for w in self.__listchild__:
            self.__container__.add_widget(w)
        self.draw_color()

    def on___listchild__(self, w, val):
        if self.__container__ != None:
            for w in self.__listchild__:
                self.__container__.add_widget(w)

    def add_widget(self, widget):
        if type(widget) is Decorators:
            super(ButtonBase, self).add_widget(widget)
        else:
            self.__listchild__.append(widget)


    def on___container___pos(self, root, val):
        if self.__shape_up__  == None:
            self.__shape_up__  = InstructionGroup(grup="__shape_up__ ")
        else:
            self.__container__.canvas.before.remove(self.__shape_up__ )
            self.__shape_up__ .clear()
        self.draw_color()

    def on_bg_color(self, root, val):
        if "#" in val:
            val = "".join(val)
            self.bg_color = get_color_from_hex(val)
        else:
            self.bg_color = val

        if get_hex_from_color(self.bg_color) <= "#33333333":
            self.color = (1,1,1,1)
        else:
            self.color = (0,0,0,1)

        if self.__shape_up__  == None:
            self.__shape_up__  = InstructionGroup(grup="__shape_up__ ")
        else:
            self.__container__.canvas.before.remove(self.__shape_up__ )
            self.__shape_up__ .clear()
        self.draw_color()

    def draw_color(self):
        if self.__container__ and self.__shape_up__ :
            size = self.__container__.size
            color = Color(*self.bg_color)
            self.__shape_up__ .add(color)
            self.__shape_up__ .add(Rectangle(pos=self.__container__.pos, size=size))
            self.__container__.canvas.before.add(self.__shape_up__ )


    def collide_point(self, x, y):
        return (x > self.x and x < self.x +self.width) and (y > self.y and y < self.y +self.height)

    def on_press(self):
        size = self.__container__.size
        if self.__shape_down__ == None:
            self.__shape_down__ = InstructionGroup(group="__shape_down__")
        else:
            self.__container__.canvas.before.remove(self.__shape_down__)
            self.__shape_down__.clear()
        color = Color(0,0,0,.4)
        self.__shape_down__.add(color)
        self.__shape_down__.add(Rectangle(pos=self.__container__.pos, size=size))
        self.__container__.canvas.before.add(self.__shape_down__)
        super(ButtonBase, self).on_press()

    def on_release(self):
        self.__container__.canvas.before.remove(self.__shape_down__)
        self.__shape_down__.clear()
        super(ButtonBase, self).on_release()

class ButtonColor(ButtonBase):
    text = StringProperty()
    selectable = BooleanProperty(False)
    selected = BooleanProperty(False)

    def __init__(self, **kargs):
        super(ButtonColor, self).__init__(**kargs)

    def on_selected(self, w, val):
        self.label_selected.text = res.FA_CHECK if val and self.selectable else ""

    def on_press(self):
        super(ButtonColor, self).on_press()
        if self.selectable:
            self.selected = not self.selected

class ButtonImg(ButtonBase):
    src = StringProperty()
    text = StringProperty()
    img_align = OptionProperty("center", options=("center", "left", "right"))

    __label_container__ = ObjectProperty(None, allownone=False)
    __orientation__ = OptionProperty("vertical", options=("vertical", "horizontal"))
    __label_size_hint__ = ListProperty([1, .2])
    __widget_image__ = ObjectProperty(None)



    def __init__(self, **kargs):
        super(ButtonImg, self).__init__(**kargs)


    def on___label___container(self, w, val):
        if self.text != "" and len(self.__label_container__.children) == 1:
            self.add_label()

    def on_text(self, w, val):
        if val != ""  and len(self.__label_container__.children) == 1:
            self.add_label()

    def add_label(self):
        label = Label(text=self.text, font_size=self.font_size,
                      color=self.color, size_hint= self.__label_size_hint__,
                      halign= 'center', valign='middle')

        self.bind(__label_size_hint__=label.setter('size_hint'))
        self.bind(size=label.setter("text_size"))
        self.bind(text=label.setter('text'))
        self.bind(color=label.setter('color'))
        self.bind(font_size=label.setter('font_size'))
        self.__label_container__.add_widget(label)

    def on_img_align(self, w, val):
        if val == "center":
            self.__label_size_hint__ = (1, .2)
            self.__orientation__ = "vertical"
        elif val == "left" or val == "right":
            self.__orientation__ = "horizontal"
            self.__label_size_hint__ = (.8, 1)
            self.__widget_image__.size_hint_x = .15
            if val == "right":
                self.__label_container__.remove_widget(self.__widget_image__)
                self.__label_container__.add_widget(self.__widget_image__)


class ButtonIcon(ButtonBase):
    icon = StringProperty('')
    text = StringProperty('')
    icon_align = OptionProperty("center", options=("center", "left", "right"))
    icon_size = ObjectProperty("20dp")

    __label_size_hint__ = ListProperty([1, .2])
    __label_container__ = ObjectProperty(allownone=False)
    __orientation__ = OptionProperty("vertical", options=("vertical", "horizontal"))
    __widget_icon__ = ObjectProperty(None)


    def get_font_size_icon(self):
        if type(self.font_size) is str:
            self.font_size = dp(self.font_size.replace('dp',''))
        if type(self.icon_size) is str:
            self.icon_size = dp(self.icon_size.replace('dp',''))
        return  self.font_size + self.icon_size

    font_size_icon = AliasProperty(get_font_size_icon, bind=["font_size", "icon_size"])

    def __init__(self, **kargs):
        super(ButtonIcon, self).__init__(**kargs)

    def on_label_container(self, w, val):
        if self.text != "" and len(self.__label_container__.children) == 1:
            self.add_label()

    def on_text(self, w, val):
        if val != ""  and  self.__label_container__ and len(self.__label_container__.children) == 1:
            self.add_label()

    def add_label(self):
        label = Label(text=self.text, font_size=self.font_size,
                               color=self.color, halign= 'center',
                               valign='middle', size_hint=self.__label_size_hint__)

        self.bind(__label_size_hint__=label.setter('size_hint'))
        self.bind(size=label.setter('text_size'))
        self.bind(text=label.setter('text'))
        self.bind(color=label.setter('color'))
        self.bind(font_size=label.setter('font_size'))
        self.__label_container__.add_widget(label)

        if self.icon_align == "right":
            self.__label_container__.remove_widget(self.__widget_icon__)
            self.__label_container__.add_widget(self.__widget_icon__)




    def on_icon_align(self, w, val):
        if val == "center":
            self.__label_size_hint__ = (1, .2)
            self.__orientation__ = "vertical"
        elif val == "left" or val == "right":
            self.__orientation__ = "horizontal"
            self.__label_size_hint__ = (.8, 1)
            self.__widget_icon__.size_hint_x = .15
            if val == "right":
                self.__label_container__.remove_widget(self.__widget_icon__)
                self.__label_container__.add_widget(self.__widget_icon__)
