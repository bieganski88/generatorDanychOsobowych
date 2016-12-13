# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 17:24:33 2016

@author: Przemysław Bieganski, bieg4n@gmail.com/ przemyslaw.bieganski88@gmail.com
"""
# import modulow wbudowanych
import random

# import modulow obcych
import pandas as pd

def generuj_udzialowcow(minimum, maximum, osoby, podmioty):
    '''
    Generuje DataFrame zawierające powiazania ludzi z podmiotami gospodarczymi.
    Parametry wejsciowe to: min, max udzialowcow na podmiot.
    osoby - data frame zawierajace dwie kolumny - pesel oraz kod pochodzenia.
    podmioty - data frame zawierajace kolumne z nip'em
    '''
    zakres = range(minimum, maximum+1)
    pesele, nipy, udzialy, narodowosc = [], [], [], []
    # lista udzialowcow niebedna do pozniejszego generowania znajomosci
    lista_udzialowcow = []

    # data frame to list
    pesele_lista = osoby.ix[:, 0].tolist() # pesele
    narodowosci_lista = osoby.ix[:, 1].tolist() # narodowosc
    nip = podmioty.ix[:, 0].tolist()

    osoby = [] # redefiniuje zmienna
    for k in range(len(pesele_lista)): # paruje pesel z osoba
        osoby.append([pesele_lista[k], narodowosci_lista[k]])

    print '\nPrzypisywanie udzialowcow do podmiotow...'
    suma, iterator = len(nip), 0
    for podmiot in nip: # dla kazdego z podmiotow gospodarczych
        ilosc = random.choice(zakres) # wylosuj liczbe udzialowcow
        # nastepnie wylosuj pesele bez powtorek!!
        udzialowcy_podmiotu = []
        while len(udzialowcy_podmiotu) != ilosc:
            pesel = random.choice(osoby)
            if pesel not in udzialowcy_podmiotu:
                udzialowcy_podmiotu.append(pesel)
        # ustal wagi dla udzialowcow
        udzial = '{} %'.format(int((float(1)/float(ilosc))*100))
        # dodaj do list
        for udzialowiec in udzialowcy_podmiotu:
            nipy.append(podmiot)
            pesele.append(udzialowiec[0])
            narodowosc.append(udzialowiec[1])
            udzialy.append(udzial)
        # wpisanie udzialowcow do globalnej listy
        lista_udzialowcow.append(udzialowcy_podmiotu)
        # jedynie w celu ukazania postepu
        if iterator % (suma/10) == 0:
            print 'postep : {} %'.format((float(iterator)/float(suma))*100)
        iterator += 1

    # zapisz jako data frame
    id_udzialu = [('UDZIAL_{}'.format(x)) for x in range(1, len(nipy)+1)]
    df0 = pd.DataFrame(id_udzialu, columns=['id_udzialu'])
    df1 = pd.DataFrame(nipy, columns=['id_podmiotu'])
    df2 = pd.DataFrame(pesele, columns=['id_osoby'])
    df3 = pd.DataFrame(narodowosc, columns=['pochodzenie'])
    df4 = pd.DataFrame(udzialy, columns=['wartosc udzialow'])

    return lista_udzialowcow, pd.concat([df0, df1, df2, df3, df4], axis=1)
