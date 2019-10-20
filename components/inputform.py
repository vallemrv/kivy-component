# -*- coding: utf-8 -*-

# @Author: Manuel Rodriguez <valle>
# @Date:   16-Jul-2017
# @Email:  valle.mrv@gmail.com
# @Filename: imputform.py
# @Last modified by:   valle
# @Last modified time: 2019-10-19T02:13:07+02:00
# @License: Apache license vesion 2.0

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.utils import get_color_from_hex, get_hex_from_color
from kivy.properties import (StringProperty, ObjectProperty, OptionProperty,
                             ListProperty, DictProperty, BooleanProperty, AliasProperty)
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.metrics import dp
from components.resources import Res as res
from components.resources import get_kv

Builder.load_file(get_kv('inputform'))

tipo = [
    'CharField', 'DecimalField', 'DateField',
    'DateTimeField', 'BooleanField', 'IntegerField', 'FloatField', 'TextField'
]

def get_type_control(tipo):
    if tipo in ['CharField', 'EmailField']:
        return "text"
    elif tipo in ["TextField"]:
        return "text_edit"
    elif tipo in ['IntegerField']:
        return "number"
    elif tipo in ['DateField',]:
        return "date"
    elif tipo in ['DateTimeField',]:
        return "datetime"
    elif tipo in ['DecimalField', 'FloatField',]:
        return "float"
    elif tipo in ['BooleanField',]:
        return "boolean"


class FloatTextInput(AnchorLayout):
    focus = BooleanProperty(False)
    text = StringProperty("")
    label = StringProperty("")
    controller = ObjectProperty(None)
    input = ObjectProperty(None)
    active = BooleanProperty(False)

    def __init__(self, **kargs):
        super(FloatTextInput, self).__init__(**kargs)

    def on_focus(self, w, l):
        if not self.focus and self.input and self.active:
            self.controller.hide(self.input)

class FloatColorInput(BoxLayout):
    active = BooleanProperty(False)
    def __init__(self, **kargs):
        super(FloatColorInput, self).__init__(**kargs)

class FloatControl(RelativeLayout):
    controller = ObjectProperty(None)
    input = ObjectProperty(None)
    text = StringProperty('')
    focus = BooleanProperty(False)
    label = StringProperty("")
    content = ObjectProperty(None)
    type_control = OptionProperty("text",
                        options=('text', 'color', 'password', 'date',
                                 'number', "float", "text_edit", "boolean", "select"))

    def __init__(self, **kargs):
        super(FloatControl, self).__init__(**kargs)
        self.textinput = FloatTextInput()
        self.bind(focus=self.textinput.setter('focus'))
        self.colorinput = FloatColorInput()

    def on_controller(self, w, l):
        self.textinput.controller = l
        self.colorinput.controller = l

    def collide_point(self, x, y):
        return (x > self.x and x < self.x +self.width) and (y > self.y and y < self.y +self.height)

    def on_touch_down(self, touch, *args):
        super(FloatControl, self).on_touch_down(touch)
        if self.collide_point(touch.x, touch.y):
            return True

    def print_type(self):
        if self.content:
            self.content.clear_widgets()
            self.textinput.active = False
            self.colorinput.active = False
            input_control = None
            if  self.type_control in ('text', 'password'):
                input_control = self.textinput
                self.textinput.ids._input.password = (self.type_control == "password")
            if  self.type_control == 'color':
                input_control = self.colorinput


            input_control.text = self.text
            input_control.label = self.label
            input_control.input = self.input
            input_control.active = True
            self.content.add_widget(input_control)


    def on_input(self, w, val):
        self.text = val.text
        self.label = val.label
        self.type_control = val.type_control
        self.print_type()

#This is how de control see it
class FormControl(RelativeLayout):
    label = StringProperty("")
    text = StringProperty("")
    color = ObjectProperty((0,0,0,1))
    bg_color = StringProperty((1,1,1,1))
    font_size = StringProperty("30dp")
    controller = ObjectProperty(None)
    name = StringProperty("")

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

    def __init__(self, model=None, **kargs):
        self.isFormControl = True
        kargs = {}
        if model:
            for k in model:
                kargs[k] = model[k]

        super(FormControl, self).__init__(**kargs)

    def add_widget(self, widget):
        if len(self.children) < 1:
            super(FormControl,self).add_widget(widget)
        else:
            self.content.add_widget(widget)

class InputTextControl(ButtonBehavior, FormControl):
    def set_text(self, value):
        self.__text__ = value

    def get_text(self):
        if self.type_control == "password":
            return  "*" * len(self.__text__)
        else:
            return self.__text__

    text = AliasProperty(get_text, set_text, bind=['__text__'])
    __text__ = StringProperty("")
    type_control = OptionProperty("text",
                          options=('text', 'color', 'password', 'date'))


    def on_release(self):
        if self.controller:
            self.controller.show_text_input(self)

class CheckBoxControl(FormControl):
    def set_text(self, value):
        self.active = value

    def get_text(self):
        return  self.active

    text = AliasProperty(get_text, set_text, bind=['active'])
    active = BooleanProperty(False)

    def on_active(self, w, l):
        if self.controller:
            self.controller.on_model_chage(self)

class Form(RelativeLayout):
    bg_color = ObjectProperty((1,1,1,1))
    model = DictProperty({})
    on_press = ObjectProperty(None)
    plantilla = DictProperty({
                "all":{
                    'font_size': '20dp',
                    'size_hint': (1, None),
                    'height': '50dp',
                    'type_control': 'text'
                }
        })

    def on_bg_color(self, w, val):
        if "#" in val:
            val = "".join(val)
            self.bg_color = get_color_from_hex(val)
        else:
            self.bg_color = val

    __form_content__ = ObjectProperty(None)

    def __init__(self, **kargs):
        super(Form, self).__init__(**kargs)

    def __clear_model__(self):
        self.model = {}
        self.form_content.clear_widgets()

    def on_model_chage(self, form_control):
        self.model[form_control.name] = unicode(form_control.__text__)

    def hide(self, input):
        self.float_input.focus = False
        ani = Animation(x=self.width*2, duration=0.05)
        ani.start(self.__float_input__)
        self.on_model_chage(input)


    def show_text_input(self, input):
        ani = Animation(x=0, duration=0.05)
        ani.bind(on_complete=self.on_complete)
        self.__float_input__.input = input
        ani.start(self.__float_input__)


    def on_complete(self, ani, w):
        self.float_input.focus = True


    def add_widget(self, widget):
        if len(self.children) < 3:
            super(Form, self).add_widget(widget)
        else:

            if hasattr(widget, 'isFormControl'):
                self.model[widget.name] = widget.text
            height = self.__form_content__.parent.height  + widget.height + dp(25)
            self.__form_content__.parent.height = height
            self.__form_content__.add_widget(widget, 0)


    def add_model(self, model, columns=None, tmpl=None):
        self.__clear_model__()
        self.model = model
        columns = columns if columns else model.keys()
        for k in columns:
            if tmpl and k in tmpl:
                plantilla = self.plantilla.get("all").copy()
                plantilla.update(tmpl[k])
            elif k in self.plantilla:
                plantilla = self.plantilla.get(k).copy()
            else:
                plantilla = self.plantilla.get("all").copy()

            plantilla["name"] = k
            plantilla["text"] = unicode(model[k])
            plantilla["controller"] = self
            if not "label" in plantilla:
                plantilla["label"] = k.title()

            if 'type_control' in plantilla and plantilla['type_control'] != 'text':
                type_control = plantilla['type_control']
                if type_control == 'checkbox':
                    input = CheckBoxControl(model=plantilla)
                else:
                    input = InputTextControl(model=plantilla)

            else:
                input = InputTextControl(model=plantilla)

            self.add_widget(input)

    def form_check(self):
        if self.on_press:
            self.on_press(self.model)
