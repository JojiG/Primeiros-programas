A = float(input('Digite o primeiro termo: '))
B = float(input('Digite o segundo termo: '))
C = float(input('Digite o terceiro termo: '))
poli = ('({})X^2+({})X+({})'.format(A, B, C))
delta = B**2-4*A*C
print(delta)
x1 = (-B+delta**(1/2))/(2*A)
x2 = (-B-delta**(1/2))/(2*A)
print('As raízes de {} são {:.2f} e {:.2f}'.format(poli, x1, x2))
