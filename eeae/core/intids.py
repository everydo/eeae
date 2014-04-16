# encoding: utf-8

class IntIds:

    _id_obj = {}
    _obj_id = {}
    
    def __init__(self):
        self._id_obj = {}
        self._obj_id = {}
        
    def get_id(self, obj):
        return self._obj_id[obj]
        
    def get_object(self, id):
        return self._id_obj[id]
