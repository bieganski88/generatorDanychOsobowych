# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 09:45:12 2016

@author: Przemysław Bieganski, bieg4n@gmail.com/ przemyslaw.bieganski88@gmail.com
"""
import json
import pandas as pd

# wczytywanie kodow z json'a
with open('./generator/pkd.json') as data_file:
    PKD = json.load(data_file)

def tworz_pkd(pkde=PKD):
    '''
    Wczytuje liste kodow PKD z pliku JSON.
    Dzieli ciąg znakow na kolumny i zapisuje do pandas data frame.
    '''
    tresc, kody = [], []

    # odzielam tresc od kodow
    dlugosc_listy = len(pkde)
    for k in range(dlugosc_listy):
        tresc.append(pkde[k][28:])
        kody.append(pkde[k][:28])

    # rozbijam kody na elementy atomowe
    wartosci, linia = [], []
    dlugosc_listy = len(kody)
    for k in range(dlugosc_listy):
        linia = kody[k][:-1].split("\t") + [tresc[k]]
        wartosci.append(linia)

    # create columns
    sekcja, dzial, grupa, klasa, symbol, opis = [], [], [], [], [], []
    dlugosc_listy = len(wartosci)
    for k in range(dlugosc_listy):
        sekcja.append(wartosci[k][0])
        dzial.append(wartosci[k][1])
        grupa.append(wartosci[k][2])
        klasa.append(wartosci[k][3])
        symbol.append(wartosci[k][4])
        opis.append(wartosci[k][5])

    # convert to data frame
    df0 = pd.DataFrame(sekcja, columns=['sekcja'])
    df1 = pd.DataFrame(dzial, columns=['dzial'])
    df2 = pd.DataFrame(grupa, columns=['grupa'])
    df3 = pd.DataFrame(klasa, columns=['klasa'])
    df4 = pd.DataFrame(symbol, columns=['symbol'])
    df5 = pd.DataFrame(opis, columns=['opis'])

    return pd.concat([df0, df1, df2, df3, df4, df5], axis=1)
