# Dimensional analysis

import string

class DimensionsError(Exception):
    pass

class Dimensions(object):
    def __init__(self,d):
        if isinstance(d,int):
            self.dimensions = {}
        elif isinstance(d,str):
            self.dimensions = self.detect_dimensions(d)
        else:
            raise TypeError("d must be an integer or a string")
        clean_0_dimensions(self)

    def detect_dimensions(self,d):
        dimensions = {}
        d.replace(" ","")
        last = 0
        while last <= len(d)-1:
            try:
                dimension = d[d.index("[",last)+1:d.index("]",last)]
            except ValueError:
                break
            last = d.index("]",last)
            if last < len(d)-2 and d[last+1] == "^":
                last+=1
                count = ""
                last_char = d[last+1+len(count)]
                while last_char in string.digits+"-":
                    count += last_char
                    if last+1+len(count) > len(d)-1:
                        last+=1
                        break
                    last_char = d[last+1+len(count)]
                    last += 1
                if count != "":
                    count = int(count)
                else:
                    raise ValueError("Index is not valid")
            else:
                count = 1
            if dimension not in dimensions:
                dimensions[dimension] = count
            else:
                dimensions[dimension] += count
            last += 1
        return dimensions

    def __add__(self,x):
        if not isinstance(x,Dimensions):
            try:
                x = Dimensions(x)
            except TypeError:
                raise TypeError("Can only add/subtract "+__name__+".Dimensions compatible objects")
        if not self.dimensions == x.dimensions:
            raise DimensionsError("Dimensions do not match, so cannot be added/subtracted")
        return self

    __sub__ = __add__

    def __mul__(self,x):
        if not isinstance(x,Dimensions):
            try:
                x = Dimensions(x)
            except TypeError:
                raise TypeError("Can only multiply "+__name__+".Dimensions compatible objects")

        new = Dimensions("")
        for d in self.dimensions:
            new.dimensions[d] = self.dimensions[d]
        for d in x.dimensions:
            if d in new.dimensions:
                new.dimensions[d] += x.dimensions[d]
            else:
                new.dimensions[d] = x.dimensions[d]
        clean_0_dimensions(new)
        return new

    def __truediv__(self,x):
        if not isinstance(x,Dimensions):
            try:
                x = Dimensions(x)
            except TypeError:
                raise TypeError("Can only divide "+__name__+".Dimensions compatible objects")

        new = Dimensions("")
        for d in self.dimensions:
            new.dimensions[d] = self.dimensions[d]
        for d in x.dimensions:
            if d in new.dimensions:
                new.dimensions[d] -= x.dimensions[d]
            else:
                new.dimensions[d] = -(x.dimensions[d])
        clean_0_dimensions(new)
        return new

    __floordiv__ = __truediv__
    __div__ = __truediv__

    def __pow__(self,i):
        new = Dimensions("")
        
        for d in self.dimensions:
            new.dimensions[d] = self.dimensions[d] * i

        clean_0_dimensions(new)
        return new

    def __eq__(self,x):
        if not isinstance(x,Dimensions):
            raise TypeError("Can only compare "+__name__+".Dimensions objects")

        return self.dimensions == x.dimensions

    def __str__(self):
        output = ""
        for d,v in self.dimensions.items():
            output += "[{d}]".format(d=d)
            if v != 1:
                output += "^{v}".format(v=v)
        return output

    def __repr__(self):
        return __name__+".Dimensions(\""+str(self)+"\")"

def function(d):
    if isinstance(d,str):
        d = Dimensions(d)
    elif isinstance(d,Dimensions):
        pass
    else:
        raise TypeError

    if d.dimensions != {}:
        raise DimensionalError("Must be dimensionless to put through a function")
    else:
        return d

def clean_0_dimensions(dim):
    for d,v in list(dim.dimensions.items()):
        if v == 0:
            dim.dimensions.pop(d)

sin = function
cos = function
tan = function
exp = function

LENGTH = Dimensions("[L]")
MASS = Dimensions("[M]")
CURRENT = Dimensions("[I]")
TEMPERATURE = Dimensions("[\u03B8]")
TIME = Dimensions("[T]")
LIGHT_INTENSITY = Dimensions("[J]")

ACCELERATION = LENGTH * TIME**-2
VELOCITY = LENGTH * TIME**-1
FORCE = MASS * ACCELERATION
MOMENTUM = MASS * VELOCITY
CHARGE = CURRENT * TIME
ENERGY = FORCE * LENGTH
POTENTIAL_DIFFERENCE = ENERGY / CHARGE
VOLTS = POTENTIAL_DIFFERENCE
RESISTANCE = POTENTIAL_DIFFERENCE / CURRENT
AREA = LENGTH**2
VOLUME = LENGTH**3
DENSITY = MASS / VOLUME
RESISTIVITY = (RESISTANCE * AREA)/LENGTH
POWER = ENERGY / TIME
PRESSURE = FORCE / AREA
CAPACITANCE = CHARGE / POTENTIAL_DIFFERENCE
FLUX_DENSITY = FORCE / (CURRENT * LENGTH)
MAGNETIC_FLUX = FLUX_DENSITY * AREA
BIG_G = FORCE * LENGTH**2 * MASS**-2
