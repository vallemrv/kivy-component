# @Author: Manuel Rodriguez <valle>
# @Date:   14-Jul-2017
# @Email:  valle.mrv@gmail.com
# @Filename: pagenavigations.py
# @Last modified by:   valle
# @Last modified time: 2019-10-19T02:11:49+02:00
# @License: Apache license vesion 2.0

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import (StringProperty, ListProperty, NumericProperty,
                             ObjectProperty, DictProperty, BooleanProperty)
from kivy.animation import Animation
from kivy.lang import Builder
from components.resources import get_kv
from components.resources import Res as res
from datetime import  datetime

Builder.load_file(get_kv("pagenavigations"))


#They are the ones that contain the pages of the application
class Page(RelativeLayout):
    title = StringProperty('')
    title_bg_color = StringProperty((1,1,1,1))
    id_page = StringProperty(None)
    bg_color = ObjectProperty((1,1,1,1))
    manager = ObjectProperty(None)
    show = ObjectProperty(None)

    __main__ = BooleanProperty(False)
    __button_back__ = ObjectProperty(None)

    def on___button_back__(self, w, val):
        if self.__main__:
            self.__head__.remove_widget(self.__button_back__)

    def on_bg_color(self, w, val):
        if type(val) is str and "#" in val:
            self.bg_color = get_color_from_hex(val)
        else:
            self.bg_color = val

    def add_widget(self, widget):
        if len(self.children) < 1:
            super(Page, self).add_widget(widget)
        else:
            self.content_page.add_widget(widget)

    def collide_point(self, x, y):
       return (x > self.x and x < self.x +self.width) and (y > self.y and y < self.y +self.height)

    def on_touch_down(self, touch, *args):
       super(Page, self).on_touch_down(touch)
       if self.collide_point(touch.x, touch.y):
           return True

#This is the main class for navigations manage
class PageManager(FloatLayout):
    pages = DictProperty({})
    stack_pages = ListProperty([])

    def __init__(self, **kargs):
        super(PageManager, self).__init__(**kargs)


    def add_widget(self, widget):
        if hasattr(widget, 'id_page'):
            widget.manager = self
            widget.bind(id_page=self.on_id_pages)
            super(PageManager,self).add_widget(widget)
            if len(self.children) == 1:
                widget.__main__ = True
                self.stack_pages.append(widget)


    def on_width(self, w, val):
        for child in self.pages.values():
            if not child.__main__:
                child.pos = val +10, 0

    def on_id_pages(self, w, val):
        self.pages[val] = w


    def navigate(self, nav):
        if nav in self.pages:
            w = self.pages[nav]
            self.stack_pages.append(self.pages[nav])
            self.remove_widget(w)
            self.add_widget(w)
            ai = Animation(x=0, duration=.1)
            ai.start(w)
            w.show = datetime.now()

    def back_page(self):
        if len(self.stack_pages) > 1:
            w = self.stack_pages.pop()
            ai = Animation(x=self.width+10, duration=.1)
            ai.start(w)
            self.stack_pages[-1].show = datetime.now()
