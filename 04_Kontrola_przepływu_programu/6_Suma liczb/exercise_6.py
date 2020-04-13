n = input('Podaj liczbę ')
n = int(n)
sum = 0
for num in range(0, n+1, 1):
    sum=sum+num

print('Suma liczb od 0 do ' + str(n) + ' to ' + str(sum))