# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 15:22:16 2016

@author: Przemysław Bieganski, bieg4n@gmail.com/ przemyslaw.bieganski88@gmail.com
"""
# importy modulow wbudowanych
import random

# importy modulow obcych
import pandas as pd

# import modulow wlasnych
import generator.common as common

# tabela zawiera nastepujace atrybuty:
# id podmiotu gospodarczego
# telefon_firma
# kod_pocztowy
# ulica
# miejscowosc
# kraj (poki co tylko PL)


def dane_kontaktowe(generator, number, id_podmiotu):
    ''' Generowanie danych kontaktowych dla podmiotow gospodarczych.
    Argumenty funkcji:
    generator - obiekt generator fake- factory
    number - integer z liczba podmiotow gospodarczych
    NIPy - lista zawierajaca nipy kolejnych podmiotow gospodarczych
    '''
    # id podmiotu gospodarczego
    df1 = pd.DataFrame(id_podmiotu, columns=['id_podmiotu'])
    print "\nGeneruje dane kontaktowe.."
    # adres i numer telefonu
    telefony, mail, kod, ulica = [], [], [], []
    miejscowosc, mieszkanie, wynajem, kraje = [], [], [], []
    for num in range(number):
        # kraj pochodzenia
        kraj = 'Polish'
        kraje.append(kraj)
        # kod pocztowy
        kod.append(generator.postcode())
        # ulica
        ulica.append(u'ul. {}'.format(common.dodaj_ulice(kraj)))
        # miejscowosc
        miejscowosc.append(common.dodaj_miasto(kraj))
        #numer telefonu
        tel = '+ 48 {}'.format(common.rwnd(10))
        telefony.append(tel)
        if num % (number/10) == 0:
            print 'postep : {} %'.format((float(num)/float(number))*100)
        # adres email kontaktowy
        mail.append(generator.safe_email())
        # siedziba - czy mieszkanie prywatne oraz czy zgloszono wynajem
        test = random.randint(1, 9)
        if test >= 7:
            mieszkanie.append('Tak')
            test = random.randint(1, 9)
            if test >= 7:
                wynajem.append('Nie')
            else:
                wynajem.append('Tak')
        else:
            mieszkanie.append('Nie')
            wynajem.append('Tak')

    # konwersja list do data frame
    df2 = pd.DataFrame(kod, columns=['kod_pocztowy'])
    df3 = pd.DataFrame(miejscowosc, columns=['miejscowosc'])
    df4 = pd.DataFrame(ulica, columns=['ulica'])
    df5 = pd.DataFrame(telefony, columns=['telefon_kontaktowy'])
    df6 = pd.DataFrame(mail, columns=['adres_mail_kontaktowy'])
    df7 = pd.DataFrame(mieszkanie, columns=['mieszkanie_prywatne'])
    df8 = pd.DataFrame(wynajem, columns=['zgloszony_wynajem'])
    # kraj
    df9 = pd.DataFrame(kraje, columns=['kraj'])

    # zwraca zlaczone data frame'y
    return pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], axis=1)
