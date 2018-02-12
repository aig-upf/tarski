

class JsonReader(object):

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        raise NotImplementedError()


class JsonWriter(object):

    def __init__(self, filename):
        self.filename = filename

    def write(self, element):
        raise NotImplementedError()
