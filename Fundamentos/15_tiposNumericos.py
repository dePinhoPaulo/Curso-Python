#Tipos numericos
print(dir(int))
print(dir(float))

a = 5
b = 2.5
print(a/b)
print(a+b)
print(a*b)
print(a-b)

print(b.is_integer())
print((5.0).is_integer())

print(int.__add__(2,3))

print((-2).__abs__())
print((-2.5).__abs__())

print(1.1 + 2.2)
from decimal import Decimal, getcontext
print(Decimal(1)/Decimal(7))

getcontext().prec = 4
print(Decimal(1)/Decimal(7))
print(Decimal.max(Decimal(1),Decimal(7)))

print(dir(Decimal))

print(Decimal(1.1)+Decimal(2.2))

import decimal
print(dir(decimal))