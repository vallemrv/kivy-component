# @Author: Manuel Rodriguez <valle>
# @Date:   14-Jul-2017
# @Email:  valle.mrv@gmail.com
# @Filename: pagenavigations.py
# @Last modified by:   valle
# @Last modified time: 06-Feb-2018
# @License: Apache license vesion 2.0

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import (StringProperty, ListProperty, NumericProperty,
                             ObjectProperty, DictProperty)
from kivy.animation import Animation
from kivy.lang import Builder
import components.resources as res

Builder.load_file(res.get_kv("pagenavigations"))

#The home page is the first page that is displayed and usually contains a menu.
class MainPage(RelativeLayout):
    title = StringProperty('')
    title_bg_color = StringProperty("#ffffff")
    page_manager = ObjectProperty(None)
    show = ObjectProperty(None)

    def __init__(self, **kargs):
        super(MainPage, self).__init__(**kargs)

    def add_widget(self, widget):
        if len(self.children) < 1:
            super(MainPage, self).add_widget(widget)
        else:
            self.content_page.add_widget(widget)



#They are the ones that contain the pages of the application
class Page(RelativeLayout):
    title = StringProperty('')
    title_bg_color = StringProperty("#ffffff")
    id_page = StringProperty("")
    bg_color = StringProperty("#ffffff")
    show = ObjectProperty(None)

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
    bg_color = StringProperty('#FFFFFF')

    def __init__(self, **kargs):
        super(PageManager, self).__init__(**kargs)


    def add_widget(self, widget):
        widget.page_manager = self
        if self.__esPage__(widget, MainPage):
            self.stack_pages.append(widget)
        elif self.__esPage__(widget, Page):
            widget.bind(id_page=self.on_id_pages)

        super(PageManager,self).add_widget(widget)


    def on_width(self, w, val):
        for child in self.pages.values():
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
            if w.show:
                w.show(self)

    def back_page(self):
        w = self.stack_pages.pop()
        ai = Animation(x=self.width+10, duration=.1)
        ai.start(w)

    def __esPage__(self, widget, clase):
        esPage = type(widget) == clase
        for base in widget.__class__.__bases__:
            esPage = esPage or (base == clase)
        return esPage
