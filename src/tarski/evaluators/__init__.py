from . import simple

factory_entries = {'simple': simple.evaluate}


def get_entry_point(key):
    return factory_entries[key]
