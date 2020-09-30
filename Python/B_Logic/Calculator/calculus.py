
import sympy as sym

def Derivitive(function):
    x = sym.Symbol('x')
    function = function.strip("")
    print(function)
    derivitive = sym.diff(function)
    print(derivitive)