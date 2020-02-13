# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, info, prevRoom = None):
        self.name = name
        self.info = info
        self.prevRoom = prevRoom

        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
