# @Author: Manuel Rodriguez <valle>
# @Date:   20-Jul-2017
# @Email:  valle.mrv@gmail.com
# @Filename: spin.py
# @Last modified by:   valle
# @Last modified time: 2019-10-19T13:15:06+02:00
# @License: Apache license vesion 2.0


from kivy.uix.floatlayout import FloatLayout
from kivy.properties import BooleanProperty, NumericProperty
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_string('''
#:import path components.resources.Path
#:import res components.resources.Res
<Spin>:
    spin_label: _spin_label
    size_hint: 1, 1
    pos: 1000, 0
    canvas:
        Color:
            rgba: 0,0,0,.3
        Rectangle:
            size: self.size
            pos: self.pos
    Label:
        id: _spin_label
        pos_hint: {'center_x': .5, 'center_y': .5}
        canvas.before:
            PushMatrix
            Rotate:
                angle: root.angle
                origin: self.center
        canvas.after:
            PopMatrix
        font_name: path.FONT_AWESOME
        font_size: dp(50)
        text: res.FA_SPINNER
        size_hint: .5, .5
                ''')


class Spin(FloatLayout):
    bussy = BooleanProperty(False)
    angle = NumericProperty(0)

    def on_size(self, w, v):
        if not self.bussy:
            self.hide()

    def __init__(self, **kargs):
        super(Spin, self).__init__(**kargs)
        self.anim = Animation(angle = 360, duration=1.5)
        self.anim += Animation(angle = 360, duration=1.5)
        self.anim.repeat = True
        def hide(st):
            self.hide()
        Clock.schedule_once(hide, 1)

    def on_bussy(self, w, val):
        if self.spin_label:
            self.angle = 0
            if self.bussy:
                self.anim.start(self)
            else:
                self.anim.stop(self)

    def on_angle(self, item, angle):
        if angle == 360 and self.bussy:
            item.angle = 0
        elif not self.bussy:
            item.angle = 360


    def show(self):
        self.bussy = True
        ani = Animation(x=0, duration=.1)
        ani.start(self)

    def hide(self):
        self.bussy = False
        ani = Animation(x=self.width+10, duration=.1)
        ani.start(self)

    def collide_point(self, x, y):
        return (x > self.x and x < self.x +self.width) and (y > self.y and y < self.y +self.height)

    def on_touch_down(self, touch, *args):
        super(Spin, self).on_touch_down(touch)
        if self.collide_point(touch.x, touch.y):
            return True
