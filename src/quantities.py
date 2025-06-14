from .symbols import symbols
from sys import stdout 
from fractions import Fraction

class quantity:
    """
    A class to represent a physical quantity with a value and units.
    Attributes
    ----------
    value : tuple
        A tuple containing the value and the unit of the quantity.
    Methods
    -------
    __init__(value: tuple):
        Initializes the quantity with a value and units.
    __repr__():
        Returns the string representation of the quantity.
    __str__():
        Returns the formatted string representation of the quantity.
    __mul__(other):
        Multiplies the quantity with another quantity, float, int, or symbol.
    __truediv__(other):
        Divides the quantity by another quantity.
    __pow__(other):
        Raises the quantity to the power of another quantity or value.
    quantify(value, unit):
        Static method to create a new quantity with a given value and unit.
    value:
        Returns the value of the quantity.
    v:
        Returns the value of the quantity (alias for value).
    units:
        Returns the units of the quantity.
    u:
        Returns the units of the quantity (alias for units).
    """
    def __init__(self, value:tuple):
        self._value = value[0]
        self._units = symbols(value[1])
        pass 
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        if False:  # stdout.isatty(): 
            u_str = str(self.u).replace('\\,', ' ').replace('{', '(').replace('}', ')')
            return f"{self.v} {u_str}"
        else:
            return rf"${self.v}\,${str(self.u)}"
            
    def __mul__(self, other):
        if isinstance(other, quantity):
            return self.quantify(self.value * other.value, self.units * other.units)
        elif isinstance(other, (float, int)):
            return self.quantify(self.value * other, self.units)
        elif isinstance(other, symbols):
            return self.quantify(self.value, self.units * other)
        else:
            raise TypeError(f"Operation with unkown type {other}. Must be float|int or quantity.")

    @staticmethod
    def quantify(value, unit):
        return quantity((value, symbols(unit)))
    
    def __add__(self, other):
        if isinstance(other, (float, int)):
            return self.quantify(self.value + other, self.units)
        elif isinstance(other, quantity):
            assert self.units == other.units, "Cannot sum/sub numbers with different units of measure."
            return self.quantify(self.value + other.value, self.units)
        else:
            raise TypeError(f"Operation with unkown type {other}. Must be float|int or quantity.")
    def __truediv__(self, other):
        return self.__mul__(other**(-1))
    def __neg__(self):
        return self.quantify(-self.value, self.units)
    
    def __sub__(self,other): 
        return self.__add__(-other)
    
    def __pow__(self, other):
        if isinstance(other, (float, int, Fraction)) or (isinstance(other, str)):
            if isinstance(other, str):
                other = Fraction(other)
                other = other.numerator / other.denominator
            other_v = other
            other_u = 1
        elif isinstance(other, quantity):
            other_v = other.value
            other_u = other.value
        else:
            raise TypeError(f"Operation with unkown type {other}. Must be float|int or quantity.")
        return self.quantify(self.value ** other_v, self.units ** other_u)
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
