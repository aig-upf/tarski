"""
    Some basic utility methods.
"""
from collections import OrderedDict


class UninitializedAttribute:
    def __init__(self, name):
        object.__setattr__(self, 'name', name)

    def _raise_error(self, *args, **kwargs):
        # pylint: disable=unused-argument
        raise AttributeError("Attempt to access object '{}', which has not yet been initialized. "
                             "Revise the application workflow.".format(object.__getattribute__(self, 'name')))

    __getattr__ = _raise_error
    __setattr__ = _raise_error
    __delattr__ = _raise_error
    __len__ = _raise_error
    __getitem__ = _raise_error
    __setitem__ = _raise_error
    __delitem__ = _raise_error
    __iter__ = _raise_error
    __contains__ = _raise_error


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
            raise RuntimeError("Duplicate element '{}'".format(obj))
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
