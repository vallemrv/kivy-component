# @Author: Manuel Rodriguez <valle>
# @Date:   16-Jul-2017
# @Email:  valle.mrv@gmail.com
# @Filename: imputform.py
# @Last modified by:   valle
# @Last modified time: 18-Jul-2017
# @License: Apache license vesion 2.0

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import (StringProperty, ObjectProperty,
                             ListProperty, DictProperty, BooleanProperty)
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.metrics import dp


Builder.load_string('''
#:import get_color kivy.utils.get_color_from_hex
#:import ButtonIcon components.buttons.ButtonIcon
#:import res components.resources
<FloatTextInput>:
    input_text: _input
    size_hint: 1, 1
    canvas:
        Color:
            rgba: .4,.4,.4,.4
        Rectangle:
            size: self.size
            pos: self.pos
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        size_hint: 1, 1
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            size_hint: .9, None
            height: dp(100)
            BoxLayout:
                orientation: 'horizontal'
                TextInput:
                    id: _input
                    size_hint: .7, None
                    height: dp(35)
                    font_size: root.font_size
                    multiline: False
                    focus: root.focus
                    text: root.text
                ButtonIcon:
                    icon: res.FA_CHECK
                    size_hint: None, None
                    height: dp(35)
                    width: dp(35)
                    font_size: '12dp'
                    border_size: 0
                    bgColor: '#a5e5f9'
                    on_release:
                        root.text = _input.text
                        root.controller.hide(root.input, _input.text)


<ValleTextInput>:
    AnchorLayout:
        anchor_y: 'center'
        anchor_x: 'center'
        canvas:
            Color:
                rgba: get_color(root.bgColor)
            Rectangle:
                size: self.size
                pos: self.pos
        GridLayout:
            cols: 1
            size_hint: .9, .9
            Label:
                size_hint: 1, None
                text: root.label
                text_size: self.size
                halign: 'left'
                valign: 'middle'
                color: .6,.6,.6,.9
                font_size: dp(15)
                height: dp(25)
            BoxLayout:
                orientation: 'vertical'
                size_hint: 1, 1
                Label:
                    text: root.text
                    font_size: root.font_size
                    text_size: self.size
                    size_hint: 1, 1
                    halign: 'left'
                    valign: 'middle'
                    id: _text
                    color: get_color(root.color)


            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'center'
                size_hint: 1, None
                height: dp(1)
                canvas:
                    Color:
                        rgba: 0,0,0,1
                    Rectangle:
                        size: self.size
                        pos: _text.x, _text.y-dp(3)


<InputForm>:
    float_input: _float_input
    form_content: _form_content
    canvas.before:
        Color:
            rgba: get_color(self.bgColor)
        Rectangle:
            size: self.size
            pos: self.pos
    ScrollView:
        BoxLayout:
            orientation: 'vertical'
            size_hint: 1, None
            GridLayout:
                cols: 1
                spacing: dp(5)
                size_hint: 1, 1
                id: _form_content


            AnchorLayout:
                anchor_y: 'center'
                anchor_x: 'right'
                size_hint: .95, .8
                ButtonIcon:
                    text: 'Aceptar'
                    icon: res.FA_CHECK
                    orientation: 'horizontal'
                    size_hint: .5, None
                    height: dp(40)
                    font_size: '20dp'
                    bgColor: '#EAF2B3'
                    color: 0,0,0,1
                    border_size: '1dp'
                    icon_font_size: '20dp'
                    on_release: root.enviar_form()


    FloatTextInput:
        id: _float_input
        pos: root.width+10, 0
        controller: root

                    ''')



class FloatTextInput(RelativeLayout):
    controller = ObjectProperty(None)
    input = ObjectProperty(None)
    font_size = StringProperty("15dp")
    text = StringProperty('')
    focus = BooleanProperty(False)

    def __init__(self, **kargs):
        super(FloatTextInput, self).__init__(**kargs)

    def on_input(self, w, val):
        self.text = val.text

    def collide_point(self, x, y):
       return (x > self.x and x < self.x +self.width) and (y > self.y and y < self.y +self.height)

    def on_touch_down(self, touch, *args):
       super(FloatTextInput, self).on_touch_down(touch)
       if self.collide_point(touch.x, touch.y):
           return True


class ValleTextInput(ButtonBehavior, RelativeLayout):
    label = StringProperty("")
    text = StringProperty("")
    color = StringProperty("#000000")
    bgColor = StringProperty("#ffffff")
    font_size = StringProperty("30dp")
    controller = ObjectProperty(None)
    name = StringProperty("")


    def __init__(self, model=None, **kargs):
        if model:
            kargs = {}
            for k in model:
                kargs[k] = model[k]
        super(ValleTextInput, self).__init__(**kargs)


    def on_release(self):
        if self.controller:
            self.controller.show(self)




class InputForm(RelativeLayout):
    bgColor = StringProperty("#ffffff")
    model = DictProperty({})
    form_content = ObjectProperty(None)
    on_press = ObjectProperty(None)
    plantilla = DictProperty({
                "all":{
                    'font_size': '20dp',
                    'size_hint': (1, None),
                    'height': '50dp'
                }
        })

    def __init__(self, **kargs):
        super(InputForm, self).__init__(**kargs)

    def show(self, input):
        ani = Animation(x=0, duration=0.05)
        ani.bind(on_complete=self.on_complete)
        self.float_input.input = input
        ani.start(self.float_input)


    def on_complete(self, ani, w):
        self.float_input.focus = True


    def hide(self, input, text):
        ani = Animation(x=self.width+10, duration=0.05)
        input.text = text
        self.model[input.name] = input.text
        self.float_input.focus = False
        ani.start(self.float_input)

    def add_widget(self, widget):
        if len(self.children) < 2:
            super(InputForm, self).add_widget(widget)
        else:
            if type(widget) is ValleTextInput:
                self.model[widget.name] = widget.text
            height = self.form_content.parent.height + dp(20) + widget.height
            self.form_content.parent.height = height
            self.form_content.add_widget(widget, 0)

    def add_model(self, model, order):
        self.model = model
        for k in order:
            if k in self.plantilla:
                plantilla = self.plantilla.get(k).copy()
            else:
                plantilla = self.plantilla.get("all").copy()

            plantilla["name"] = k
            plantilla["text"] = model[k]
            plantilla["controller"] = self
            if not "label" in plantilla:
                plantilla["label"] = k.title()

            input = ValleTextInput(model=plantilla)
            self.add_widget(input)

    def enviar_form(self):
        print self.model
        if self.on_press:
            self.on_press(self.model)
