
class IIndexer:

    def __init__(self, obj):
        pass

    def index(self, recursive=False):
        pass

    def unindex(self, recursive=False):
        pass

    def reindex(self, fields=[], recursive=False):
        pass

    def index_file_content(self, recursive=False):
        pass

class QuerySet:

    def anyof(self): pass

    def sum(self): pass
