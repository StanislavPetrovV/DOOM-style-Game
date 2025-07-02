class Switch:
    def __init__(self, x, y, is_active=False):
        self.x = x
        self.y = y
        self.is_active = is_active

    def activate(self):
        self.is_active = True