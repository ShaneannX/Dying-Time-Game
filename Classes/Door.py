class Door:
    def __init__(self, position,is_open = False):
        self.position = position
        self.is_open = is_open

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False