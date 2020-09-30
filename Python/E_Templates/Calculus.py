##Calculate a derivitave
import sympy as sym
x = sym.Symbol('x')
function = x ** 4 + 7 * x ** 3 + 8
derivitive = sym.diff(function)
print(derivitive)