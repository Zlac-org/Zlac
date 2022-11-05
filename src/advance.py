# advance.py is a part of Zlac and is registered under the same license : Apache License, Version 2.0
# Advanced part of Zlac
# Copyright 2022 Zlac-org

try:
    import math
    # Only dependency of advance.py is math module
except ImportError:
    print('\n[ERROR] Failed importing modules. Make sure the venv is activated or try running ''pip install recquirements.txt''')    

def area_rectangle(b: float,l: float):
    return b*l

def area_sq(a : float,b: None):
    return a**2

def area_tri(b: float, h:float):
    return (h*b)/2   

def per_rectangle(b: float , l: float):
    return 2*(l+b)  

def per_sq(a: float, b: None):
    return 4*a

def area_circle(r : float,n : None):
    return math.pi*r*r 

def per_circle(r : float,n:None):
    return 2*math.pi*r 

def pi_dis(x:None,y:None):
    return math.pi

def pim(x:None,y:float):
    if y == None:
        return math.pi
    else:

        return math.pi*y

def pia(x:None,y:float):
    if y == None:
        return math.pi
    else:

        return math.pi+y

def pis(x:None,y:float):
    if y == None:
        return math.pi
    else:

        return math.pi-y

def pid(x:None,y:float):
    if y == None:
        return math.pi
    else:
        
        return math.pi/y

def log(x:float, y:float):
    return math.log(x,y) 

def ln(x:None, y: float):
    return math.log(y)

def sqr(x:None, y:float):
    return math.sqrt(y)

def perc(x:float, y:float):
    # x is the part and y the whole
    if y == None:
        y = 100
        return x/y
    else:
        return 100 * x/y

def facto(x:float, y:None):
    i = 1
    prod = 1
    while i <= x:
        if x == 0:
            return 1.0
        else:
            prod = prod * i
            i = i+1
    return prod

    

def checkifint(str):
    if str[0] in ('-', '+'):
        return str[1:].isdigit()
    return str.isdigit()
    

