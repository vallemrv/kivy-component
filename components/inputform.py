# @Author: Manuel Rodriguez <valle>
# @Date:   16-Jul-2017
# @Email:  valle.mrv@gmail.com
# @Filename: imputform.py
# @Last modified by:   valle
# @Last modified time: 22-Jul-2017
# @License: Apache license vesion 2.0

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import (StringProperty, ObjectProperty, OptionProperty,
                             ListProperty, DictProperty, BooleanProperty)
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.metrics import dp
import components.resources as res

Builder.load_file(res.get_kv('inputform'))


class FloatTextInput(RelativeLayout):
    controller = ObjectProperty(None)
    input = ObjectProperty(None)
    text = StringProperty('')
    focus = BooleanProperty(False)
    label = StringProperty("")
    content = ObjectProperty(None)
    content_input = ObjectProperty(None)
    sel_color = ObjectProperty(None)
    type_input = OptionProperty("text",
                        options=('text', 'color', 'password', 'date'))

    def __init__(self, **kargs):
        super(FloatTextInput, self).__init__(**kargs)

    def on_focus(self, w, val):
        if not val and self.type_input == 'text':
            self.text = w.text
            self.controller.hide(self.input, w.text)


    def print_type(self):
        if self.content:
            self.content.clear_widgets()
            if self.type_input == 'color' and self.sel_color:
                self.sel_color.text = self.text
                self.content.add_widget(self.sel_color)
            if self.type_input == 'text' and self.content_input:

                self.content.add_widget(self.content_input)

    def on_input(self, w, val):
        self.text = val.text
        self.label = val.label
        self.type_input = val.type_input
        self.print_type()

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
    type_input = OptionProperty("text",
                          options=('text', 'color', 'password', 'date'))



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
                    'height': '50dp',
                    'type_input': 'text'
                }
        })

    def __init__(self, **kargs):
        super(InputForm, self).__init__(**kargs)

    def __clear_model__(self):
        self.model = {}
        self.form_content.clear_widgets()


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
        if len(self.children) < 3:
            super(InputForm, self).add_widget(widget)
        else:
            if type(widget) is ValleTextInput:
                self.model[widget.name] = widget.text
            height = self.form_content.parent.height  + widget.height + dp(25)
            self.form_content.parent.height = height
            self.form_content.add_widget(widget, 0)


    def add_model(self, model, columns=None, tmpl=None):
        self.__clear_model__()
        self.model = model
        columns = columns if columns else model.keys()
        for k in columns:
            if tmpl and k in tmpl:
                plantilla = tmpl.get(k).copy()
            elif k in self.plantilla:
                plantilla = self.plantilla.get(k).copy()
            else:
                plantilla = self.plantilla.get("all").copy()

            plantilla["name"] = k
            plantilla["text"] = unicode(model[k])
            plantilla["controller"] = self
            if not "label" in plantilla:
                plantilla["label"] = k.title()

            input = ValleTextInput(model=plantilla)
            self.add_widget(input)

    def form_check(self):
        if self.on_press:
            self.on_press(self.model)
