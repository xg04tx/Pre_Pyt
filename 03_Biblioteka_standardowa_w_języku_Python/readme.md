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

## Zadanie 1 &ndash; Pobieranie danych od użytkownika.

Używając Pythona napisz program, który:

1. pobierze z klawiatury imię użytkownika,
2. pobierze z klawiatury nazwisko użytkownika,
3. wyświetli komunikat "Imię Nazwisko jest programistą Pythona!"

**Przykład:**
```
Podaj imię: Guido
Podaj nazwisko: van Rossum
Guido van Rossum jest programistą Pythona!
```

**Podpowiedź:** zapisuj wpisywane przez użytkownika dane do zmiennych.
## Zadanie 2 &ndash; Łączenie listy

* Zdefiniuj tablicę składającą się z liter od `a` do `e`.
* Wypisz te litery połączone znakiem spacji. 

Wynikiem działania Twojego programu ma być ciąg: `"a b c d e"`.

> ##### Podpowiedź: skorzystaj z metody `join`.
## Zadanie 3 &ndash; Dzielenie modulo

* Stwórz dwie zmienne i przypisz do nich dowolne liczby.
* Oblicz resztę z dzielenia (modulo) tych liczb i przypisz wynik do zmiennej `modulo_result`. 
* Wypisz zmienną `modulo_result` w konsoli. 

> Jeżeli nie do końca rozumiesz działanie operatora modulo przećwicz to z innymi liczbami.

## Zadanie 4 &ndash; inkrementacja i dekrementacja

* Stwórz zmienną o nazwie `counter`. 
* Wstaw do niej liczbę 145. 
* Wypisz jej wartość w konsoli, a następnie:

    * za pomocą inkrementacji o 1 zwiększ wartość zmiennej `counter`,
    * wypisz ją w konsoli,
    * za pomocą dekrementacji o 1 zmniejsz wartość zmiennej `counter`,
    * wypisz ją w konsoli.

###### Użyj zapisu skróconego!
## Zadanie 5 &ndash; Porównywanie zmiennych

* Stwórz dwie zmienne przechowujące dowolne liczby. 
* Sprawdź czy liczba pierwsza jest większa od drugiej za pomocą odpowiedniego operatora.
* Zapisz wynik porównania w zmiennej `result`. 
* Wypisz tę zmienną w konsoli.

## Zadanie 6 &ndash; Różnica wieku

* Utwórz zmienną o nazwie `father` i nadaj jej wartość `1974`.
* Utwórz drugą zmienną o nazwie `child` i nadaj jej wartość `2007`. 
* Wypisz na konsolę komunikat:
`"Ojciec jest starszy od dziecka o ### lat."`
* Zamiast ###, wstaw różnicę wieku ojca i dziecka.

> ###### Podpowiedź: użyj konstrukcji `fstring` lub metody `format`.

## Zadanie 5 &ndash; Dzielenie

* Używając Pythona podziel liczbę 11 przez 7 i wynik zapisz w zmiennej `result`.
* Wyświetl wynik w postaci:

```
11 : 7 = (tu wstaw wynik)
```

* Zaokrąglij wynik do 2 miejsc po przecinku.

> ###### Podpowiedź: użyj funkcji `round`.
## Zadanie 8 &ndash; Wiek użytkownika

Napisz program, który:

* wyświetli na ekranie komunikat `"Podaj swoje imię: "`,
* pobierze z klawiatury imię użytkownika i zapisze go do zmiennej `name`,
* wyświetli na ekranie komunikat `"Podaj rok swojego urodzenia: "`,
* pobierze z klawiatury roku urodzenia użytkownika i zapisze go do zmiennej `year`,
* zamieni rok urodzenia użytkownika na liczbę,
* obliczy aktualny wiek użytkownika i zapisze go do zmiennej `age`,
* wyświetli na konsoli komunikat, w którym poda imię i aktualny wiek użytkownika:
`Użytkownik: <name> jest w wieku <age> lat`.

**UWAGA:** zakładamy, że użytkownik jako rok swojego urodzenia poda poprawną liczbę!
---

Repozytorium z ćwiczeniami zostanie usunięte 2 tygodnie po zakończeniu kursu. Spowoduje to też usunięcie wszystkich forków, które są zrobione z tego repozytorium.
