import math

def I(x,y) :
    #Takes the Re(z) and the Im(z) and turns it into a complex number(repersented by a string)
    #x is the Re(z) and y is the Im(z)
    #The output is a string in the form x + yi
    if y == 0 :
        z = str(x)
    elif x == 0 :
        if y == 1 :
            z = 'i'
        elif y == -1 :
            z = '-i'
        else :
            z = str(y) + 'i'
    else : 
        if y == 1 :
            z = str(x) + " " + "+" + " " + 'i'
        elif y == -1 :
            z = str(x) + " " + "+" + " " + '-i'
        else :
            z = str(x) + " " + "+" + " " + str(y) + 'i'
    return z

def conj(x,y) :
    #Takes the Re(z) and the Im(z) and turns it into z_bar(repersented by a string)
    #x is the Re(z) and y is the Im(z)
    #The output is a string in the form x + yi
    if y == 0 :
        z = str(x)
    elif x == 0 :
        if y == 1 :
            z = '-i'
        elif y == -1 :
            z = 'i'
        else :
            z = '-' + str(y) + 'i'
    else :
        if y == 1 :
            z = str(x) + " " + "" + " " + '-i'
        elif y == -1 :
            z = str(x) + " " + "" + " " + 'i'
        else :
            if y[0,1] == '-' :
                z = str(x) + " " + "+" + " " + str(y) + 'i'
            else:
                z = str(x) + " " + "+" + " " + "-" + str(y) + 'i'
    return z

def Re(z) :
    #Finds real part of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    sr = str(z)
    if sr[len(sr) - 1] == 'i' :
        for count in range(0, len(sr)) :
            place = sr[count]
            if_e = sr[count - 1]
            if place == '+' :
                if if_e == 'e' :
                    continue
                else :
                    sr2 = sr[0 : count - 1]
                    sr22 = float(sr2)
                    return sr22
        return 0
    else :
        zz = float(z)
        return zz
    
def Im(z) :
    #Finds the imaginary part of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    sr = str(z)
    if sr[len(sr) - 1] == 'i' :
        for count in range(0, len(sr)) :
            place = sr[count]
            if_e = sr[count - 1]
            if place == '+' :
                if if_e == 'e' :
                    continue
                else :
                    sr2 = sr[count + 1 : len(sr) - 1]
                    if sr2 == ' ' :
                        fin = 1
                    elif sr2 == '-' :
                        fin = -1
                    else :
                        fin = float(sr2)
                    return fin
        sr22 = sr[0 : len(sr) - 1]
        if sr22 == '' :
            return float(1)
        elif sr22 == '-' :
            return float(-1)
        else :
            return float(sr22)
    else :
        return 0

def neg(z) :
    #Makes the complex number negitive
    #The input is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    z1 = I(-x,-y)
    return z1
    
def add(z,z1) :
    #Adds two complex numbers
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    x1 = Re(z1)
    y1 = Im(z1)
    u = x + x1
    v = y + y1 
    z2 = I(u,v)
    return z2

def subt(z,z1) :
    #Finds the difference between two complex numbers (z - z1)
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    x1 = Re(z1)
    y1 = Im(z1)
    u = x - x1
    v = y - y1 
    z2 = I(u,v)
    return z2

def multi(z,z1) :
    #Multiplys two complex numbers
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    x1 = Re(z1)
    y1 = Im(z1)
    u = x * x1 - y * y1
    v = x1 * y + x * y1 
    z2 = I(u,v)
    return z2

def sqr(z) :
    #Squares a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    u = x ** 2 - y ** 2
    v = 2 * x * y
    z1 = I(u,v)
    return z1

def Arg(z) :
    #Finds the principal argument of a complex number
    #The input is a string in the form x + yi
    #The output is in radians
    x = Re(z)
    y = Im(z)
    t = math.atan2(y,x)
    return t

def arg(z) :
    #Finds the argument of a complex number
    #The input is a string in the form x + yi
    #The output is in radians
    x = Re(z)
    y = Im(z)
    t = math.atan(y/x)
    return t

def mod(z) :
    #Find the magnitude/norm/modulus of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    z1 = math.sqrt(x ** 2 + y ** 2)
    return z1

def Log(z) :
    #Finds the principal log of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    u = math.log(mod(z))
    v = Arg(z)
    z1 = I(u,v)
    return z1

def log(z) :
    #Finds the log of a complex numjber
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    u = math.log(mod(z))
    v = arg(z)
    z1 = I(u,v)
    return z1

def eul(r,t) :
    #r is the radius and t is the angle in radians(they must be real)
    #The output is a string in the form x + yi
    u = float(r * math.cos(t))
    v = float(r * math.sin(t))
    z1 = I(u,v)
    return z1

def eul_c(r,z) :
    #r is the radius and t is the angle in radians(they can be complex)
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    u = float(math.exp(-y) * math.cos(x))
    v = float(math.exp(-y) * math.sin(x))
    z1 = I(u,v)
    z2 = multi(r,z1)
    return z2

def power(z,p) :
    #Puts a complex number to the power of a number(it can be complex)
    #z is a string in the form x + yi and p is the power(it can be complex)
    #The output is a string in the form x + yi
    r = mod(z)
    t = Arg(z)
    pow = multi(t,p)
    z1 = eul_c(r, pow)
    return z1

def div(z,z1) :
    #Divides a complex number by an other complex number (z/z1)
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    r = mod(z) / mod(z1)
    t = Arg(z) - Arg(z1)
    z2 = eul(r,t)
    return z2

def sin(z) :
    #Finds the sine of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    u = eul(math.exp(-y), x)
    v = eul(math.exp(-y), -x)
    s = subt(u,v)
    z1 = multi(s, '-0.5i')
    return z1

def csc(z) :
    #Finds the cosecant of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    u = sin(z)
    z1 = div(1,u)
    return z1

def cos(z) :
    #Finds the cosine of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    u = eul(math.exp(-y), x)
    v = eul(math.exp(-y), -x)
    s = add(u,v)
    z1 = multi(s, '0.5')
    return z1

def sec(z) :
    #Finds the secant of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    u = cos(z)
    z1 = div(1,u)
    return z1

def tan(z) :
    #Finds the tangent of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    s = sin(z)
    c = cos(z)
    z1 = div(s,c)
    return z1

def cot(z) :
    #Finds the cotangent of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    u = tan(z)
    z1 = div(1,u)
    return z1

def sinh(z) :
    #Finds the hyperbolic sine of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    u = eul(math.exp(-x), y)
    v = eul(math.exp(-x), -y)
    s = subt(u,v)
    z1 = multi(s, '0.5')
    return z1

def csch(z) :
    #Finds the hyperbolic cosecant of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    u = sinh(z)
    z1 = div(1,u)
    return z1

def cosh(z) :
    #Finds the hyperbolic cosine of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    u = eul(math.exp(-x), y)
    v = eul(math.exp(-x), -y)
    s = add(u,v)
    z1 = multi(s, '0.5')
    return z1

def sech(z) :
    #Finds the hyperbolic secant of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    u = cosh(z)
    z1 = div(1,u)
    return z1

def tanh(z) :
    #Finds the hyperbolic tangent of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    s = sinh(z)
    c = cosh(z)
    z1 = div(s,c)
    return z1

def coth(z) :
    #Finds the hyperbolic cotangent of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    u = tan(z)
    z1 = div(1,u)
    return z1
