from EngUnitConversion import *

p1 = Pressure(1.0, 'bar')
p2 = Pressure(14.7, 'psi')
p3 = p1 + p2

p1.changeUnit('kgcm2')

print(p1)
print(p3)

t1 = Temperature(30, 'C')
t2 = Temperature(18, 'F')

t1.setValue(34, 'C')
t1.changeUnit('R')

print(t1+t2)
