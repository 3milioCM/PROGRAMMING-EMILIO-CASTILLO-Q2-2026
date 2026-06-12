import math

# input
a = (input("write the left endpoint of the interval: "))
b = (input("write the right endpoint of the interval: "))
f_x = (input("write the function to integrate: "))
method = input("Write the integration method (LRM/RRM/MRM/TRAP)")

#process
if "pi" in a:
    a = eval(a.replace("pi", str(math.pi)))
else:
    a = float(a)

if "pi" in b:
    b = eval(b.replace("pi", str(math.pi)))
else:
    b = float(b)
    
n = 1000
h = (b - a) / n
area = 0.0
constant = 0
shift = 0
variable = 0
    
if method == "RRM":
    shift = 1
    
if method == "MRM":
    constant = h/2
    
if method == "TRAP":
    variable = 1
    f_0 = f_x.replace("x", str(a))
    area += (h/2) * eval(f_0)
    
    for i in range(variable, n):
        xi = a + i * h
        f_xi = f_x.replace("x", str(xi))
        area += (h / 2) * 2 * eval(f_xi)
        
    f_xn = f_x.replace("x", str(b))
    area += (h / 2) * eval(f_0)
    
else:
    for i in range(shift, n + shift):
        xi = a + i * h
        height = f_x.replace("x", str(xi + constant))
        area += h * eval(height)
    
# output
print(f"the integration of {f_x} is {area}")