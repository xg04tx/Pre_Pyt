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

## Zadanie 1 &ndash; Typy danych

W pliku `exercise_1.py` utwórz 5 zmiennych i wstaw do nich następujące dane:

* liczbę całkowitą,
* liczbę zmiennoprzecinkową,
* string (napis),
* wielolinijkowy napis,
* wartość logiczną.

Skomentuj odpowiednio każdą zmienną, podając informację jaki typ danych przechowuje.

Każdą zmienną wyświetl na ekranie, w postaci:
`Zmienna XXX typu YYY`

##### Podpowiedź: do pobrania typu służy funkcja `type()`. 


## Zadanie 2 &ndash; Wartości logiczne

Stwórz dwie zmienne i przypisz do nich dwie wartości logiczne, jakie znasz. Porównaj je za pomocą operatora `==`,
a wynik zapisz do trzeciej zmiennej. Napisz w komentarzu swoje spostrzeżenia.
## Zadanie 3 &ndash; Dodawanie

W pliku `exercise_3.py` utwórz następujące zmienne:

* `add1` o wartości całkowitej,
* `add2` o wartości zmiennoprzecinkowej,
* `sum_value`, która będzie sumą `add1` i `add2`.

> ###### tip: nie używaj zmiennej sum, ponieważ jest to zarezerwowane słowo w Pythonie

Każdą zmienną wyświetl na ekranie razem z jej typem.
## Zadanie 4 &ndash; Operacje matematyczne

Napisz program, który utworzy dwie zmienne: `a1` i `a2`, po czym wykona następujące czynności:

* Przypisze zmiennej `a1` wartość **10**, zmiennej `a2` wartość **15**,
* Utworzy zmienną `sum_value`, której nada wartość sumy zmiennych `a1` i `a2`,
* Utworzy zmienną `quotus`, której nada wartość ilorazu zmiennych `a2` i `a1`,
* Utworzy zmienną `int_part`, której nada wartość części całkowitej zmiennej `quotus`,
* Wyświetli w terminalu wartości wszystkich zmiennych razem z ich typami.
## Zadanie 5 &ndash; Dodawanie elementów do listy

* Zdefiniuj **pustą** nową listę `animals`.
* Dodaj do niej imiona co najmniej trzech bajkowych zwierząt, które znasz.
* Wyświetl listę po każdej operacji.

> ###### Podpowiedź: Wykorzystaj metodę `append`.
## Zadanie 2 &ndash; Lista liczb

* Zdefiniuj tablicę składającą się z liczb od 1 do 8.
* Wypisz na ekranie przedostatni element.

> ###### Podpowiedź: użyj odwrotnego indeksowania. 
## Zadanie 7 &ndash; Pobieranie elementów z listy

Zajrzyj do pliku exercise_7.py, znajdziesz tam zdefiniowaną tablicę:
```python
characters = ["Harry", "Ron", "Hermione"]
```

* wyświetl w konsoli pierwszy element tablicy,
* wyświetl w konsoli ostatni element tablicy.

> ###### Podpowiedź: użyj odwrotnego indeksowania do pobrania ostatniego elementu. 
---

Repozytorium z ćwiczeniami zostanie usunięte 2 tygodnie po zakończeniu kursu. Spowoduje to też usunięcie wszystkich forków, które są zrobione z tego repozytorium.
