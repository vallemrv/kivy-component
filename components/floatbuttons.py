# @Author: Manuel Rodriguez <valle>
# @Date:   2019-05-07T12:32:34+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-19T02:12:49+02:00
# @License: Apache License v2.0

from kivy.properties import (ObjectProperty, StringProperty, AliasProperty,
                             ListProperty, BooleanProperty, OptionProperty,
                             NumericProperty)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Ellipse
from kivy.graphics.instructions import InstructionGroup
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.logger import Logger
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.animation import Animation
from functools import partial
from components.resources import Res as res
from components.resources import get_kv

Builder.load_file(get_kv("floatbuttons"))

class FloatButtonBase(AnchorLayout):
    icon = StringProperty(res.FA_EDIT)
    color = ObjectProperty([1,1,1,1])
    bg_color = ObjectProperty([ 0,.4,.6,1])
    font_size = ObjectProperty('20dp')
    button_size = ObjectProperty("65dp")
    align = OptionProperty("bottom", options=["bottom", "top"])
    press = ObjectProperty(None)
    release = ObjectProperty(None)

    def get_button_size(self):
        if type(self.button_size) is str:
            self.button_size = dp(self.button_size.replace('dp',''))
        return (self.button_size, self.button_size)


    __button_size__ = AliasProperty(get_button_size, bind=["button_size"])

class FloatButtonWidget(ButtonBehavior, AnchorLayout):

    __shape_up__ = None
    __shape_down__ = None

    def collide_point(self, x, y):
        return (x > self.x and x < self.x +self.width) and (y > self.y and y < self.y +self.height)

    def on_press(self):
        if self.__shape_down__ == None:
            self.__shape_down__ = InstructionGroup(grup="__shape_down__")
        else:
            self.canvas.remove(self.__shape_down__)
            self.__shape_down__.clear()
        color = Color(0,0,0,.4)
        self.__shape_down__.add(color)
        self.__shape_down__.add(Ellipse(pos=self.pos, size=self.size))
        self.canvas.add(self.__shape_down__)
        super(FloatButtonWidget, self).on_press()

    def on_release(self):
        self.canvas.remove(self.__shape_down__)
        self.__shape_down__.clear()
        super(FloatButtonWidget, self).on_release()

class FloatButton(FloatButtonBase):

    def on_color(self, w, val):
        if "#" in val:
            val = "".join(val)
            self.color = get_color_from_hex(val)
        else:
            self.color = val

    def on_bg_color(self, root, val):
        if "#" in val:
            val = "".join(val)
            self.bg_color = get_color_from_hex(val)
        else:
            self.bg_color = val

class FloatButtonsGroup(AnchorLayout):
    orientation = OptionProperty("vertical", options=("vertical", "horizontal"))
    button_size = NumericProperty("50dp")
    color = ObjectProperty([1,1,1,1])
    bg_color = ObjectProperty([ 0,.4,.6,1])
    animate = BooleanProperty(True)


    __primera_vez__ = BooleanProperty(True)
    __content_button_height__ = NumericProperty("50dp")
    __show_buttons__ = BooleanProperty(False)
    __lista_buttons__ = ListProperty([])

    def get__content_button_size__(self):
        if type(self.button_size) is str:
            self.button_size = dp(self.button_size.replace('dp',''))
        width = self.button_size
        height = self.button_size
        if self.orientation == "vertical":
            width = self.button_size
            height = self.__content_button_height__
        else:
            height = self.button_size
            width = self.__content_button_height__

        return (width, height)

    def on_orientation(self, w, val):
        self.__content_button_height__ += 1


    __content_button_size__ = AliasProperty(get__content_button_size__,
                                            bind=["__content_button_height__",
                                                  "button_size",])

    def on_size(self, w, val):
        if not self.__show_buttons__ and self.animate:
            Clock.schedule_once(partial(self.on___show_buttons__,
                                        self, bool(self.__show_buttons__)), .5)
        elif not self.animate and self.__primera_vez__:
            self.__primera_vez__ = False
            self.__content_button__.remove_widget(self.__button_principal__)



    def __init__(self, **kargs):
        super(FloatButtonsGroup, self).__init__(**kargs)


    def on___show_buttons__(self, w, val, *dt):
        if self.animate:
            time = 0.1
            duration = 0.05
            for w in self.__lista_buttons__:
                if val:
                    x = -dp(400)
                else:
                    x = dp(400)
                time += 0.1
                Clock.schedule_once(partial(self.start_animation, w, x, duration), time)

    def start_animation(self, w, x, duration, dt):
        ani = Animation(x=w.x + x, duration=duration)
        ani.start(w)


    def show_buttons(self, *args):
        self.__show_buttons__ = not self.__show_buttons__


    def add_widget(self, w):
        if type(w) is FloatButton:
            w.button_size = self.button_size
            self.__content_button__.remove_widget(self.__button_principal__)
            self.__content_button_height__ +=  self.button_size + dp(10)
            self.__content_button__.add_widget(w)
            self.__content_button__.add_widget(self.__button_principal__)
            self.__lista_buttons__.append(w)
        else:
            super(FloatButtonsGroup, self).add_widget(w)
