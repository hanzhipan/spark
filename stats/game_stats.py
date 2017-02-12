
class GameStats(object):
    def __init__(self):
        pass

    def build(self, data):
        setattr(self, data[1], data[3])

