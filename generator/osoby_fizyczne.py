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
    # LOSUJE KODY
    kody = []
    for n in range(number):
        kody.append(common.losujKraj())
    
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
    miasto = [generator.city() for _ in range(0, number)]
    dane_adresowe = [generator.street_address() for _ in range(0, number)]
    kod_pocztowy = [generator.postcode() for _ in range(0, number)]
    numer_telefonu = [generator.phone_number() for _ in range(0, number)]
    praca = [generator.job() for _ in range(0, number)]
    
    id_osoby = [('OSOBA_' + str(x)) for x in range(1, number +1)]
    df0 = pd.DataFrame(id_osoby, columns = ['id_osoby'])      
    df1 = pd.DataFrame(osoby, columns=['imie', 'nazwisko'])
    df2 = pd.DataFrame(kraj, columns = ['pochodzenie'])
    df3 = pd.DataFrame(miasto, columns = ['miasto'])
    df4 = pd.DataFrame(dane_adresowe, columns = ['adres'])
    df5 = pd.DataFrame(kod_pocztowy, columns = ['kod_pocztowy'])
    df6 = pd.DataFrame(numer_telefonu, columns = ['numer_telefonu'])
    df7 = pd.DataFrame(pesel(number), columns = ['pesel'])
    df8 = pd.DataFrame(praca, columns = ['zawod'])
    
    
    return pd.concat([df0, df1, df2, df3, df4, df5, df6, df7, df8], axis=1)