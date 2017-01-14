from garbage import Garbage


class PlasticGarbage(Garbage):
    def __init__(self, name, is_clean=False):
        super().__init__(name)
        self.is_clean = is_clean

    def clean(self):
        self.is_clean = True
