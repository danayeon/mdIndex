class File():
    def __init__(self, path):
        self.path = path

    def read(self):
        return open(self.path)

    def write(self):
        return open(self.path, mode='w')
