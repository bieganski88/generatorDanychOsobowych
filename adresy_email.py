# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:42:48 2016

@author: Przemysław Bieganski, bieg4n@gmail.com/ przemyslaw.bieganski88@gmail.com
"""

import pandas as pd
import random

def generuj_adresy_mail(generator, min, max, osoby):
    '''
    Tworzy Data Frame zawierajace zestawione adresy email wraz z peselem osoby,
    ktora ten mail posiada.
    Parametry wejsciowe to: min, max maile na osobe.
    osoby - pesele wszystkich osob.
    '''
    print '\nGenerowanie adresow email...'
    zakres = range(min, max+1)
    emaile, pesele = [], []
    
    suma, iterator = len(osoby), 0
    for osoba in osoby:
        ilosc = random.choice(zakres) # losuje ilosc adresow email dla danej osoby
        for x in range(ilosc):
            # pesel
            pesele.append(osoba)
            # adres email
            mail = '{}_{}@fake_{}'.format(osoba, x, generator.free_email_domain())
            emaile.append(mail)
        if iterator % (suma/10) == 0: print 'postep : {} %'.format((float(iterator)/float(suma))*100)
        iterator += 1
    
    # zapis do data frame
    df0 = pd.DataFrame(range(1, len(emaile) + 1), columns = ['id_adresu_email'])
    df1 = pd.DataFrame(emaile, columns=['adres_poczty_email'])
    df2 = pd.DataFrame(pesele, columns=['id_osoby'])

    return pd.concat([df0, df1, df2], axis=1)