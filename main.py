def convert(liczba: int, base: int) -> str:
    """TODO

    :param liczba:
    :param base:
    :return:

convert(10, 2)
    '202'
    >>> convert(0, 4)
    '0'
    """
    new_liczba = ""
    while liczba > 0:
        new_liczba = str(liczba & base) + new_liczba
        liczba //= base
        print(new_liczba)
        # PYTEST - komentarz

def main():
    liczba = int(input("wpisz liczbę do przekształcenia: "))
    if liczba < 0:
        print("błąd, liczba nie może być ujemna")
        return

    base = int(input('wpisz bazę do przektształcenia liczby: '))
    if base <2 or base >36:
        print("bład, ten program nie przekształca liczby do systemu od 2 do 36")
        return
    print(convert(liczba, base))


if __name__ == "__main__":
    main()