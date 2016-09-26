# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 12:29:02 2016

@author: Przemysław Bieganski, bieg4n@gmail.com/ przemyslaw.bieganski88@gmail.com
"""
import numpy as np
import pandas
import sys

import common # funkcje wykorzytywane w roznych  plikach
import osoby_fizyczne as of
import podmiot_kontakt as pk
import podmiot_gospodarczy as pg
import konta_bankowe as kb
import adresy_email as ae
import udzialy_w_firmach as uf
import pkd


from PARAMETRY_KONFIGURACYJNE import * # ładuje parametry ilosciowe generowanych danych

# Wstęp
print "Witam w generatorze danych osobowych/podmiotowych/transakcynych"
print "Prosze zweryfikowac czy ponizsze parametry konfiguracyjne sa prawidlowe??"

print 'Liczba osob >> {}'.format(liczba_osob)
print 'Podmioty gospodarcze >> {}'.format(liczba_podmiotow_gospodarczych)
print 'Konta na podmiot >> {}'.format(konta_na_podmiot)
print 'Konta na osobe >> {}'.format(konta_na_osobe)
print 'Adresy email na osobe >> {}'.format(adresy_mail_na_osobe)
print 'Ilosc udzialowcow na podmiot >> {}'.format(ilosc_udzialowcow)

decyzja = raw_input("wpisz 'y' aby kontynuowac, cokolwiek innego zeby wyjsc..")
if decyzja != 'y':
	sys.exit('Zapraszam ponownie po poprawie parametrów konfiguracyjnych!')

# tworze generator
fake_pl = common.create_generator('PL')


# TABELA  OSOBY_FIZYCZNE
znajomosci = ['brak'] + ['male'] *10 + ['umiarkowane']*5 + ['duze']*2
osoby_fizyczne = of.dane_osobowe(fake_pl, liczba_osob, znajomosci)
#osoby_fizyczne.to_csv('export/csv/osoby_fizyczne.csv', encoding = 'utf-8')


# TABELA KODY PKD
kody_pkd = pkd.tworz_pkd()


# TABELA PODMIOT GOSPODARCZY
podmiot_gospodarczy = pg.dane_podmiotu(fake_pl, liczba_podmiotow_gospodarczych)
temp =  pg.przypisz_kody(kody_pkd, liczba_podmiotow_gospodarczych) # zawiera wylacznie kody PKD
podmiot_gospodarczy = pandas.concat([podmiot_gospodarczy, temp], axis=1)


# TABELA PODMIOT_KONTAKT
podmiot_kontakt = pk.dane_kontaktowe(fake_pl, liczba_podmiotow_gospodarczych, podmiot_gospodarczy['id_podmiotu'].tolist(), 
                                     podmiot_gospodarczy['NIP'].tolist())


# TABELA UDZIALY W FIRMACH
lista_udzialowcow, udzialowcy = uf.generuj_udzialowcow(ilosc_udzialowcow[0], ilosc_udzialowcow[1], osoby_fizyczne[['id_osoby', 'pochodzenie']], podmiot_gospodarczy[['id_podmiotu']])


# TABELE KONTA BANKOWE PODMIOTOW oraz KONTA BANKOWE PRYWATNE
konta_bankowe_podmiotow = kb.generuj_konta_bankowe(konta_na_podmiot[0], konta_na_podmiot[1], podmiot_gospodarczy['id_podmiotu'].tolist(), 'podmiot')
konta_bankowe_prywatne = kb.generuj_konta_bankowe(konta_na_osobe[0], konta_na_osobe[1], osoby_fizyczne['id_osoby'].tolist(), 'osoba')
konta_bankowe_prywatne.columns = ['id_konta', 'id_osoby', 'numer_konta', 'nazwa_banku']


# TABELA ADRESY EMAIL
adresy_email = ae.generuj_adresy_mail(fake_pl, adresy_mail_na_osobe[0], adresy_mail_na_osobe[1], osoby_fizyczne['id_osoby'].tolist())


################ PODMIOT GOSPODARCZY ########################
 # EXCEL
print '\nZapisywanie do pliku excel..\nPrzy duzych zbiorach moze to potrwac kilka minut..'

writer = pandas.ExcelWriter(podmiot_sciezka)
podmiot_gospodarczy.to_excel(writer, 'informacje_podstawowe', index = False)
podmiot_kontakt.to_excel(writer, 'podmiot_kontakt', index = False)
konta_bankowe_podmiotow.to_excel(writer, 'konta_bankowe', index = False)
udzialowcy.to_excel(writer, 'udzialowcy', index = False)
#kody_pkd.to_excel(writer, 'A')
writer.save()

# CSV
podmiot_gospodarczy.to_csv('./export/csv/podmiot_gospodarczy_informacje_podstawowe.csv', sep=';', encoding='utf-8', index = False)
podmiot_kontakt.to_csv('./export/csv/podmiot_gospodarczy_podmiot_kontakt.csv', sep=';', encoding='utf-8', index = False)
konta_bankowe_podmiotow.to_csv('./export/csv/podmiot_gospodarczy_konta_bankowe.csv', sep=';', encoding='utf-8', index = False)
udzialowcy.to_csv('./export/csv/podmiot_gospodarczy_udzialowcy.csv', sep=';', encoding='utf-8', index = False)


############# OSOBY FIZYCZNE ####################
# EXCEL
writer = pandas.ExcelWriter(osoby_sciezka)
osoby_fizyczne.to_excel(writer, 'informacje_podstawowe', index = False)
konta_bankowe_prywatne.to_excel(writer, 'konta_bankowe', index = False)
adresy_email.to_excel(writer, 'adresy_email', index = False)
udzialowcy.to_excel(writer, 'udzialowcy', index = False)
writer.save()

# CSV
osoby_fizyczne.to_csv('./export/csv/osoby_fizyczne_informacje_podstawowe.csv', sep=';', encoding='utf-8', index = False)
konta_bankowe_prywatne.to_csv('./export/csv/osoby_fizyczne_konta_bankowe.csv', sep=';', encoding='utf-8', index = False)
adresy_email.to_csv('./export/csv/osoby_fizyczne_adresy_email.csv', sep=';', encoding='utf-8', index = False)
udzialowcy.to_csv('./export/csv/osoby_fizyczne_udzialowcy.csv', sep=';', encoding='utf-8', index = False)

print "Proces zakonczony powodzeniem!!"
print ""