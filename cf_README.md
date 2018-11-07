# cf.I(x,y)
Takes the Real(x) and Imaginary(y) parts of a complex number and puts it in the form of x + yi. 
The input is two floats and it returns a string.

# cf.conj(x,y)
Takes the Real(x) and Imaginary(y) parts of a complex number and puts it in the form of x + -yi. 
The input is two floats and it returns a string.

# cf.Re(z)
Returns the Real part of a complex number.
The input is a string and it returns a float.

# cf.Im(z)
Returns the Imaginary part of a complex number.
The input is a string and it returns a float.

# cf.neg(z)
Returns the negative of a complex number in the form of -x + -yi.
The input is a string and it returns a string.

# cf.add(z,z1)
Returns the addition of two complex numbers in the form of x + yi.
The input is two strings and it returns a string.

# cf.subt(z,z1)
Returns the subtraction of two complex numbers in the form of x + yi. (z - z1)
The input is two strings and it returns a string.

# cf.multi(z,z1)
Returns the product of two complex numbers in the form of x + yi. 
The input is two strings and it returns a string.

# cf.sqr(z)
Returns the square of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.Arg(z)
Returns the principal argument of a complex number in radians. 
The input is a string and it returns a float.

# cf.arg(z)
Returns the argument of a complex number in radians. 
The input is a string and it returns a float.

# cf.mod(z)
Returns the norm/magnitude/modulus of a complex number. 
The input is a string and it returns a float.

# cf.Log(z)
Returns the principal logarithm of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.log(z)
Returns the logarithm of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.eul(r,t)
Takes a input in polar form (radius,angle(radians)) and returns a complex number in the form of x + yi.
The input is two floats and it returns a string.

# cf.eul_c(r,z)
Takes a input in the form of (r,z) and returns a complex number in the form of x + yi. (r*e**(z*i))
The input is two strings and it returns a string.

# cf.power(z,p)
Returns the complex number to the power of complex number in the form of x + yi. (z ** p)
The input is two strings and it returns a string.

# cf.div(z,z1)
Returns the a complex number divied by complex number in the form of x + yi. 
The input is two strings and it returns a string.

# cf.sin(z)
Returns the sine of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.csc(z)
Returns the cosecant of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.cos(z)
Returns the cosine of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.sec(z)
Returns the secant of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.tan(z)
Returns the tangent of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.cot(z)
Returns the cotangent of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.sinh(z)
Returns the hyperbolic sine of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.csch(z)
Returns the hyperbolic cosecant of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.cosh(z)
Returns the hyperbolic cosine of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.sech(z)
Returns the hyperbolic secant of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.tanh(z)
Returns the hyperbolic tangent of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.coth(z)
Returns the hyperbolic cotangent of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.gamma(z)
Returns the euler gamma of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.zeta(z)
Returns the Riemann Zeta function of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.eta(z)
Returns the Dirichlet Eta function of a complex number in the form of x + yi. 
The input is a string and it returns a string.

# cf.F(z,n)
Returns the polylogarithm of a complex number in the form of x + yi. (sum of (z**(k))/(k**(n))
The input is two strings and it returns a string.

# cf.siegel(t)
Returns the Riemann-Siegel theta function of a real number. 
The input is a float and it returns a float.

# cf.Z(t)
Returns the Riemann-Siegel Z function of a real number in the form of x + yi. 
The input is a float and it returns a string.

# cf.B(n)
Returns the bernoulli numbers in form of x + yi.
The input is a string and it returns a string.

# cf.lamba(z)
Returns the Dirichlet Lamba function in form of x + yi.
The input is a string and it returns a string.

# cf.beta(z)
Returns the Dirichlet Beta function in form of x + yi.
The input is a string and it returns a string.

# cf.lerch(z,s,a)
Returns the Lerch Transcendent in form of x + yi.
The input are strings and it returns a string.

# cf.totient(n) 
Returns the totient of a number.
The input is a positive integer and it returns integer.

# cf.totient_num(n)
Returns the totative of a number.
The input is a positive integer and it returns list.

# cf.div_sig(k,n)
Returns the Divisor function of a number.
The input are positive integers and it returns integer.

# cf.divisors(n)
Returns the divisors of a number.
The input is a positive integer and it returns list.

# cf.is_prime(n)
Returns true if the number is a prime and false if not.
The input is a positive integer and it returns string.

# cf.tau(n)
Returns the Tau function of a number.
The input is a positive integer and it returns integer.

# cf.N(p)
Reurns the group of units in the ring of integers modulo p.
The input is a positive integer and it returns integer.

# cf.X(k,j,n)
Returns the Dirichlet Characters of a number. ( mod k, index j)
The input are positive integers and it returns integer.

# cf.L(k,s,X1)
Returns the Dirichlet L function in form of x + yi. ( mod k, index X1)
The input are positive integers(k,X1) and a string(s) and it returns string.
