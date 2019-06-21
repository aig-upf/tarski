
import os

_CURRENT_DIR_ = os.path.dirname(os.path.realpath(__file__))


def load_tpl(name):
    with open(os.path.join(_CURRENT_DIR_, "templates", name), 'r') as file:
        return file.read()
