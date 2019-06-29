# @Author: Manuel Rodriguez <valle>
# @Date:   2019-05-05T00:52:35+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-05-05T20:00:27+02:00
# @License: Apache License v2.0

from kivy.properties import StringProperty, ListProperty
import json

class JsonObjects():

    db = StringProperty()
    tb = StringProperty()
    fields = ListProperty([])

    def __init__(self, db, tb, **obj):
        self.db = db
        self.tb = tb
        for k, v in obj.items():
            self.fields.append(k)
            setattr(self, k, v)


    def add_item(self, **item):
        for k, v in item.items():
            setattr(self, k, v)

    def __obj_to_dict__(self):
        json_obj = {}
        for k in self.fields:
            json_obj[k] = getattr(self, k)
        return json_obj

    def get_add(self):
        return {
           "db": db,
           "tb": tb,
           "op": "add",
           "obj": json.dumps(self.__obj_to_dict__())
        }

    def get_delete(self, db, tb, **condition):
        return {
           "db": self.db,
           "tb": self.tb,
           "op": "delete",
           "args": json.dumps(condition)
        }

    def get_filter(self, **condition):
        return {
           "db": self.db,
           "tb": self.tb,
           "op": "filter",
           "args": json.dumps(condition)
        }

    def get_update(self, **condition):
        return {
           "db": self.db,
           "tb": self.tb,
           "op": "update",
           "args": json.dumps(condition),
           "obj": json.dumps(self.__obj_to_dict__())
        }
