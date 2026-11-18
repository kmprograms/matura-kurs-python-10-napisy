**Polski** · [English](README.en.md)

---

# Matura z informatyki, poziom rozszerzony - kurs Pythona, lekcja 10. "Napisy"

> ### 🎬 Wideo z omówieniem
> Pełne omówienie tej lekcji krok po kroku znajdziesz na moim kanale YouTube:
> **[Link do filmu na YouTube](https://youtu.be/N6YsSNfIFq8)**
>
> Na filmie pokazuję, jak tworzyć napisy i dlaczego są niemodyfikowalne. Omawiam znaki specjalne i napisy surowe, kody znaków i porównywanie leksykograficzne oraz najważniejsze metody napisów. Pokazuję też, jak rozbić wiersz danych metodą `split`, jak złożyć napis metodą `join` i co daje moduł `string`.

---

## Opis

Repozytorium zawiera kod z kursu Pythona, w którym przygotowuję do matury z informatyki na poziomie rozszerzonym. Ta lekcja dotyczy napisów, czyli obiektów typu `str`. Napisy pojawiają się na maturze bardzo często, między innymi wtedy, gdy trzeba przetworzyć kolejne wiersze pliku tekstowego z danymi.

Kod lekcji znajduje się w pliku `app-10-napisy.py`. Każde zagadnienie jest w osobnej funkcji:

- `podstawy` - tworzenie napisów, niemodyfikowalność, sklejanie i powielanie, napisy wielowierszowe, znaki specjalne, napisy surowe i metoda `join`
- `znaki_porownywanie_napisow` - kody znaków (`ord` i `chr`), porównywanie leksykograficzne, sortowanie napisów i sprawdzanie, czy znak jest literą lub cyfrą
- `metody_dla_napisow` - wycinki, wyszukiwanie, zliczanie, zmiana wielkości liter, usuwanie białych znaków, zamiana, rozbijanie i sprawdzanie zawartości napisu
- `split_join_w_praktyce` - małe zadanie na wierszu z liczbami, podobnym do wiersza z pliku maturalnego
- `modul_string` - gotowe stałe z modułu `string`

W repozytorium są też pliki z wcześniejszych lekcji kursu. W następnej lekcji omawiam komunikację z plikiem tekstowym.

## Wymagania

- Python 3.10 lub nowszy. Sam plik `app-10-napisy.py` nie korzysta z nowszych konstrukcji, ale plik `app-4-instrukcje-warunkowe.py` z wcześniejszej lekcji używa instrukcji `match`, która jest dostępna od Pythona 3.10
- Brak zewnętrznych zależności, wykorzystano wyłącznie bibliotekę standardową (moduły `string`, `random`, `math` i `collections`)

## Uruchomienie

```bash
git clone https://github.com/kmprograms/matura-kurs-python-10-napisy
cd matura-kurs-python-10-napisy
python app-10-napisy.py
```

Domyślnie funkcja `main` uruchamia tylko `modul_string()`. Wywołania pozostałych części lekcji są zakomentowane. Aby uruchomić wybraną część, usuń znak `#` przed jej wywołaniem:

```python
def main() -> None:
    # podstawy()
    # znaki_porownywanie_napisow()
    # metody_dla_napisow()
    # split_join_w_praktyce()
    modul_string()
```

Pliki z wcześniejszych lekcji uruchamiasz tak samo, np. `python app-9-kontenery-dict.py`.

## Struktura projektu

| Plik | Opis |
| --- | --- |
| `app-1-pierwszy-program-zmienne.py` | Pierwszy program, zmienne, f-stringi, operatory arytmetyczne i zamiana typów |
| `app-2-liczby-calkowite.py` | Działania na liczbach całkowitych, reszta z dzielenia, podzielność, operatory relacji, spójniki logiczne i wyznaczanie cyfr liczby |
| `app-3-pozyskiwanie-danych-systemy-liczbowe-float.py` | Wczytywanie danych, moduł `random`, systemy liczbowe, operacje bitowe i moduł `math` |
| `app-4-instrukcje-warunkowe.py` | Warunki logiczne, instrukcje `if`, `elif` i `else`, wyrażenie warunkowe i instrukcja `match` |
| `app-5-petle.py` | Pętle `while` i `for`, funkcja `range`, instrukcje `break` i `continue`, pętle zagnieżdżone |
| `app-6-funkcje.py` | Funkcje, parametry i argumenty, wartości domyślne, adnotacje typów i zwracanie wartości |
| `app-7-kontenery-listy.py` | Listy i ich metody, wycinki, listy dwuwymiarowe, wyrażenia listowe i wyrażenia generatora |
| `app-8-kontenery-tuple.py` | Krotki i `namedtuple` |
| `app-9-kontenery-dict.py` | Słowniki, `Counter`, `defaultdict`, zbiory i `deque` |
| `app-10-napisy.py` | Kod tej lekcji: napisy |
| `README.md` | Opis repozytorium po polsku |
| `README.en.md` | Opis repozytorium po angielsku |

## Omówienie kodu

### Podstawy - funkcja `podstawy`

Napis to ciąg znaków. Zapisuje się go w apostrofach albo w cudzysłowach. Oba zapisy są równoważne. Napis wielowierszowy zapisuje się w potrójnych cudzysłowach.

Napisy są niemodyfikowalne. Metoda `upper` nie zmienia napisu `s1`, tylko tworzy nowy napis z samych wielkich liter i na niego wskazuje `s2`. Tak samo działa operator `+=`. Po `s1 += "!!!"` zmienna `s1` wskazuje na nowy napis, a stary zostaje porzucony.

```python
    s1 = "Cześć"
    s2 = s1.upper()
    print(s1)
    print(s2)

    s1 += "!!!"
    print(s1)

    # s1[0] = "J"
    print(s1[0])
    print(s1[1:])

    s3 = "J" + s1[2:]
    print(s3)
```

Wynik:

```
Cześć
CZEŚĆ
Cześć!!!
C
ześć!!!
Jeść!!!
```

Odczyt znaku po indeksie i wycinki działają tak samo jak w listach. Zmiana znaku pod indeksem nie jest możliwa, dlatego linia `# s1[0] = "J"` jest zakomentowana. Napis "Jeść!!!" powstaje przez konkatenację, czyli sklejenie litery "J" z wycinkiem `s1[2:]`.

Operator `+` nie połączy napisu z liczbą. Liczbę trzeba najpierw zamienić na napis funkcją `str` albo użyć f-stringa, który sam wykona konwersję. Operator `*` powiela napis.

```python
    age = 18
    print("Wiek: " + str(age))
    print(f"Wiek: {age}")
    print("ab" * 3)
```

Wynik:

```
Wiek: 18
Wiek: 18
ababab
```

Napis wielowierszowy też może być f-stringiem. Wcięcia wewnątrz takiego napisu są jego częścią, dlatego kolejne wiersze w kodzie zaczynają się od początku linii. Ukośnik `\` na końcu wiersza sprawia, że enter nie tworzy nowego wiersza, więc pierwszy wiersz zostaje sklejony z drugim.

```python
    s4 = f"""Pierwszy wiersz\
Drugi wiersz
Wiek: {age}"""
    print(s4)
```

Wynik:

```
Pierwszy wierszDrugi wiersz
Wiek: 18
```

W napisie można umieszczać znaki specjalne. W lekcji używam trzech: `\n` to nowy wiersz, `\t` to tabulator, a `\\` to pojedynczy ukośnik. W napisie surowym (raw string) z przedrostkiem `r` znaki specjalne nie są interpretowane.

```python
    s5 = "Wiersz nr 1\nWiersz nr 2 z tabulatorem\tkoniec\nWiersz nr 3 z ukośnikiem \\"
    print(s5)

    s6 = r"Raw 1\nRaw 2\tRaw 3\\"
    print(s6)
```

Wynik:

```
Wiersz nr 1
Wiersz nr 2 z tabulatorem	koniec
Wiersz nr 3 z ukośnikiem \
Raw 1\nRaw 2\tRaw 3\\
```

Metoda `join` łączy elementy listy w jeden napis. Napis, na rzecz którego ją wołasz, jest separatorem. Może być pusty albo składać się z kilku znaków. Funkcja `len` zwraca długość napisu, a funkcja `list` rozbija napis na listę pojedynczych znaków.

```python
    s7 = ["a", "b", "c"]
    s8 = "".join(s7)
    print(s8)
    s9 = ",".join(s7)
    print(s9)

    print(len(s9))
    print(list("kmprograms"))
```

Wynik:

```
abc
a,b,c
5
['k', 'm', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 's']
```

### Znaki i porównywanie napisów - funkcja `znaki_porownywanie_napisow`

W Pythonie nie ma osobnego typu na pojedynczy znak, takiego jak `char` w C++. Pojedynczy znak to po prostu napis o długości 1. Niektóre funkcje, np. `ord`, przyjmują tylko taki napis.

Każdy znak jest przechowywany jako kod. Funkcja `ord` zwraca kod znaku, a funkcja `chr` zamienia kod na znak. Python obsługuje cały Unicode, w tym polskie litery, ale właściwości ważne na maturze widać już w tabeli ASCII. Link do niej jest w komentarzu w kodzie.

| Grupa znaków | Kody dziesiętne |
| --- | --- |
| cyfry `0`-`9` | 48-57 |
| wielkie litery `A`-`Z` | 65-90 |
| małe litery `a`-`z` | 97-122 |

Kodów nie trzeba znać na pamięć, bo zawsze odczytasz je funkcją `ord`. Ważna jest kolejność. Najpierw są cyfry, potem wielkie litery, potem małe litery, a w każdej grupie znaki leżą jeden po drugim.

```python
    c1 = "a"
    print(ord(c1))
    # https://pl.wikipedia.org/wiki/ASCII
```

Wynik: `97`.

```python
    codes = [80, 89, 84, 72, 79, 78]
    print("".join(chr(c) for c in codes))
    print([ord(c) for c in "Matura"])
```

Wynik:

```
PYTHON
[77, 97, 116, 117, 114, 97]
```

Napis jest iterowalny. W pętli `for` pod zmienną trafia kolejny znak napisu, dlatego napis można podać wszędzie tam, gdzie wcześniej podawało się listę, np. w wyrażeniu listowym.

Porównywanie napisów odbywa się znak po znaku na podstawie kodów, czyli leksykograficznie. Działają wszystkie operatory relacji: `<`, `<=`, `>`, `>=`, `==` i `!=`.

```python
    s1 = "ala"
    s2 = "adam"
    s3 = "alabama"
    print(s1 < s2)
    print(s1 < s3)
    print(s1 <= s3)
    print(s1 > s2)
    print(s1 >= s2)
    print(s1 == s2)
    print(s1 != s2)
```

Wynik:

```
False
True
True
True
True
False
True
```

- `s1 < s2` daje `False`. Pierwsze litery są takie same, a przy drugich `d` ma mniejszy kod niż `l`. Dlatego to "adam" jest mniejszy, choć ma więcej znaków.
- Gdyby `s1` miało wartość "Ala", wynik byłby `True`, bo wielkie `A` ma mniejszy kod niż małe `a`.
- `s1 < s3` daje `True`. Początek obu napisów jest taki sam, a "ala" kończy się wcześniej. Długość ma znaczenie dopiero w takiej sytuacji, a nie w pierwszej kolejności.

Sortowanie napisów domyślnie korzysta z porównywania leksykograficznego. Parametrem `key` wskazujesz inne kryterium, np. `str.lower`, czyli porównanie po zamianie na małe litery, albo wyrażenie lambda.

```python
    imiona = ["Ala", "aleksander", "ALICJA", "bogdan", "Bogumila"]
    print(sorted(imiona))
    print(sorted(imiona, key=str.lower))
    print(sorted(imiona, key=lambda imie: len(imie)))
```

Wynik:

```
['ALICJA', 'Ala', 'Bogumila', 'aleksander', 'bogdan']
['Ala', 'aleksander', 'ALICJA', 'bogdan', 'Bogumila']
['Ala', 'ALICJA', 'bogdan', 'Bogumila', 'aleksander']
```

Porównania pozwalają też sprawdzić, czy znak jest małą literą, wielką literą albo cyfrą. Warunek `len(s4) == 1` jest potrzebny, bo bez niego np. napis "ala" też mieści się między "a" i "z".

```python
    s4 = "a"
    print(len(s4) == 1 and "a" <= s4 <= "z")
    print(len(s4) == 1 and "A" <= s4 <= "Z")
    print(len(s4) == 1 and "0" <= s4 <= "9")

    # print(ord("ala"))

    print("".join([s3[i] for i in range(len(s3)) if s3[i] in "alb"]))
```

Wynik:

```
True
False
False
alabaa
```

Linia `# print(ord("ala"))` pokazuje, że `ord` nie przyjmie dłuższego napisu. Po jej odkomentowaniu program zgłosi błąd `TypeError: ord() expected a character, but string of length 3 found`.

Ostatnia linia przegląda napis "alabama" po indeksach i zostawia tylko znaki, które występują w napisie "alb". Z wybranych znaków `join` składa nowy napis.

### Metody dla napisów - funkcja `metody_dla_napisow`

Napisy obsługują te same wycinki co listy. Krok `-1` odwraca napis, a krok `2` bierze co drugi znak.

```python
    s1 = "kmprograms"

    print(s1[0], s1[-1], s1[1:4], s1[2:])
    print(s1[::-1])
    print(s1[::2])
```

Wynik:

```
k s mpr programs
smargorpmk
kporm
```

Wyszukiwanie i zliczanie dla `s1 = "kmprograms"`. Indeksy są liczone od zera.

| Wyrażenie | Wynik | Opis |
| --- | --- | --- |
| `"prog" in s1` | `True` | czy napis zawiera podany fragment |
| `s1.index("r")` | `3` | indeks pierwszego wystąpienia |
| `s1.rindex("r")` | `6` | indeks ostatniego wystąpienia |
| `s1.find("m")` | `1` | indeks pierwszego wystąpienia |
| `s1.rfind("m")` | `8` | indeks ostatniego wystąpienia |
| `s1.count("r")` | `2` | liczba wystąpień |
| `s1.startswith("km")` | `True` | czy napis zaczyna się od podanego fragmentu |
| `s1.endswith("ms")` | `True` | czy napis kończy się podanym fragmentem |
| `min(s1)` | `a` | najmniejszy znak w sensie leksykograficznym |
| `max(s1)` | `s` | największy znak w sensie leksykograficznym |

Gdy szukanego fragmentu nie ma, `find` i `rfind` zwracają `-1`, a `index` i `rindex` zgłaszają wyjątek.

Zmiana wielkości liter dla `s2 = "kmPrograms"`:

| Wyrażenie | Wynik | Opis |
| --- | --- | --- |
| `s2.lower()` | `kmprograms` | same małe litery |
| `s2.upper()` | `KMPROGRAMS` | same wielkie litery |
| `s2.swapcase()` | `KMpROGRAMS` | zamiana wielkości każdej litery |
| `"ala ma kota".title()` | `Ala Ma Kota` | każdy wyraz od wielkiej litery |
| `"ala ma kota".capitalize()` | `Ala ma kota` | tylko pierwszy wyraz od wielkiej litery |

Usuwanie białych znaków przyda się przy wczytywaniu danych z pliku. Podkreślenia w f-stringach pokazują, gdzie kończy się wynik.

```python
    s3 = "   tekst    "
    print(f"_{s3.strip()}_")
    print(f"_{s3.lstrip()}_")
    print(f"_{s3.rstrip()}_")
```

Wynik:

```
_tekst_
_tekst    _
_   tekst_
```

`strip` usuwa białe znaki z obu stron, `lstrip` tylko z lewej, a `rstrip` tylko z prawej.

Zamiana, rozbijanie i dopełnianie:

| Wyrażenie | Wynik | Opis |
| --- | --- | --- |
| `"kontakt@km-programs.pl".replace("k", "K")` | `KontaKt@Km-programs.pl` | zamienia wszystkie wystąpienia |
| `"a-b-c".replace("-", "", 1)` | `ab-c` | zamienia tylko pierwsze wystąpienie |
| `"Ala ma kota".split()` | `['Ala', 'ma', 'kota']` | rozbija domyślnie po białych znakach, np. spacjach |
| `"Ala-ma kota".split("-")` | `['Ala', 'ma kota']` | rozbija po podanym separatorze |
| `"Ala ma kota".split(" ", 1)` | `['Ala', 'ma kota']` | rozbija najwyżej po jednym separatorze |
| `"kontakt@km-programs.pl".partition("@")` | `('kontakt', '@', 'km-programs.pl')` | krotka z częścią przed separatorem, separatorem i częścią po nim |
| `"89".zfill(6)` | `000089` | dopełnia zerami z lewej do sześciu znaków |
| `"89".center(6, "*")` | `**89**` | wyśrodkowuje napis i dopełnia go podanym znakiem |

`partition` bierze pod uwagę tylko pierwsze wystąpienie separatora. `zfill` przyda się później, np. przy konwersji liczb na system binarny i dodawaniu liczb binarnych.

Sprawdzanie zawartości napisu:

| Wyrażenie | Wynik | Co sprawdza |
| --- | --- | --- |
| `"a".isalpha()` | `True` | czy to litera |
| `"a".isalnum()` | `True` | czy to litera lub cyfra |
| `"1".isdigit()` | `True` | czy to cyfra |
| `"a".islower()` | `True` | czy to mała litera |
| `"A".isupper()` | `True` | czy to wielka litera |
| `" ".isspace()` | `True` | czy to biały znak |

### split i join w praktyce - funkcja `split_join_w_praktyce`

Zmienna `linia` symuluje jeden wiersz z pliku tekstowego, jaki możesz spotkać na maturze. Zadanie polega na zsumowaniu liczb z wiersza i zbudowaniu z nich nowych napisów.

```python
def split_join_w_praktyce() -> None:
    linia = "12 45 7 30"

    elementy = linia.split()
    print(elementy)

    liczby = [int(e) for e in elementy]
    print(liczby)
    print(sum(liczby))

    print(",".join(elementy))
    print(", ".join(str(l % 10) for l in liczby))
```

Kolejne kroki:

1. `linia.split()` rozbija wiersz po spacjach na listę napisów
2. wyrażenie listowe `[int(e) for e in elementy]` zamienia każdy napis na liczbę całkowitą
3. `sum(liczby)` zwraca sumę liczb z wiersza
4. `",".join(elementy)` skleja napisy z listy `elementy` i oddziela je przecinkiem
5. `", ".join(str(l % 10) for l in liczby)` tworzy napis z cyfr jedności liczb, oddzielonych przecinkiem i spacją. `l % 10` daje liczbę, dlatego przed sklejeniem zamieniam ją na napis funkcją `str`

Wynik:

```
['12', '45', '7', '30']
[12, 45, 7, 30]
94
12,45,7,30
2, 5, 7, 0
```

### Moduł string - funkcja `modul_string`

Moduł `string` importuję na początku pliku instrukcją `import string`. Zawiera gotowe stałe z zestawami znaków. Zamiast wpisywać alfabet albo cyfry ręcznie, możesz od razu użyć tych stałych, np. przy sprawdzaniu właściwości liter.

```python
def modul_string() -> None:
    print(string.ascii_letters)
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    print(string.digits)
    print(string.hexdigits)
    print(string.punctuation)
```

Moduł ma też inne stałe, np. `octdigits`, `whitespace` i `printable`. Warto zajrzeć do dokumentacji modułu.

## Wyniki

Po uruchomieniu z domyślną funkcją `main` program wywołuje `modul_string()` i wypisuje:

```
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
0123456789abcdefABCDEF
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

Wyniki pozostałych funkcji podałem przy ich omówieniu.

## Uwagi implementacyjne

Każde zagadnienie jest w osobnej funkcji z adnotacją `-> None`, a wywołania są zebrane w funkcji `main`, uruchamianej przez `if __name__ == '__main__':`. Dzięki temu łatwo uruchomić tylko wybraną część lekcji.

Metody, które pozornie zmieniają napis, takie jak `lower`, `replace` czy `strip`, zawsze zwracają nowy napis. Oryginał zostaje bez zmian. Widać to po wywołaniu `print(s2)` w funkcji `metody_dla_napisow`, które po wszystkich operacjach nadal wypisuje `kmPrograms`.

Każde sklejenie napisów, także operatorem `+=`, tworzy nowy obiekt. Przy bardzo dużej liczbie takich operacji ciągłe kopiowanie może spowolnić program. Warto o tym pamiętać przy rozwiązywaniu zadań maturalnych.

Przy sprawdzaniu znaku za pomocą porównań warunek `len(s4) == 1` daje pewność, że porównujesz pojedynczy znak, a nie dłuższy napis.

Zachowanie metod `isalpha`, `isalnum` i `isdigit` dla napisów dłuższych niż jeden znak warto sprawdzić w dokumentacji Pythona.

Lekcja celowo pomija wyrażenia regularne. W tej serii skupiam się na tym, co jest niezbędne do implementowania rozwiązań zadań na maturze z informatyki.