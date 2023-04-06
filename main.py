import Brudy
import Pobranie_logow

def generuj_raport(sciezka):
    print("Wadliwe logi:")
    wadliwe_logi = Brudy.czy_wadliwe(sciezka)
    for log in wadliwe_logi:
        print(log)
    print('"Procent wadliwych logow": ', Brudy.licz_procent_wadliwych(sciezka))
    print('"Czas trwania raportu":', Brudy.czas_trwania(sciezka))
    print('"Temperatura": {')
    slownik = Brudy.slownik_temperatur(sciezka)
    print(f'\t"max": "{slownik["max"]}"')
    print(f'\t"min": "{slownik["min"]}"')
    print(f'\t"srednia": "{slownik["srednia"]}"')
    print("},")
    o = Brudy.licz_okresy_przegrzania(sciezka)
    print('"liczba_okresow_przegrzania": ', o, ',')


    return " "

print(generuj_raport("wejscie.txt"))

