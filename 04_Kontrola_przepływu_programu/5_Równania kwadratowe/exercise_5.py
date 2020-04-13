import math
print('Równanie w postaci a*x**2 + b*x + c == 0')
a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))
delta = b**2-4*a*c
if delta>0:
    pier_delta = math.sqrt(delta)
    x_1 = (-b + pier_delta) / (2 * a)
    x_2 = (-b - pier_delta) / (2 * a)
    print('Pierwiastki równania kwadratowego:\n x_1 =' + str(x_1) +
          '\nx_2 = ' + str(x_2))

if delta==0:
    pier_delta = math.sqrt(delta)
    x_1 = (-b + pier_delta) / (2 * a)
    x_2 = (-b - pier_delta) / (2 * a)
    print('Pierwiastki równania kwadratowego:\nx_1 = x_2 =' + str(x_1))

if delta<0:
    print('Delta jest ujemna')