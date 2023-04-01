import copy
import time
from collections import Counter
from datetime import datetime

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
    temperatury = [t.strip('C') for t in temperatury]
    temperatury_edit = [t.replace(".", "") for t in temperatury]
    daty_edit = [d.replace('-', '') for d in daty]
    czasy_edit = [c.replace(':', '') for c in czasy]
    x += 1


def czy_wadliwe():
    wadliwe = []

    i = 0
    for data in daty:
        if daty_edit[i].isdigit():
            pass
        else:
            wadliwe.append(logi[i])
        i += 1

    i = 0
    for czas in czasy:
        if czasy_edit[i].isdigit():
            pass
        else:
            wadliwe.append(logi[i])
        i += 1

    i = 0
    for temperatura in temperatury_edit:
        if temperatury_edit[i].isdigit():
            if float(temperatury_edit[i]) > 0:
                pass
        else: wadliwe.append(logi[i])
        i += 1

    wadliwe_logi = []
    [wadliwe_logi.append(log) for log in wadliwe if log not in wadliwe_logi]
    '''wadliwe_print = []
    for wiersz in wadliwe_logi:
        wadliwe_print.append(wiersz)
    for wiersz in wadliwe_print:
        print('"', ' '.join(wiersz), '"')'''

    return wadliwe_logi


wadliwe_logi = czy_wadliwe()
procent_wadliwych_logow = 100.0
procent_wadliwych_logow = round((len(wadliwe_logi)/len(logi) * 100), 1)


def zwroc_prawidlowe():
    for x in wadliwe_logi:
        logi.remove(x)
    return logi

def czas_trwania():
    data_czas = []
    for x in logi:
        for n in x:
            x.pop()
        data_czas.append(x)
        x.append(n)
    
def slownik_temperatur():
   slownik = {"max": None, "min": None, "srednia": None}
   temperatury = []
   n = 0
   for i in logi:
       temperatury.append(logi[n][2])
       n += 1
   temperatury = [t.strip('C') for t in temperatury]
   temperatury_float = list(map(float, temperatury))
   slownik["max"] = max(temperatury_float)
   slownik["min"] = min(temperatury_float)
   slownik["srednia"] = round(sum(temperatury_float) / len(temperatury_float), 1)
   return slownik
