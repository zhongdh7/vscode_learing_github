print("hello world")
a=10
b=20
print(a+b)
#计算定积分
import sympy as sp
x = sp.symbols('x')
f = sp.sin(x)
integral = sp.integrate(f, (x, 0, sp.pi))
print(integral)
