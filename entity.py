# encoding: utf-8

from intids import IntIds

class Object:

    name = ''
    parent = None
    object_type = 'Object'
    schemas = ()

    def move_to(self, parent, new_name=None):
        new_name = new_name or self.name
        parent[new_name] = self

    def copy_to(self, parent, new_name=None):
        new_name = new_name or self.name
        parent[new_name] = copy(self)
        
class Item(Object):

    content_type = ''
    data = ''
    
    def set_data(self, data):
        self.data = data
        
    def get_data(self):
        return self.data

class Container(Object):

    _order = (,)
    _data = {}
    
    def __init__(self):
        self._data = {}
        self.order = (,)

    def set_order(self, order):
        self._order = order

    def keys(self):
        for key in self._order:
            yield key
            
        for key in _data:
            if key not in self._order:
                yield key

    def values(self):
        return _data.values()


    def object_path(self, obj):
        return path
        
    def object_by_path(self, path):
        return obj

class Root(Container):

    _intids = None

    def __init__(self):
        Container.__init__(self)
        self._intids = IntIds()
        self._recycle_box = RecycleBox()

    def get_intid_registry(self):
        return self._intids
    
    def get_recycle_box(self): 
        return self._recycle_box
