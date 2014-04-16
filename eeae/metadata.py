# encoding: utf-8

class IMetadata:

    def __init__(self, obj):
        self.obj = obj
        if not hasattr(obj, '_md'):
            obj._md = {}
        if not hasattr(obj, '_mdset'):
            obj._mdset = {'_settings':{}}

    def update(self, data):
        return self.obj._md.update(data)

    def new_mdset(self, name):
        self.obj._mdset[name] = {}

    def remove_mdset(self, name):
        del self.obj._mdset[name]

    def get_mdset(self, name):
        return self.obj._mdset[name]

    def set_mdset(self, name, data):
        self.obj._mdset[name] = data

    def update_mdset(self, name, data):
        self.obj._mdset[name].update(data)

    def list_mdsets(self):
        return self._mdset.keys()

    def get_setting(self, name):
        return self._mdset['_settings'][name]

    def set_setting(self, name, value):
        self._mdset['_settings'][name] = value
