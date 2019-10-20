# @Author: Manuel Rodriguez <vallemrv>
# @Date:   11-Jul-2017
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-19T02:13:21+02:00
# @License: Apache license vesion 2.0


from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.vector import Vector
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.graphics.instructions import InstructionGroup
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.properties import (StringProperty, ObjectProperty, BooleanProperty,
                             ListProperty, OptionProperty, NumericProperty,
                             AliasProperty)
from kivy.clock import Clock
from kivy.animation import Animation
from math import ceil
from datetime import datetime
from components.resources import Res as res
from components.resources import get_kv

Builder.load_file(get_kv("labels"))

class LabelDecorators(AnchorLayout):
    def __init__(self, **kargs):
        super(LabelDecorators, self).__init__(**kargs)

class LabelBase(ButtonBehavior, Widget):
    bg_color = ObjectProperty((0,1,.5,1))
    color = ObjectProperty((0,0,0,1))
    text = StringProperty()
    font_size = StringProperty('30dp')
    border_size = NumericProperty("3dp")
    valign = OptionProperty("middle",  options=["top","middle","bottom"])
    halign = OptionProperty("center",  options=["left","center","right"])
    tag = ObjectProperty(None, allowNone=True)
    clicable = BooleanProperty(False)
    pres = ObjectProperty(None)


    def __init__(self, **kargs):
       super(LabelBase, self).__init__(**kargs)
       self.__shape_down__ = None


    __listchild__ = ListProperty([])


    def on___listchild__(self, w, val):
        if self.container != None:
            for w in self.__listchild__:
                self.container.add_widget(w)

    def add_widget(self, widget):
        if type(widget) is LabelDecorators:
            super(LabelBase, self).add_widget(widget)
        else:
            self.__listchild__.append(widget)

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

    def collide_point(self, x, y):
        return (x > self.x and x < self.x +self.width) and (y > self.y and y < self.y +self.height)

    def on_touch_down(self, touch, *args):
        if self.collide_point(touch.x, touch.y) and self.clicable:
            size = dp(70), dp(70)
            w, h = size
            pos = touch.x -w/ 2, touch.y - h/2
            if self.__shape_down__ == None:
                self.__shape_down__ = InstructionGroup(group="__shape_down__")
            else:
                self.container.canvas.before.remove(self.__shape_down__)
                self.__shape_down__.clear()
            color = Color(0,0,0,.4)
            self.__shape_down__.add(color)
            self.__shape_down__.add(Ellipse(pos=pos, size=size))
            self.container.canvas.before.add(self.__shape_down__)
            Clock.schedule_once(self.remove_shape_down, .2)
            press = datetime.now()
            super(LabelBase, self).on_touch_down(touch)
            return True

    def remove_shape_down(self, dt):
        self.container.canvas.before.remove(self.__shape_down__)
        self.__shape_down__.clear()



class LabelColor(LabelBase):
    def on_text(self, w, v):
        pass

class LabelIcon(LabelBase):
    icon = StringProperty(res.FA_ANGLE_RIGHT)

class FloatLabel(AnchorLayout):
    text = StringProperty("")
    position = OptionProperty("bottom", options=["bottom", "top"])
    duration = NumericProperty(3)
    clicable = BooleanProperty(False)
    bg_color = ObjectProperty((0, 1, .2, 1))
    color = ObjectProperty((0,0,0,1))


    __show__ = BooleanProperty(False)
    __contador__ = NumericProperty(0)


    def __get_pos_widget__(self):
        if not self.__show__:
            if self.position == 'bottom':
                return 0, -self.height
            else:
                return 0, self.height

    __pos_widget__ = AliasProperty(__get_pos_widget__, bind=["position",
                                                             "size"])

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


    def __init__(self, **kargs):
        super(FloatLabel, self).__init__(**kargs)


    def show(self):
        if not self.__show__:
            self.__show__ = True
            y = self.height if self.position == 'bottom' else -self.height
            ani = Animation(y=self.__label_widget__.y + y, duration=.5)
            ani.start(self.__label_widget__)
            Clock.schedule_once(self.hide_label, self.duration+.5)
        else:
            self.__contador__ += 1
            Clock.schedule_once(self.hide_label, self.duration+.5)


    def hide_label(self, dt):
        if self.__contador__ <= 0:
            self.__contador__ = 0
            y = -self.height if self.position == 'bottom' else self.height
            ani = Animation(y=self.__label_widget__.y + y, duration=.5)
            ani.start(self.__label_widget__)
            Clock.schedule_once(self.clear_show, .5)
        else:
            self.__contador__ -= 1

    def clear_show(self, dt):
        self.__show__ = False
