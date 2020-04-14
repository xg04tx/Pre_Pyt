numbers = []
n = int(input('Podaj ilość liczb: '))
for n in range(0, n, 1):
    numbers.append(int(input('Podaj liczbę: ')))
print(numbers)
suma = sum(numbers)
print(suma)
average = suma / n
print(average)

if suma > average:
    print('suma jest większa!')
else:
    print('średnia jest większa!')
