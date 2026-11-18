import string

def podstawy() -> None:
    # Napis, czyli obiekt typu str, to ciąg znaków. Zapisuje się go w apostrofach albo w cudzysłowach. Oba zapisy
    # są równoważne. Napis wielowierszowy zapisuje się w potrójnych cudzysłowach.

    # Napisy są niemodyfikowalne. Nie można zmienić pojedynczego znaku. Każda operacja, na przykład zamiana
    # na wielkie litery albo sklejanie plusem, tworzy nowy napis.

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

    age = 18
    print("Wiek: " + str(age))
    print(f"Wiek: {age}")
    print("ab" * 3)

    s4 = f"""Pierwszy wiersz\
Drugi wiersz
Wiek: {age}"""
    print(s4)

    s5 = "Wiersz nr 1\nWiersz nr 2 z tabulatorem\tkoniec\nWiersz nr 3 z ukośnikiem \\"
    print(s5)

    s6 = r"Raw 1\nRaw 2\tRaw 3\\"
    print(s6)

    s7 = ["a", "b", "c"]
    s8 = "".join(s7)
    print(s8)
    s9 = ",".join(s7)
    print(s9)

    print(len(s9))
    print(list("kmprograms"))


def znaki_porownywanie_napisow() -> None:
    c1 = "a"
    print(ord(c1))
    # https://pl.wikipedia.org/wiki/ASCII

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

    codes = [80, 89, 84, 72, 79, 78]
    print("".join(chr(c) for c in codes))
    print([ord(c) for c in "Matura"])

    imiona = ["Ala", "aleksander", "ALICJA", "bogdan", "Bogumila"]
    print(sorted(imiona))
    print(sorted(imiona, key=str.lower))
    print(sorted(imiona, key=lambda imie: len(imie)))

    s4 = "a"
    print(len(s4) == 1 and "a" <= s4 <= "z")
    print(len(s4) == 1 and "A" <= s4 <= "Z")
    print(len(s4) == 1 and "0" <= s4 <= "9")

    # print(ord("ala"))

    print("".join([s3[i] for i in range(len(s3)) if s3[i] in "alb"]))


def metody_dla_napisow() -> None:
    s1 = "kmprograms"

    print(s1[0], s1[-1], s1[1:4], s1[2:])
    print(s1[::-1])
    print(s1[::2])
    print("prog" in s1)
    print(s1.index("r"))  # pierwsze wystąpienie
    print(s1.rindex("r"))  # ostatnie wystąpienie
    print(s1.find("m"))
    print(s1.rfind("m"))
    print(s1.count("r"))
    print(s1.startswith("km"))
    print(s1.endswith("ms"))
    print(min(s1))
    print(max(s1))

    s2 = "kmPrograms"
    print(s2.lower())
    print(s2.upper())
    print(s2.swapcase())
    print("ala ma kota".title())
    print("ala ma kota".capitalize())
    print(s2)

    s3 = "   tekst    "
    print(f"_{s3.strip()}_")
    print(f"_{s3.lstrip()}_")
    print(f"_{s3.rstrip()}_")

    print("kontakt@km-programs.pl".replace("k", "K"))  # zamienia wszystkie wystąpienia
    print("a-b-c".replace("-", "", 1))  # tylko pierwsze wystąpienie

    print("Ala ma kota".split())
    print("Ala-ma kota".split("-"))
    print("Ala ma kota".split(" ", 1))

    print("kontakt@km-programs.pl".partition("@"))
    print("89".zfill(6))
    print("89".center(6, "*"))

    print("a".isalpha())
    print("a".isalnum())
    print("1".isdigit())
    print("a".islower())
    print("A".isupper())
    print(" ".isspace())


def split_join_w_praktyce() -> None:
    linia = "12 45 7 30"

    elementy = linia.split()
    print(elementy)

    liczby = [int(e) for e in elementy]
    print(liczby)
    print(sum(liczby))

    print(",".join(elementy))
    print(", ".join(str(l % 10) for l in liczby))


def modul_string() -> None:
    print(string.ascii_letters)
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    print(string.digits)
    print(string.hexdigits)
    print(string.punctuation)
    

def main() -> None:
    # podstawy()
    # znaki_porownywanie_napisow()
    # metody_dla_napisow()
    # split_join_w_praktyce()
    modul_string()


if __name__ == '__main__':
    main()
