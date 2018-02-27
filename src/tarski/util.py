"""
    Some basic utility methods.
"""
import os
import re
import unicodedata
from collections import OrderedDict


def normalize(name):
    slug = unicodedata.normalize('NFKD', name)
    slug = slug.encode('ascii', 'ignore').lower()
    slug = re.sub(r'[^a-z0-9]+', '_', slug.decode()).strip('-')
    slug = re.sub(r'[-]+', '_', slug)
    return slug


def normalize_and_camelcase(name):
    return to_camelcase(normalize(name))


def normalize_action_name(name):
        return normalize_and_camelcase(name) + 'Action'


def to_camelcase(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


def load_file(filename):
    with open(filename, 'r') as f:
        c = f.read()
    return c


def load_file_safely(filename):
    if not os.path.isfile(filename):
        return None

    with open(filename, 'r') as f:
        c = f.read()
    return c


def bool_string(value):
    return 'true' if value else 'false'


def is_external(symbol):
    return symbol[0] == '@'

def has_unbounded_arity(symbol) :
    return symbol[0:2] == '@@'


class UninitializedAttribute(object):
    def __init__(self, name):
        object.__setattr__(self, 'name', name)

    def _raise_error(self, *args, **kwargs):
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


class IndexDictionary(object):
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
