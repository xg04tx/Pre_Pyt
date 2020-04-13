import datetime
today = datetime.datetime.now().year
name = input('Podaj swoje imię: ')
year = int(input('Podaj rok urodzenia: '))
age = today - year
print('Użytkownik: ' + name + ' jest w wieku ' + str(age) + ' lat')