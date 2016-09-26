# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 13:51:14 2016

@author: Przemysław Bieganski, bieg4n@gmail.com/ przemyslaw.bieganski88@gmail.com
"""
import pandas as pd
import common, random
# tabela składa sie z trzech kolumn:
# imie, nazwisko oraz pesel

def pesel(number):
    '''Generuje fikcyjny pesel dla osoby.
    unikalna 11 cyfrowa losowa liczba'''
    pesele = set()
    while len(pesele) != number:
        pesel = common.rwNd(11)
        pesele.add(pesel)
    return list(pesele)


def pochodzenie(number = 1):
    '''Parametr startowy: number - ilosc kodow do wylosowania.
    Zwraca liste kodow kraju wybrany losowo (z wagami).
    '''
    # TWORZE LISTE WSZYSTKICH WARTOSCI
    duzo = ['PL'] * 40
    srednio = ['GB', 'ES', 'FR', 'IT', 'NL'] * 2
    malo = ['CZ', 'DE', 'DK', 'GR']
    wszystko = duzo + srednio + malo
    
    # LOSUJE KODY
    kody = []
    for n in range(number):
        kody.append(random.choice(wszystko))
    
    # zwraca liste
    return kody
    


def dane_osobowe(generator, number, znajomosci):
    '''Generuje data frame, zawierajace imie, nazwisko oraz
    unikalny pesel. Dodatkowo kraj pochodzenia oraz liczbe znajomych
    z pewnego portalu spolecznosciowego.'''
    print "\nGeneruje dane osobowe.."
    osoby, znajomi = [], []
    for num in range(0, number): 
        osoba = generator.name()
        for ch in ['pan ', 'pani ']:
            osoba= osoba.replace(ch, '')
        osoby.append(osoba.split()[:2])
        znajomi.append(random.choice(znajomosci))
        # pasek postepu
        if num % (number/10) == 0: print 'postep : {} %'.format((float(num)/float(number))*100)
    
    kraj = pochodzenie(number)
    # miasto zgodne z danym krajem
    miasta = []
    for kr in kraj: 
        miasta.append(common.dodaj_miasto(kr))
    
    id_osoby = [('OSOBA_' + str(x)) for x in range(1, number +1)]
    df0 = pd.DataFrame(id_osoby, columns = ['id_osoby'])      
    df1 = pd.DataFrame(osoby, columns=['imie', 'nazwisko'])
    df2 = pd.DataFrame(kraj, columns = ['pochodzenie'])
    df3 = pd.DataFrame(miasta, columns = ['adres'])
    df4 = pd.DataFrame(pesel(number), columns = ['pesel'])
    df5 = pd.DataFrame(znajomi, columns = ['znajomosci'])
    
    
    return pd.concat([df0, df1, df2, df3, df4, df5], axis=1)