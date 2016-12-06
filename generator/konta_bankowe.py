# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:47:10 2016

@author: Przemysław Bieganski, bieg4n@gmail.com/ przemyslaw.bieganski88@gmail.com
"""

import pandas as pd
import common
import random

lista_bankow = [u'Aareal Bank', u'Alior Bank', u'Banif Plus Bank', u'Bank BGŻ BNP Paribas',
u'Bank BPH', u'Bank Gospodarstwa Krajowego', u'Bank Handlowy', u'Bank Millennium',
u'Bank Ochrony Środowiska', u'Bank of China', u'Bank of Tokyo-Mitsubishi UFJ Polska',
u'Bank Pocztowy', u'Bank Polska Kasa Opieki', u'Bank Zachodni WBK', u'Banque PSA Finance',
u'BNP Paribas', u'BNP Paribas Securities Services', u'BPI Bank Polskich Inwestycji', u'CAIXABANK',
u'Citibank Europe', u'Credit Agricole Bank Polska', u'Danske Bank', u'Deutsche Bank Polska',
u'DNB Bank Polska', u'DZ Bank AG', u'Elavon Financial Services', u'Euro Bank', u'EUROCLEAR Bank',
u'FCE Bank Polska', u'Fiat Bank Polska', u'FM Bank PBP', u'Getin Noble Bank', u'Haitong Bank, S.A., Oddział w Polsce',
u'HSBC Bank Polska', u'Idea Bank', u'Ikano Bank', u'Industrial and Commercial Bank of China',
u'ING Bank Śląski', u'Intesa Sanpaolo', u'J.P. Morgan Europe', u'mBank', u'Mercedes-Benz Bank Polska',
u'Nordea Bank', u'Nykredit Realkredit', u'Pekao Bank Hipoteczny', u'PKO Bank Hipoteczny', u'Plus Bank',
u'Powszechna Kasa Oszczędności Bank Polski SA (Inteligo)', u'Raiffeisen Polbank', u'RBS Bank', u'RCI Banque',
u'Santander Consumer Bank', u'Saxo Bank', u'Skandinaviska Enskilda Banken', u'Société Générale',
u'Svenska Handelsbanken', u'Sygma Banque', u'Toyota Bank Polska', u'UBS', u'Vanquis Bank',
u'Volkswagen Bank Polska', u'Western Union']

def generuj_konta_bankowe(min, max, podmioty, typ = 'osoba', banki = lista_bankow ):
    '''
    Tworzy listę kont bankowych przypisanych do konkretnych podmiotow.
    Parametry wejsciowe:
    min - minimalna ilosc kont na podmiot,
    max - maksymalna ilosc kont na podmiot,
    ilosc_podmiotow - dla ilu podmiotow maja byc wygenerowane konta,
    banki - lista bankow w postaci listy
    typ - czy generowane jest konto dla podmiotu gospodarczego czy prywatne,
    dopuszczalne artosci ['podmiot', 'osoba']
    '''
    print '\nGenerowanie numerow kont bankowych...'
    zakres = range(min, max+1)
    konta, numery_podmiotow, oddzialy_bankow = [], [], []
    
    suma, iterator = len(podmioty), 0
    for podmiot in podmioty:
        ilosc = random.choice(zakres) # losuje ilosc kont dla podmiotu
        # brak kontroli unikalnosci numeru konta!!! dodac pozniej
        for x in range(ilosc):
            # numer konta
            k = str(common.rwNd(22))
            konto = '{} {} {} {} {} {}'.format(k[:2], k[2:6], k[6:10], k[10:14], k[14:18], k[18:22])
            konta.append(konto)
            # id podmiotu
            numery_podmiotow.append(podmiot)
            #oddzialy_bankow
            oddzialy_bankow.append(random.choice(banki))
        if iterator % (suma/10) == 0: print 'postep : {} %'.format((float(iterator)/float(suma))*100)
        iterator += 1
    
    # tworzenie unikalnego identyfikatora
    if typ == 'podmiot':
        prefix = 'KONTO_P_'
    else:
        prefix = 'KONTO_O_'
    
    identyfikatory = [(prefix + str(x)) for x in range(1, len(konta)+ 1)]
    
    # zapis list do data frame
    df0 = pd.DataFrame(identyfikatory, columns = ['id_konta'])
    df1 = pd.DataFrame(numery_podmiotow, columns=['id_podmiotu'])
    df2 = pd.DataFrame(konta, columns=['numer_konta'])
    df3 = pd.DataFrame(oddzialy_bankow, columns=['nazwa_banku'])
    
    
    print 'postep : 100 %'
    
    return pd.concat([df0, df1, df2, df3], axis=1)
