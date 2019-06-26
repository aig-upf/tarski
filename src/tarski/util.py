"""
    Some basic utility methods.
"""
from collections import OrderedDict

from .errors import DuplicateDefinition


class IndexDictionary:
    """ A basic indexing object that assigns consecutive indexes to the indexed objects. """
    def __init__(self, elements=None):
        self.data = OrderedDict()
        self.objects = []
        _ = [self.add(element) for element in (elements or [])]

    def get_index(self, key):
        return self.data[key]

    def get_object(self, index):
        return self.objects[index]

    def add(self, obj):
        if obj in self.data:
            raise DuplicateDefinition(obj, self.data[obj])
        self.data[obj] = len(self.data)
        self.objects.append(obj)

    def dump(self):
        return [str(o) for o in self.data.keys()]

    def __str__(self):
        return ','.join('{}: {}'.format(idx, o) for o, idx in self.data.items())

    __repr__ = __str__

    def __iter__(self):
        return self.data.__iter__()

    def enumerate(self):
        """ Iterate over all (ordered) pairs of the form idx, o, where idx is the index of object 'o' """
        return ((idx, o) for o, idx in self.data.items())

    def __contains__(self, k):
        return k in self.data

    def __len__(self):
        return len(self.data)
