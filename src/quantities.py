from .symbols import symbols
from sys import stdout 


class quantity:
    def __init__(self, value:tuple):
        self._value = value[0]
        self._units = symbols(value[1])
        pass 
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        if False:#stdout.isatty():
            return f"{self.v} [{str(self.u).replace(r'\,', ' ').replace('{', '(').replace('}', ')')}]"
        else:
          
            return rf"{self.v}\,[{str(self.u)}]"
            
    def __mul__(self, other):
        if isinstance(other, quantity):
            return self.quantify(self.value*other.value, self.units*other.units)
        elif isinstance(other, float|int):
            return self.quantify(self.value*other, self.units)
        elif isinstance(other, symbols):
            return self.quantify(self.value, self.units*other)
    @staticmethod
    def quantify(value, unit):
        return quantity((value, symbols(unit)))
    def __truediv__(self, other):
        return self.__mul__(other**(-1))
    
    def __pow__(self, other):
        other_u = other if not isinstance(other,quantity) else other.value
        
        return self.quantify(self.value**other, self.units**other_u)
    
    @property
    def value(self):
        return self._value
    @property
    def v(self):
        return self.value
    @property
    def units(self):
        return self._units
    @property
    def u(self):
        return self.units
