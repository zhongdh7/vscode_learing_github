print("hello world")
a=10
b=20
print(a+b)
#计算定积分
import sympy as sp
x = sp.symbols('x')
f = sp.sin(x)
integral = sp.integrate(f, (x, 0, sp.pi))
print("this is the integral of sin(x) from 0 to pi:", integral)
for i in range(5):
    print(i)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print("the factorial of 5 is:", factorial(5))

