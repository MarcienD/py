from datetime import datetime
import copy


o = open("wejscie.txt")
logi = o.read()
logi = logi.split('\n')
logi = [l.split(' ') for l in logi]

a = ['', '', '']
logi_pomocnicza = copy.deepcopy(logi)
n = 0
for x in logi_pomocnicza:
    y = logi_pomocnicza[n].extend(a)
    n += 1

daty = []
czasy = []
temperatury = []

x = 0
for i in logi:
    daty.append(logi_pomocnicza[x][0])
    czasy.append(logi_pomocnicza[x][1])
    temperatury.append(logi_pomocnicza[x][2])
    temperatury_edit = [t.strip('C') for t in temperatury]
    temperatury_edit = [t.replace(".", "") for t in temperatury]
    daty_edit = [d.replace('-', '') for d in daty]
    czasy_edit = [c.replace(':', '') for c in czasy]
    x += 1


def czy_wadliwe():
    wadliwe = []
    i = 0
    for data in daty:
        if not daty_edit[i].isdigit() or not czasy_edit[i].isdigit() or not temperatury_edit[i].isdigit():
            wadliwe.append(logi[i])
        else:
            pass
        i += 1
    return wadliwe

def licz_procent_wadliwych():
    wadliwe_logi = czy_wadliwe()
    procent_wadliwych_logow = 100.0
    procent_wadliwych_logow = round((len(wadliwe_logi) / len(logi) * 100), 1)
    return procent_wadliwych_logow


def zwroc_prawidlowe():
    wadliwe_logi = czy_wadliwe()
    for x in wadliwe_logi:
        logi.remove(x)
    return logi

def czas_trwania():
    dane = logi
    data_czas = []
    for x in dane:
        for c in x:
            x.pop()
        data_czas.append(x)
        x.append(c)
    if len(data_czas) > 1:
        start = data_czas[0][0], data_czas[0][1]
        stop = data_czas[len(data_czas) - 1][0], data_czas[len(data_czas) - 1][1]
        start = ' '.join([str(x) for x in start])
        stop = ' '.join([str(x) for x in stop])
        start = datetime.strptime(start, '%Y-%m-%d %H:%M')
        stop = datetime.strptime(stop, '%Y-%m-%d %H:%M')
        czas_raportu = (stop - start).total_seconds() / 60
    else:
        czas_raportu = 0
    return czas_raportu

def slownik_temperatur():
   slownik = {"max": None, "min": None, "srednia": None}
   temperatury = []
   n = 0
   for i in logi:
       temperatury.append(logi[n][2])
       n += 1
   temperatury = [t.strip('C') for t in temperatury]
   temperatury_float = list(map(float, temperatury))
   slownik["max"] = str(max(temperatury_float))
   slownik["min"] = str(min(temperatury_float))
   slownik["srednia"] = str(round(sum(temperatury_float) / len(temperatury_float), 1))
   return slownik

def licz_okresy_przegrzania():
    liczba_okresow_przegrzania = 0
    for log in logi:
        if float(log[2].strip('C')) > 100:
            liczba_okresow_przegrzania += 1
    return liczba_okresow_przegrzania
