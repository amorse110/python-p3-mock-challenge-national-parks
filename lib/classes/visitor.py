from classes.trip import Trip


class Visitor:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("Visitor name must be a string 1-15 characters in length")

    def trips(self):
        return 

    def national_parks(self):
        pass
