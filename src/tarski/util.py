"""
    Some basic utility methods.
"""
from collections import OrderedDict


class DuplicateElementError(Exception):
    pass


class IndexDictionary:
    """
    A very basic indexing mechanism object that assigns consecutive indexes to the indexed objects.
    """

    def __init__(self, elements=None):
        self.data = OrderedDict()
        self.objects = []
        elements = [] if elements is None else elements
        for element in elements:
            self.add(element)

    def get_index(self, key):
        return self.data[key]

    def get_object(self, index):
        return self.objects[index]

    def add(self, obj):
        if obj in self.data:
            raise DuplicateElementError("Duplicate element '{}'".format(obj))
        self.data[obj] = len(self.data)
        self.objects.append(obj)

    def dump(self):
        return [str(o) for o in self.data.keys()]

    def __str__(self):
        return ','.join('{}: {}'.format(k, o) for k, o in self.data.items())

    __repr__ = __str__

    def __iter__(self):
        return self.data.__iter__()

    def __contains__(self, k):
        return k in self.data

    def __len__(self):
        return len(self.data)
