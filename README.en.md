[Polski](README.md) · **English**

---

# Matura in Computer Science, extended level - Python course, lesson 10. "Strings"

> ### 🎬 Video walkthrough
> You can find a full step-by-step walkthrough of this lesson on my YouTube channel:
> **[Watch the video on YouTube](https://youtu.be/N6YsSNfIFq8)**
>
> In the video I show how to create strings and why they are immutable. I cover escape sequences and raw strings, character codes and lexicographic comparison, and the most important string methods. I also show how to split a line of data with `split`, how to build a string with `join`, and what the `string` module offers.

---

## Description

This repository contains code from my Python course that prepares students for the Matura exam in computer science (the Polish high school leaving exam) at the extended level. This lesson covers strings, i.e. objects of type `str`. Strings come up very often in the Matura exam, for example when you need to process the lines of a text file with data.

The code for this lesson is in the `app-10-napisy.py` file. Each topic has its own function:

- `podstawy` - creating strings, immutability, concatenation and repetition, multi-line strings, escape sequences, raw strings and the `join` method
- `znaki_porownywanie_napisow` - character codes (`ord` and `chr`), lexicographic comparison, sorting strings and checking whether a character is a letter or a digit
- `metody_dla_napisow` - slicing, searching, counting, changing letter case, stripping whitespace, replacing, splitting and checking string contents
- `split_join_w_praktyce` - a small exercise on a line of numbers, similar to a line from a Matura data file
- `modul_string` - ready-made constants from the `string` module

The repository also contains files from earlier lessons of the course. In the next lesson I cover working with text files.

## Requirements

- Python 3.10 or newer. The `app-10-napisy.py` file itself does not use any newer constructs, but `app-4-instrukcje-warunkowe.py` from an earlier lesson uses the `match` statement, which is available since Python 3.10
- No external dependencies, only the standard library is used (the `string`, `random`, `math` and `collections` modules)

## Running

```bash
git clone https://github.com/kmprograms/matura-kurs-python-10-napisy
cd matura-kurs-python-10-napisy
python app-10-napisy.py
```

By default the `main` function runs only `modul_string()`. The calls to the other parts of the lesson are commented out. To run a chosen part, remove the `#` character in front of its call:

```python
def main() -> None:
    # podstawy()
    # znaki_porownywanie_napisow()
    # metody_dla_napisow()
    # split_join_w_praktyce()
    modul_string()
```

You run the files from earlier lessons the same way, e.g. `python app-9-kontenery-dict.py`.

## Project structure

| File | Description |
| --- | --- |
| `app-1-pierwszy-program-zmienne.py` | First program, variables, f-strings, arithmetic operators and type conversion |
| `app-2-liczby-calkowite.py` | Integer operations, remainder, divisibility, relational operators, logical operators and extracting the digits of a number |
| `app-3-pozyskiwanie-danych-systemy-liczbowe-float.py` | Reading input, the `random` module, number systems, bitwise operations and the `math` module |
| `app-4-instrukcje-warunkowe.py` | Logical conditions, `if`, `elif` and `else` statements, conditional expressions and the `match` statement |
| `app-5-petle.py` | `while` and `for` loops, the `range` function, `break` and `continue` statements, nested loops |
| `app-6-funkcje.py` | Functions, parameters and arguments, default values, type hints and return values |
| `app-7-kontenery-listy.py` | Lists and their methods, slicing, two-dimensional lists, list comprehensions and generator expressions |
| `app-8-kontenery-tuple.py` | Tuples and `namedtuple` |
| `app-9-kontenery-dict.py` | Dictionaries, `Counter`, `defaultdict`, sets and `deque` |
| `app-10-napisy.py` | Code for this lesson: strings |
| `README.md` | Repository description in Polish |
| `README.en.md` | Repository description in English |

## Code walkthrough

### Basics - the `podstawy` function

A string is a sequence of characters. You write it in single quotes or double quotes. Both forms are equivalent. A multi-line string is written in triple quotes.

Strings are immutable. The `upper` method does not change the `s1` string. It creates a new string made of uppercase letters only, and `s2` points to that new string. The `+=` operator works the same way. After `s1 += "!!!"` the variable `s1` points to a new string, and the old one is discarded.

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

Output:

```
Cześć
CZEŚĆ
Cześć!!!
C
ześć!!!
Jeść!!!
```

Reading a character by index and slicing work the same way as with lists. Changing a character at a given index is not possible, which is why the `# s1[0] = "J"` line is commented out. The string "Jeść!!!" is created by concatenation, i.e. joining the letter "J" with the slice `s1[2:]`.

The `+` operator cannot join a string with a number. You first have to convert the number to a string with the `str` function or use an f-string, which does the conversion for you. The `*` operator repeats a string.

```python
    age = 18
    print("Wiek: " + str(age))
    print(f"Wiek: {age}")
    print("ab" * 3)
```

Output:

```
Wiek: 18
Wiek: 18
ababab
```

A multi-line string can also be an f-string. Indentation inside such a string is part of it, which is why the following lines in the code start at the beginning of the line. A backslash `\` at the end of a line means the line break does not create a new line, so the first line is joined with the second one.

```python
    s4 = f"""Pierwszy wiersz\
Drugi wiersz
Wiek: {age}"""
    print(s4)
```

Output:

```
Pierwszy wierszDrugi wiersz
Wiek: 18
```

You can put escape sequences in a string. The lesson uses three of them: `\n` is a new line, `\t` is a tab, and `\\` is a single backslash. In a raw string with the `r` prefix, escape sequences are not interpreted.

```python
    s5 = "Wiersz nr 1\nWiersz nr 2 z tabulatorem\tkoniec\nWiersz nr 3 z ukośnikiem \\"
    print(s5)

    s6 = r"Raw 1\nRaw 2\tRaw 3\\"
    print(s6)
```

Output:

```
Wiersz nr 1
Wiersz nr 2 z tabulatorem	koniec
Wiersz nr 3 z ukośnikiem \
Raw 1\nRaw 2\tRaw 3\\
```

The `join` method joins the elements of a list into one string. The string you call it on is the separator. It can be empty or consist of several characters. The `len` function returns the length of a string, and the `list` function splits a string into a list of single characters.

```python
    s7 = ["a", "b", "c"]
    s8 = "".join(s7)
    print(s8)
    s9 = ",".join(s7)
    print(s9)

    print(len(s9))
    print(list("kmprograms"))
```

Output:

```
abc
a,b,c
5
['k', 'm', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 's']
```

### Characters and string comparison - the `znaki_porownywanie_napisow` function

Python has no separate type for a single character, such as `char` in C++. A single character is simply a string of length 1. Some functions, e.g. `ord`, accept only such a string.

Every character is stored as a code. The `ord` function returns the code of a character, and the `chr` function converts a code into a character. Python supports the whole of Unicode, including Polish letters, but the properties that matter for the Matura exam are already visible in the ASCII table. A link to it is in a comment in the code.

| Character group | Decimal codes |
| --- | --- |
| digits `0`-`9` | 48-57 |
| uppercase letters `A`-`Z` | 65-90 |
| lowercase letters `a`-`z` | 97-122 |

You do not need to memorize the codes, because you can always read them with `ord`. What matters is the order. Digits come first, then uppercase letters, then lowercase letters, and within each group the characters follow one another.

```python
    c1 = "a"
    print(ord(c1))
    # https://pl.wikipedia.org/wiki/ASCII
```

Output: `97`.

```python
    codes = [80, 89, 84, 72, 79, 78]
    print("".join(chr(c) for c in codes))
    print([ord(c) for c in "Matura"])
```

Output:

```
PYTHON
[77, 97, 116, 117, 114, 97]
```

A string is iterable. In a `for` loop the variable takes the next character of the string, so you can use a string anywhere you previously used a list, e.g. in a list comprehension.

Strings are compared character by character based on their codes, i.e. lexicographically. All relational operators work: `<`, `<=`, `>`, `>=`, `==` and `!=`.

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

Output:

```
False
True
True
True
True
False
True
```

- `s1 < s2` gives `False`. The first letters are the same, and in the second position `d` has a smaller code than `l`. That is why "adam" is smaller, even though it has more characters.
- If `s1` were "Ala", the result would be `True`, because uppercase `A` has a smaller code than lowercase `a`.
- `s1 < s3` gives `True`. Both strings start the same way, and "ala" ends sooner. Length matters only in this situation, not in the first place.

Sorting strings uses lexicographic comparison by default. With the `key` parameter you choose a different criterion, e.g. `str.lower`, which compares the strings after converting them to lowercase, or a lambda expression.

```python
    imiona = ["Ala", "aleksander", "ALICJA", "bogdan", "Bogumila"]
    print(sorted(imiona))
    print(sorted(imiona, key=str.lower))
    print(sorted(imiona, key=lambda imie: len(imie)))
```

Output:

```
['ALICJA', 'Ala', 'Bogumila', 'aleksander', 'bogdan']
['Ala', 'aleksander', 'ALICJA', 'bogdan', 'Bogumila']
['Ala', 'ALICJA', 'bogdan', 'Bogumila', 'aleksander']
```

Comparisons also let you check whether a character is a lowercase letter, an uppercase letter or a digit. The `len(s4) == 1` condition is necessary, because without it, e.g., the string "ala" also falls between "a" and "z".

```python
    s4 = "a"
    print(len(s4) == 1 and "a" <= s4 <= "z")
    print(len(s4) == 1 and "A" <= s4 <= "Z")
    print(len(s4) == 1 and "0" <= s4 <= "9")

    # print(ord("ala"))

    print("".join([s3[i] for i in range(len(s3)) if s3[i] in "alb"]))
```

Output:

```
True
False
False
alabaa
```

The `# print(ord("ala"))` line shows that `ord` does not accept a longer string. When you uncomment it, the program raises the error `TypeError: ord() expected a character, but string of length 3 found`.

The last line goes through the string "alabama" by index and keeps only the characters that appear in the string "alb". `join` then builds a new string from the selected characters.

### String methods - the `metody_dla_napisow` function

Strings support the same slicing as lists. A step of `-1` reverses the string, and a step of `2` takes every second character.

```python
    s1 = "kmprograms"

    print(s1[0], s1[-1], s1[1:4], s1[2:])
    print(s1[::-1])
    print(s1[::2])
```

Output:

```
k s mpr programs
smargorpmk
kporm
```

Searching and counting for `s1 = "kmprograms"`. Indexes start at zero.

| Expression | Result | Description |
| --- | --- | --- |
| `"prog" in s1` | `True` | whether the string contains the given substring |
| `s1.index("r")` | `3` | index of the first occurrence |
| `s1.rindex("r")` | `6` | index of the last occurrence |
| `s1.find("m")` | `1` | index of the first occurrence |
| `s1.rfind("m")` | `8` | index of the last occurrence |
| `s1.count("r")` | `2` | number of occurrences |
| `s1.startswith("km")` | `True` | whether the string starts with the given substring |
| `s1.endswith("ms")` | `True` | whether the string ends with the given substring |
| `min(s1)` | `a` | smallest character in the lexicographic sense |
| `max(s1)` | `s` | largest character in the lexicographic sense |

When the substring is not found, `find` and `rfind` return `-1`, while `index` and `rindex` raise an exception.

Changing letter case for `s2 = "kmPrograms"`:

| Expression | Result | Description |
| --- | --- | --- |
| `s2.lower()` | `kmprograms` | lowercase letters only |
| `s2.upper()` | `KMPROGRAMS` | uppercase letters only |
| `s2.swapcase()` | `KMpROGRAMS` | swaps the case of every letter |
| `"ala ma kota".title()` | `Ala Ma Kota` | every word starts with an uppercase letter |
| `"ala ma kota".capitalize()` | `Ala ma kota` | only the first word starts with an uppercase letter |

Stripping whitespace is useful when reading data from a file. The underscores in the f-strings show where the result ends.

```python
    s3 = "   tekst    "
    print(f"_{s3.strip()}_")
    print(f"_{s3.lstrip()}_")
    print(f"_{s3.rstrip()}_")
```

Output:

```
_tekst_
_tekst    _
_   tekst_
```

`strip` removes whitespace from both sides, `lstrip` only from the left, and `rstrip` only from the right.

Replacing, splitting and padding:

| Expression | Result | Description |
| --- | --- | --- |
| `"kontakt@km-programs.pl".replace("k", "K")` | `KontaKt@Km-programs.pl` | replaces all occurrences |
| `"a-b-c".replace("-", "", 1)` | `ab-c` | replaces only the first occurrence |
| `"Ala ma kota".split()` | `['Ala', 'ma', 'kota']` | splits on whitespace by default, e.g. spaces |
| `"Ala-ma kota".split("-")` | `['Ala', 'ma kota']` | splits on the given separator |
| `"Ala ma kota".split(" ", 1)` | `['Ala', 'ma kota']` | splits on at most one separator |
| `"kontakt@km-programs.pl".partition("@")` | `('kontakt', '@', 'km-programs.pl')` | tuple with the part before the separator, the separator and the part after it |
| `"89".zfill(6)` | `000089` | pads with zeros on the left to six characters |
| `"89".center(6, "*")` | `**89**` | centers the string and pads it with the given character |

`partition` takes only the first occurrence of the separator into account. `zfill` will come in handy later, e.g. when converting numbers to binary and adding binary numbers.

Checking string contents:

| Expression | Result | What it checks |
| --- | --- | --- |
| `"a".isalpha()` | `True` | whether it is a letter |
| `"a".isalnum()` | `True` | whether it is a letter or a digit |
| `"1".isdigit()` | `True` | whether it is a digit |
| `"a".islower()` | `True` | whether it is a lowercase letter |
| `"A".isupper()` | `True` | whether it is an uppercase letter |
| `" ".isspace()` | `True` | whether it is a whitespace character |

### split and join in practice - the `split_join_w_praktyce` function

The `linia` variable simulates a single line from a text file, the kind you may come across in the Matura exam. The task is to sum the numbers in the line and build new strings from them.

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

The steps:

1. `linia.split()` splits the line on spaces into a list of strings
2. the list comprehension `[int(e) for e in elementy]` converts each string into an integer
3. `sum(liczby)` returns the sum of the numbers in the line
4. `",".join(elementy)` joins the strings from the `elementy` list and separates them with a comma
5. `", ".join(str(l % 10) for l in liczby)` builds a string from the units digits of the numbers, separated by a comma and a space. `l % 10` gives a number, so I convert it to a string with `str` before joining

Output:

```
['12', '45', '7', '30']
[12, 45, 7, 30]
94
12,45,7,30
2, 5, 7, 0
```

### The string module - the `modul_string` function

I import the `string` module at the top of the file with `import string`. It contains ready-made constants with character sets. Instead of typing the alphabet or the digits by hand, you can use these constants right away, e.g. when checking properties of letters.

```python
def modul_string() -> None:
    print(string.ascii_letters)
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    print(string.digits)
    print(string.hexdigits)
    print(string.punctuation)
```

The module also has other constants, e.g. `octdigits`, `whitespace` and `printable`. It is worth looking at the module's documentation.

## Output

When run with the default `main` function, the program calls `modul_string()` and prints:

```
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
0123456789abcdefABCDEF
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

The output of the other functions is shown in their walkthroughs above.

## Implementation notes

Each topic has its own function annotated with `-> None`, and the calls are collected in the `main` function, which is run through `if __name__ == '__main__':`. This makes it easy to run only the chosen part of the lesson.

Methods that seem to change a string, such as `lower`, `replace` or `strip`, always return a new string. The original stays unchanged. You can see this in the `print(s2)` call in the `metody_dla_napisow` function, which still prints `kmPrograms` after all the operations.

Every string concatenation, including with the `+=` operator, creates a new object. With a very large number of such operations, the constant copying can slow the program down. Keep this in mind when solving Matura tasks.

When checking a character with comparisons, the `len(s4) == 1` condition guarantees that you are comparing a single character and not a longer string.

It is worth checking in the Python documentation how `isalpha`, `isalnum` and `isdigit` behave for strings longer than one character.

The lesson deliberately skips regular expressions. In this series I focus on what you need to implement solutions to Matura computer science tasks.