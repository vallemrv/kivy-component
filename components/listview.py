# @Author: Manuel Rodriguez <valle>
# @Date:   10-May-2017
# @Email:  valle.mrv@gmail.com
# @Filename: listview.py
# @Last modified by:   valle
# @Last modified time: 2019-10-19T02:46:44+02:00
# @License: Apache license vesion 2.0

from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, ListProperty, NumericProperty
from kivy.utils import get_color_from_hex

Builder.load_string('''
<MenuListView>:
    __list__: _listado
    __scroll__: _scroll
    spacing: 5
    canvas.before:
        Color:
            rgba: root.bg_color
        Rectangle:
            size: self.size
            pos: self.pos
    anchor_x: 'center'
    anchor_y: 'center'
    ScrollView:
        id: _scroll
        size_hint: 1, 1
        GridLayout:
            cols: 1
            spacing: root.spacing
            size_hint: 1, None
            height: len(self.children) * dp(root.row_height)
            id: _listado
                    ''')

class MenuListView(AnchorLayout):
    bg_color = ObjectProperty((1,1,1,1))
    row_height = NumericProperty("70dp")

    def on_bg_color(self, w, val):
        if "#" in val:
            val = "".join(val)
            self.bg_color = get_color_from_hex(val)
        else:
            self.bg_color = val

    def add_widget(self, widget):
        if type(widget) is ScrollView:
            super(MenuListView, self).add_widget(widget)
        else:
            self.__list__.add_widget(widget)

    def add_linea(self, widget):
        self.__list__.add_widget(widget)
        self.__scroll__.scroll_y = 0

    def rm_linea(self, widget):
        self.__list__.remove_widget(widget)

    def rm_all_widgets(self):
        self.__list__.clear_widgets()

    def scroll_up(self, up=1):
        self.__scroll__.scroll_y = up

    def get_lineas(self):
        return self.__list__.children
