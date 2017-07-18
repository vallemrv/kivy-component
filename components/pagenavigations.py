# @Author: Manuel Rodriguez <valle>
# @Date:   14-Jul-2017
# @Email:  valle.mrv@gmail.com
# @Filename: pagenavigations.py
# @Last modified by:   valle
# @Last modified time: 18-Jul-2017
# @License: Apache license vesion 2.0

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import (StringProperty, ListProperty,
                             ObjectProperty, DictProperty)
from kivy.animation import Animation
from kivy.lang import Builder

Builder.load_string('''
#:import LabelColor components.labels.LabelColor
#:import ButtonIcon components.buttons.ButtonIcon
#:import get_color kivy.utils.get_color_from_hex

<MainPage>:
    content_page: _content_page
    size_hint: 1, 1
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        AnchorLayout:
            id: _header
            size_hint: 1, None
            height: dp(50)
            anchor_y: 'top'
            anchor_x: 'center'
            canvas:
                Color:
                    rgb: 0,0,0
                Rectangle:
                    size: self.size
                    pos: self.pos
            LabelColor:
                size_hint: 1, .99
                text: root.title
                bgColor: root.title_bgColor
                border_size: 0
                font_size: '20dp'


        AnchorLayout:
            id: _content_page
            size_hint: 1, 1

<Page>:
    content_page: _content_page
    size_hint: 1, 1
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        AnchorLayout:
            id: _header
            size_hint: 1, None
            height: dp(50)
            anchor_y: 'top'
            anchor_x: 'center'
            canvas:
                Color:
                    rgb: 0,0,0
                Rectangle:
                    size: self.size
                    pos: self.pos
            LabelColor:
                size_hint: 1, .99
                text: root.title
                bgColor: root.title_bgColor
                border_size: 0
                font_size: '20dp'
            AnchorLayout:
                anchor_y: 'center'
                anchor_x: 'right'
                size_hint: .85, 1
                ButtonIcon:
                    size_hint: None, .7
                    width: dp(60)
                    text: 'back'
                    icon: res.FA_ANGLE_LEFT
                    orientation: 'horizontal'
                    font_size: '15dp'
                    border_size: 0
                    bgColor:'#EAF2B3'
                    color: 0,0,0,1
                    on_release: root.parent.back_page()

        AnchorLayout:
            id: _content_page
            size_hint: 1, 1
            canvas.before:
                Color:
                    rgb: get_color(root.bgColor)
                Rectangle:
                    size: self.size
                    pos: self.pos

''')

class MainPage(RelativeLayout):
    title = StringProperty('')
    title_bgColor = StringProperty("#ffffff")
    page_manager = ObjectProperty(None)

    def __init__(self, **kargs):
        super(MainPage, self).__init__(**kargs)

    def add_widget(self, widget):
        if len(self.children) < 1:
            super(MainPage, self).add_widget(widget)
        else:
            self.content_page.add_widget(widget)



class Page(RelativeLayout):
    title = StringProperty('')
    title_bgColor = StringProperty("#ffffff")
    id_page = StringProperty("")
    bgColor = StringProperty("#ffffff")


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


class PageManager(FloatLayout):
    pages = DictProperty({})
    stack_pages = ListProperty([])

    def __init__(self, **kargs):
        super(PageManager, self).__init__(**kargs)

    def add_widget(self, widget):
        widget.page_manager = self
        if type(widget) is MainPage:
            self.stack_pages.append(widget)
        elif type(widget) is Page:
            widget.bind(id_page=self.on_id_pages)

        super(PageManager,self).add_widget(widget)

    def on_width(self, w, val):
        for child in self.pages.values():
            child.pos = val +10, 0

    def on_id_pages(self, w, val):
        self.pages[val] = w


    def navigate(self, nav):
        w = self.pages[nav]
        self.stack_pages.append(self.pages[nav])
        ai = Animation(x=0, duration=.1)
        ai.start(w)

    def back_page(self):
        w = self.stack_pages.pop()
        ai = Animation(x=self.width+10, duration=.1)
        ai.start(w)
