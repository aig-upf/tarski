

class PddlReader(object):

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        raise RuntimeError("Unimplemented")


class PddlWriter(object):

    def __init__(self, filename):
        self.filename = filename

    def write(self, element):
        raise RuntimeError("Unimplemented")


