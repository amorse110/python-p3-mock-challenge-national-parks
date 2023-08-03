
class Trip:
    
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor
#MUST BE OF TYPE VISITOR
    @visitor.setter
    def visitor(self, visitor):
        from classes.visitor import Visitor

        if type(visitor) == Visitor:
            self._visitor = visitor
        else:
            raise Exception
    
    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        from classes.national_park import NationalPark
        
        if type(national_park) == NationalPark:
            self._national_park = national_park
        else:
            raise Exception