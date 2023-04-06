from datetime import datetime
import copy

def pobieranie(sciezka):
    o = open(sciezka)
    wszystkie_logi = o.read()
    wszystkie_logi = wszystkie_logi.split('\n')
    wszystkie_logi = [l.split(' ') for l in wszystkie_logi]
    return wszystkie_logi


def tworzenie_pomocniczej(sciezka):
    a = ['', '', '']
    logi_pomocnicza = copy.deepcopy(pobieranie(sciezka))
    n = 0
    for x in logi_pomocnicza:
        y = logi_pomocnicza[n].extend(a)
        n += 1
    return logi_pomocnicza


def obsluga_dat(sciezka):
    logi_pomocnicza = tworzenie_pomocniczej(sciezka)
    daty = []
    x = 0
    for i in logi_pomocnicza:
        daty.append(logi_pomocnicza[x][0])
        tablica_dat = [d.replace('-', '') for d in daty]
        x += 1
    return tablica_dat


def obsluga_temperatur(sciezka):
    logi_pomocnicza = tworzenie_pomocniczej(sciezka)
    temperatury = []
    x = 0
    for i in logi_pomocnicza:
        temperatury.append(logi_pomocnicza[x][2])
        temperatury = [t.strip('C') for t in temperatury]
        tablica_temperatur = [t.replace(".", "") for t in temperatury]
        x += 1
    return tablica_temperatur


def obsluga_czasow(sciezka):
    logi_pomocnicza = tworzenie_pomocniczej(sciezka)
    czasy = []
    x = 0
    for i in logi_pomocnicza:
        czasy.append(logi_pomocnicza[x][1])
        tablica_czasow = [c.replace(':', '') for c in czasy]
        x += 1
    return tablica_czasow


def czy_wadliwe(sciezka):
    wadliwe = []
    daty = obsluga_dat(sciezka)
    czasy = obsluga_czasow(sciezka)
    temperatury = obsluga_temperatur(sciezka)
    wszystkie_logi = pobieranie(sciezka)
    i = 0
    for data in daty:
        if not daty[i].isdigit() or not temperatury[i].isdigit() or not temperatury[i].isdigit():
            wadliwe.append(wszystkie_logi[i])
        else:
            pass
        i += 1
    return wadliwe


def zwroc_prawidlowe_logi(sciezka):
    wadliwe_logi = czy_wadliwe(sciezka)
    logi = pobieranie(sciezka)
    for x in wadliwe_logi:
        logi.remove(x)
    return logi


def licz_procent_wadliwych(sciezka):
    wadliwe_logi = czy_wadliwe(sciezka)
    prawidlowe_logi = zwroc_prawidlowe_logi(sciezka)
    procent_wadliwych_logow = 100.0
    procent_wadliwych_logow = round((len(wadliwe_logi) / len(prawidlowe_logi) * 100), 1)
    return procent_wadliwych_logow

def czas_trwania(sciezka):
    dane = zwroc_prawidlowe_logi(sciezka)
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

def slownik_temperatur(sciezka):
   slownik = {"max": None, "min": None, "srednia": None}
   temperatury = []
   logi = zwroc_prawidlowe_logi(sciezka)
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


def licz_okresy_przegrzania(sciezka):
    liczba_okresow_przegrzania = 0
    logi = zwroc_prawidlowe_logi(sciezka)
    for log in logi:
        if float(log[2].strip('C')) > 100:
            liczba_okresow_przegrzania += 1
    return liczba_okresow_przegrzania

'''
        czasy.append(logi_pomocnicza[x][1])
        temperatury.append(logi_pomocnicza[x][2])
        temperatury = [t.strip('C') for t in temperatury]
        temperatury_edit = [t.replace(".", "") for t in temperatury]
        czasy_edit = [c.replace(':', '') for c in czasy]
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
'''