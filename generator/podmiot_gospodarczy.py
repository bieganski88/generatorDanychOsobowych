# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 13:51:14 2016

@author: Przemysław Bieganski, bieg4n@gmail.com/ przemyslaw.bieganski88@gmail.com
"""

import pandas as pd
import common
import random

# tabela zawiera nastepujace atrybuty
# id podmiotu, bedace kluczem glownym //ok
# nazwa podmiotu
# regon
# KRS
# nip
# pesel_osoby (klucz obcy pochodzacy z osob fizycznych)
# data_rejestracji_KRS
# forma_prawna (wartosc z listy)
# kapital_zakladowy (wartosc z listy)
# glowny_kod_PKD
# calosc_udzialow (czy calosc w rekach prezesa)

def generuj_regon(number):
    '''
    9 lub 14 cyfrowy, 14 dla podmiotow dzialajacych w wielu wojewodztwach
    wagi 8 9 2 3 4 5 6 7 nastepnie suma mod 11 i to jest ostatnia cyfra.
    Parametr wejsiowy >> ile stworzyc unikalnych regonow.
    Zwraca liste regonow.
    '''
    regony = set()
    while len(regony) != number:
        r = str(common.rwNd(8))
        kontrolna = (int(r[0])*8 + int(r[1])*9 + int(r[2])*2 + int(r[3])*3 +
                    int(r[4])*4 + int(r[5])*5 + int(r[6])*6 + int(r[7])*7) % 11
        if kontrolna == 10: kontrolna = 0
        r = (r + str(kontrolna))
        regony.add(r)
        
    return list(regony)


def generuj_KRS(number, digit):
    '''
    Generuje numer KRS, o okreslonej poprzez parametr 'digit' dlugosci.
    '''
    liczba = range(4,7)
    KRS = set()
    while len(KRS) != number:
        x = random.choice(liczba)
        k = str(common.rwNd(x)).zfill(digit)
        KRS.add(k)
        
    return list(KRS)
    
def generuj_nip(number):
    '''
    dziesięciocyfrowy kod, służący do identyfikacji podatników w Polsce.
    wagi 6, 5, 7, 2, 3, 4, 5, 6, 7 nastepnie z sumy mod 11. nip nie moze miec
    cyfry kontrolnej 10.
    '''
    nipy = set()
    while len(nipy) != number:
        n = str(common.rwNd(9))
        kontrolna = (int(n[0])*6 + int(n[1])*5 + int(n[2])*7 + int(n[3])*2 +
                    int(n[4])*3 + int(n[5])*4 + int(n[6])*5 + int(n[7])*6 + int(n[8])*7) % 11
        if kontrolna == 10:
            continue
        else:
            kraj = common.losujKraj()
            n = (kraj + '-' + n + str(kontrolna))
            nipy.add(n)
            
    return list(nipy)


def generuj_forme(number):
    '''
    Generuje liste form prawnych spotykanych w Polsce.
    Dostepne formy prawne zapisane sa w listach ponizej.
    uwzglednione jest wagowanie. Parametr - dlugosc zwracanej listy.
    '''
    duzo = [u'spółka jawna', u'spółka partnerska', u'spółka komandytowa',
              u'spółka komandytowo-akcyjna', u'spółka z ograniczoną odpowiedzialnością',
              u'spółka akcyjna', u'spółka cywilna', u'przedsiębiorstwo prywatne osoby fizycznej'] * 8          
    srednio = [u'przedsiębiorstwo państwowe', u'przedsiębiorstwo państwowe', u'spółdzielnia',
               u'fundacja'] * 3
    # dla zalozonych po 01.05.2004 // czego poki co nie uwzglednilem       
    malo = [u'spółka europejska', u'europejskie zgrupowanie interesów gospodarczych', 
            u'spółdzielnia europejska', u'europejska spółka prywatna', u'europejska spółka wzajemna',
            u'stowarzyszenie europejskie']
    wszystkie = duzo + srednio + malo
    formy = []
    for num in range(number):
        forma = random.choice(wszystkie)
        formy.append(forma)
        
    return formy


def generuj_kapital(formy_prawne):
    '''
    Losuje wysokosc kapitalu zgodnie z przypisana forma prana do danego podmiotu.
    Tak aby zapital nie byl mniejszy niz prawnie dopuszczalny.
    Wejscie: lista form prawnych dla wszystkich podmiotow.
    Wyjscie: lista wysokosci kapitalow.
    '''
    kwoty = [5000, 10000, 25000, 50000, 100000, 250000, 500000, 1000000]
    kapital = []
    for forma in formy_prawne:
        if forma == u'spółka komandytowo-akcyjna': # min 50 000
            kwota = random.choice(kwoty[3:6])
        elif forma == u'spółka akcyjna': # min 100 000
            kwota = random.choice(kwoty[4:])
        elif forma == u'spółka z ograniczoną odpowiedzialnością': # min 100 000
            kwota = random.choice(kwoty[:4])
        elif forma == u'spółdzielnia europejska': # min 30 000 ok 120 000 zl
            kwota = random.choice(kwoty[5:])
        elif forma == u'spółka europejska': # 120 000 euro ok 500 000 zl
                kwota = random.choice(kwoty[6:])
        else:
            kwota = random.choice(kwoty)
        kapital.append(kwota)
        
    return kapital


def dane_podmiotu(generator, number):
    # id podmiotu gospodarczego
    print "\nGeneruje dane podmiotow gospodarczych.."
    id_podmiotow = [('PODMIOT_' + str(x)) for x in range(1, number +1)]
    df1 = pd.DataFrame(id_podmiotow, columns = ['id_podmiotu'])
    
    #delkaracja pustych list na dane
    nazwy, regony, KRSy, nipy, rejestracja = [], [], [], [], []
    formy, kapital = [], []
    
    for num in range(number):
    # nazwa_podmiotu df2
        nazwy.append(generator.company()) # TYMCZASOWE - BO DURNE NAZWY!!!!
    print 'postep: nazwy OK'
        
    # regon - rejestr gospodarki narodowej df3
    regony = generuj_regon(number)
    print 'postep: regony OK'
        
    # KRS df4
    KRSy = generuj_KRS(number, 11)
    print 'postep: KRS OK'
    
    # nip df5
    nipy = generuj_nip(number)
    print 'postep: nipy OK'
    
    # data rejestracji KRS df7
    # rok - miesiac - dzien || pelen zakres dat
    for num in range(number):
        data = '{}T00:00:00+01:00'.format(generator.date())
        rejestracja.append(data)
    print 'postep: rejestracja OK'
        
    # forma prawna df8
    formy = generuj_forme(number)
    print 'postep: forma OK'
    
    # kapital zakladowy df9
    kapital = generuj_kapital(formy)
    print 'postep: kapital OK'
    
    # usuniecie niepotrzebnych danych dla podmiotow zagranicznych
    for counter, nip in enumerate(nipy):
        if 'Polish' not in nip:
            regony[counter] = 'brak danych'
            KRSy[counter] = 'brak danych'
            formy[counter] = 'brak danych'
            kapital[counter] = 'brak danych'

    # konwersja list do data frame
    df2 = pd.DataFrame(nazwy, columns = ['nazwa_podmiotu'])
    df3 = pd.DataFrame(regony, columns = ['regon'])
    df4 = pd.DataFrame(KRSy, columns = ['numer_KRS'])
    df5 = pd.DataFrame(nipy, columns = ['NIP'])
    df7 = pd.DataFrame(rejestracja, columns = ['data_rejestracji'])
    df8 = pd.DataFrame(formy, columns = ['forma_prawna'])
    df9 = pd.DataFrame(kapital, columns = ['kapital_wlasny'])
    # zwraca zlaczone data frame'y
    return pd.concat([df1, df2, df3, df4, df5, df7, df8, df9], axis=1)


def przypisz_kody(kody_pkd, number):
    '''Przypisuje sekcje dzialalnosci do podmiotu,
    jak rowniez kod PKD szczegolowy.
    Parametry wejsciowe to:
    number - ilosc podmiotow gospodarczych,
    kody_pkd - data frame z kodami pkd'''
    
    # wycinek tabeli tylko z potrzebnymi kolumnami >> sekcja, symbol
    kody_subset =  kody_pkd.ix[:, ['sekcja', 'symbol']]
    # konwersja kolumn na sety
    sekcje_list = kody_subset['sekcja'].tolist()
    # puste listy na dane
    sekcje, symbole = [], []
    for k in range(number):
        # losowanie sekcji
        s = random.choice(sekcje_list)
        sekcje.append(s)
        # losowanie symbolu z danej sekcji
        kody_sekcja = kody_subset.query('sekcja == @s')
        symbole_list = kody_sekcja['symbol'].tolist()
        symbol = random.choice(symbole_list)
        symbole.append(symbol)
    
    # konwertuje lisy na data frame
    df0 = pd.DataFrame(sekcje, columns=['dziedzina'])
    df1 = pd.DataFrame(symbole, columns=['dominujaca dzialalnosc'])
    
    return pd.concat([df0, df1], axis=1)
    