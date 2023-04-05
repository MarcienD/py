import Pobranie_logow

def generuj_raport():
    x = Pobranie_logow.czy_wadliwe()
    print(x)
    y = Pobranie_logow.licz_procent_wadliwych()
    print(y)
    z = Pobranie_logow.zwroc_prawidlowe()
    print('"Temperatura": {')
    slownik = Pobranie_logow.slownik_temperatur()
    print(f'\t"max": "{slownik["max"]}"')
    print(f'\t"min": "{slownik["min"]}"')
    print(f'\t"srednia": "{slownik["srednia"]}"')
    print("},")
    i = Pobranie_logow.licz_okresy_przegrzania()
    print('"liczba_okresow_przegrzania": ', i, ',')
    i = Pobranie_logow.czas_trwania()
    print(i)
gotowy_raport = generuj_raport()
print(gotowy_raport)

