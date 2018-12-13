# @Author: Manuel Rodriguez <valle>
# @Date:   10-May-2017
# @Email:  valle.mrv@gmail.com
# @Filename: listview.py
# @Last modified by:   valle
# @Last modified time: 06-Feb-2018
# @License: Apache license vesion 2.0

from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, NumericProperty
from kivy.utils import get_color_from_hex


Builder.load_string('''
#:import get_color kivy.utils.get_color_from_hex
<MenuListView>:
    list: _listado
    scroll: _scroll
    spacing: 5
    canvas.before:
        Color:
            rgb: get_color(root.bg_color)
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
    bg_color = StringProperty("#b8b3ac")
    row_height = NumericProperty("70dp")

    def add_widget(self, widget):
        if type(widget) is ScrollView:
            super(MenuListView, self).add_widget(widget)
        else:
            self.add_linea(widget)

    def add_linea(self, widget):
        self.list.add_widget(widget)
        self.scroll.scroll_y = 0

    def rm_linea(self, widget):
        self.list.remove_widget(widget)

    def rm_all_widgets(self):
        self.list.clear_widgets()

    def scroll_up(self, up=1):
        self.scroll.scroll_y = up
