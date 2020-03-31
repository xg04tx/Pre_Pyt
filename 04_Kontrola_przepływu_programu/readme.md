![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/152855/73064373-5ed69780-3ea1-11ea-8a71-3d370a5e7dd8.png)

# Kilka ważnych informacji

Przed przystąpieniem do rozwiązywania zadań przeczytaj poniższe wskazówki

## Jak zacząć?

1. Stwórz [*fork*](https://guides.github.com/activities/forking/) repozytorium z zadaniami.
2. Sklonuj repozytorium na swój komputer. Użyj do tego komendy `git clone adres_repozytorium`
Adres repozytorium możesz znaleźć na stronie repozytorium po naciśnięciu w guzik "Clone or download".
3. Rozwiąż zadania i skomituj zmiany do swojego repozytorium. Użyj do tego komend `git add nazwa_pliku`.
Jeżeli chcesz dodać wszystkie zmienione pliki użyj `git add .` 
Pamiętaj że kropka na końcu jest ważna!
Następnie skommituj zmiany komendą `git commit -m "nazwa_commita"`
4. Wypchnij zmiany do swojego repozytorium na GitHubie.  Użyj do tego komendy `git push origin master`
5. Stwórz [*pull request*](https://help.github.com/articles/creating-a-pull-request) do oryginalnego repozytorium, gdy skończysz wszystkie zadania.

Poszczególne zadania rozwiązuj w odpowiednich plikach.

# Poniżej znajdziesz wytyczne do zadań

## Zadanie 1 &ndash; Pętla `while`

* Wypisz na ekran 10 razy: "jestem programistą Pythona"
* Użyj pętli while.
## Zadanie 2 &ndash; Kolejne potęgi

* Napisz program, który obliczy kolejne potęgi liczby 2 dla wykładnika z przedziału od 0 do 10 włącznie.
* Wyświetl wynik w postaci:
```
0: 1
1: 2
2: 4
3: 8
4: 16
5: 32
6: 64
7: 128
8: 256
9: 512
10: 1024
```
* Użyj pętli `for`.

## Zadanie 3 &ndash; Porównanie imion

Napisz program, który:

* wyświetli na ekranie komunikat `"Podaj pierwsze imię"`,
* pobierze z klawiatury imię i zapisze go do zmiennej `first_name`,
* wyświetli na ekranie komunikat `"Podaj drugie imię"`,
* pobierze z klawiatury drugie imię użytkownika i zapisze go do zmiennej `second_name`,
* wyświetli na ekranie `Takie same` jeżeli imiona są takie same albo `Różne` jeżeli są różne.

> ###### Podpowiedź: użyj instrukcji warunkowej `if`!

## Zadanie 4 &ndash; Porównanie liczb

* Napisz program, który przyjmie od użytkownika dwie liczby (`a` i `b`).
* Wypisz informację która z nich jest większa w postaci:
```
a jest większe!
```

> ###### Podpowiedź: pamiętaj o rzutowaniu liczb na typ liczbowy (np. `float`)!
> ###### Stringi porównywane są z zachowaniem porządku leksykograficznego.

## Zadanie 5 &ndash; Równania kwadratowe

Napisz program do pomocy licealistom w liczeniu pierwiastków równań kwadratowych. Program ma:

* wyświetlić na ekranie komunikat: `Równanie w postaci a*x**2 + b*x + c == 0`,
* wyświetlić na ekranie komunikat: `Podaj a`,
* pobrać wartość od użytkownika i zapisać ją do zmiennej `a` (pamiętaj o rzutowaniu na odpowiedni typ),
* wyświetlić na ekranie komunikat: `Podaj b`,
* pobrać wartość od użytkownika i zapisać ją do zmiennej `b` (pamiętaj o rzutowaniu na odpowiedni typ),
* wyświetlić na ekranie komunikat: `Podaj c`,
* pobrać wartość od użytkownika i zapisać ją do zmiennej `c` (pamiętaj o rzutowaniu na odpowiedni typ),
* policzy deltę,
* jeśli delta > 0, policzyć wartości `x_1` i `x_2`, a następnie wyświetlić je w postaci:
```
Pierwiastki równania kwadratowego:
x_1 = <wartość>
x_2 = <wartość>
```
* jeżeli delta = 0, policzyć wartości `x_1` i `x_2` a następnie wyświetlić ją na ekranie w postaci:
```
Pierwiastki równania kwadratowego:
x_1 = x_2 = <wartość>

```
* jeżeli delta jest ujemna, wypisz na ekran odpowiednią informację.

**Uwaga** Nie musisz sprawdzać czy wejście jest poprawne.

## Zadanie 6 &ndash; Suma liczb

Napisz program, który policzy sumę wszystkich liczb od 0 do n, gdzie n jest podane przez użytkownika.

Zadanie rozwiąż na dwa sposoby:
* używając pętli,
* korzystając z wbudowanych w Pythona funkcji: `range` i `sum`.
## Zadanie 7 &ndash; Średnia

Napisz program, który:
* przyjmie od użytkownika informację, ile liczb ten chce wprowadzić,
* przyjmie `n` liczb (gdzie `n` - podane przez użytkownika),
* zapisze wprowadzone przez użytkownika liczby w liście w zmiennej `numbers`,
* policzy ich sumę i średnią,
* wypisze na ekran te liczby i czy suma jest większa od średniej:
```
Wprowadzone liczby: <liczby>
suma: <wartość>, 
średnia: <wartość> 
Suma jest większa! / Średnia jest większa!
```

## Zadanie 8 &ndash; Porównywanie napisów

* Zapisz w zmiennych ciągi znaków: `kot` i `pies`. 
* Wypisz na ekran wynik ich porównania operatorem `<`.

Zastanów się dlaczego wynik jest taki, popróbuj z innymi ciągami znaków, a wynik zapisz w komentarzu.

## Zadanie 9 &ndash; Definiowanie listy liczb

* Zdefiniuj listę składającą się z liczb od 1 do 8.
* Wypisz każdą z tych liczb w osobnym wierszu, poprzedzoną słowem `liczba: `.

> ###### Podpowiedź: do zdefiniowania liczby miżesz wykorzystać funkcję `range`.
## Zadanie 10 &ndash; Tabliczka mnożenia

* Napisz program, który pobierze od użytkownika liczbę `n` (z przedziału 1-10).
* Następnie wygeneruj dla tabliczkę mnożenia dla podanej liczby (patrz przykład poniżej).

##### Przykład:
```
Podaj liczbę: 3
```

##### Wynik:
```
1 * 3 = 3
2 * 3 = 6
3 * 3 = 9
4 * 3 = 12
5 * 3 = 15
6 * 3 = 18
7 * 3 = 21
8 * 3 = 24
9 * 3 = 27
10 * 3 = 30
```

## Zadanie 11 &ndash; Fizzbuzz

Używając pętli i konstrukcji z zakresem `(1, 101)` napisz program `fizzbuzz`, który dla każdej liczby od 1 do 100:
* jeżeli liczba jest podzielna przez 3, wypisze na ekran `Fizz`
* jeżeli liczba jest podzielna przez 5, program wypisze na ekran `Buzz`
* jeżeli liczba jest podzielna przez 3 i 5, program wypisze na ekran `FizzBuzz` 
(przykładowo dla liczby 15 ma się wypisać **tylko** `FizzBuzz`)
* w przeciwnym wypadku program wypisze na ekran liczbę.
---

Repozytorium z ćwiczeniami zostanie usunięte 2 tygodnie po zakończeniu kursu. Spowoduje to też usunięcie wszystkich forków, które są zrobione z tego repozytorium.
