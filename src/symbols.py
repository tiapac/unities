from fractions import Fraction

class symbol:
    power = "^"
    plus  = "+"
    minus = "-"
    mult  = r"\cdot"
    space = r"\,"

    def __init__(self, string, subsymbols = set):

        self._string    = string
        self._base      = self.__base(string)
        self._exp       = self.__exp(string)
        self.subsymbols = subsymbols
        if self._exp == 0: self._base = ""
        pass
    
    @staticmethod
    def __tofloat(value):
        if "/" in value:
            num, den = value.split("/")
            return float(num)/float(den)
        else:
            return float(value)
    @property
    def string(self):
        res =  self._base
        value = self.__tofloat(self.exp)
        if abs(value)>1: 
            res += self.power+"{%s}"%self.exp
        elif abs(self.__tofloat(self.exp))<1:
            res += self.power+"{%s}"%self.exp
        else: 
            match value:
                case 1|1.0:
                    pass
                case -1|-1.0:
                    res += self.power+"{%s}"%self.exp
                case 0|0.0:
                    res = "1"

        return res
    @property
    def base(self):
        return self._base
    @property
    def exp(self):
        return self._exp
    
    
    def __base(self,string)-> str:
        return string if not self.power in string else string.split(self.power, maxsplit=1)[0]
    def __exp(self,string)-> int:
        
        string = "1" if not self.power in string else (string.split(self.power, maxsplit=1)[1])
        string.replace("{","(").replace("}",")")
        string = string.strip("(").strip(")")
        return  string

    def __str__(self):
        return self.string
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        if isinstance(other, symbol):
            return (self.base == other.base) and (self.exp == other.exp)
        else:
            raise TypeError("You can only compare symbols with symbols")
        pass
    
    def __pow__(self, other):
    
        if isinstance(other, int|str|float|Fraction):
            try:
                other = float(other)
            except:
                try:
                    other = Fraction(other)
                except Exception as e:
                    
                    raise TypeError("Exponent must be an integer or a fraction:", e)
            match other:
                case 1|1.0:
                    return self
                case 0|0.0: 
                    return symbol("")
                case _: 
                    
                    exp = str(Fraction(float(self.__tofloat(self.exp))*other))
                    if exp == 1 or exp == 0: 
                        return self**exp
                    else:
                        return symbol(self.base+symbol.power+exp)
                    



    def __mul__(self, other):
        if isinstance(other, symbol):
            if self.base == other.base:
                res = str(Fraction(self.__tofloat(self.exp)+self.__tofloat(other.exp)))
                return symbol(self.base
                              +symbol.power
                              +res)
            else:
                return symbols(self, other)# symbol("{self.base}^{self.exp}"+"{other.base}^{other.exp}")
                 
        elif isinstance(other, str):
            other = symbol(other)
            return self.__mul__(self, other)  
        else:
            raise TypeError("You can only multiply symbols with symbols or symbols with strings")

    def __truediv__(self, other):
        return self.__mul__(other**(-1))
    def __hash__(self):
        return hash((self.base, self.exp))




class symbols: 
    def __init__(self, *args):
        done = False
        for arg in args: 
            if isinstance(arg, symbols):
                assert len(args) == 1

                self.symbols = arg.symbols
                done = True
                break
        if not done:
            tmp = list(args)
            for i, arg in enumerate(args):
                if isinstance(arg, str): tmp[i] = symbol(arg)
            self.symbols = tmp
        pass
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return "".join([str(sym)+sym.space for sym in self.symbols]).strip(symbol.space)
    def __pow__(self, other):
        
        if isinstance(other, int):            
            return symbols(*(sym**other for sym in self.symbols))
        else:
            raise TypeError("You can only raise symbols to an integer power")
    def __contains__(self, item):
        if isinstance(item, symbol):
            return any([item == sym for sym in self.symbols])
        else:
            raise TypeError("You can only check containment with symbols")

    def __iter__(self):
        return iter(self.symbols)
    def __truediv__(self, other):
        return self.__mul__(other**(-1))
    def __mul__(self, other):
        if isinstance(other, symbols):
            tmp = [s for s in self.symbols]
            for sym in other:
                found = False
                for i, mysim in enumerate(tmp):
                    if mysim.base == sym.base:
                        tmp[i] = mysim * sym
                        found = True
                        break
                if not found:
                    tmp.append(sym)
            return symbols(*tmp)
        elif isinstance(other, symbol):
            tmp = list(self.symbols)
            found = False
            for i, sym in enumerate(tmp):
                if sym.base == other.base:
                    tmp[i] = sym * other
                    found = True
                    break
            if not found:
                tmp.append(other)
            return symbols(*tmp)
        else:
            raise TypeError("You can only multiply symbols with symbols or symbols with symbols")
    

