# -*- coding: utf-8 -*-
"""
Created on Wed Dec 07 12:37:49 2016

@author: Przemysław Bieganski, bieg4n@gmail.com/ przemyslaw.bieganski88@gmail.com
"""

# moduly firm trzecich
import pandas

# moduly wlasne
from generator import common # funkcje wykorzytywane w roznych  plikach
from generator import osoby_fizyczne as of
from generator import podmiot_kontakt as pk
from generator import podmiot_gospodarczy as pg
from generator import konta_bankowe as kb
from generator import udzialy_w_firmach as uf
from generator import pkd

def przetwarzanie(data):
    '''
    Glowny proces generowania danych. Z poziomu tej funkcji sa wywolywane
    wszystkie pozostale metody.
    Wejscie:
    data - wczytane parametry konfiguracyjne.
    Wyjscie:
    informacja o powodzeniu lub przerwaniu procesu.
    '''
    ###################### PRZYPISYWANIE ZMIENNYCH ##########################
    jezyk = data['jezyk']
    parametry_ilosciowe = data['parametry_ilosciowe']
    sciezki_zapisu = data['sciezki_zapisu']

    # deklaracja sciezek zapisu wygenerowanych danych
    xlsx_sciezka = sciezki_zapisu['xlsx']
    csv_sciezka = sciezki_zapisu['csv']

    # deklaracja parametrow ilosciowych
    liczba_osob = parametry_ilosciowe['liczba_osob']
    liczba_podmiotow_gospodarczych = parametry_ilosciowe['liczba_podmiotow']
    konta_na_podmiot = parametry_ilosciowe['konta_podmiot']
    konta_na_osobe = parametry_ilosciowe['konta_osoba']
    ilosc_udzialowcow = parametry_ilosciowe['ilosc_udzialowcow']

    ######################### WSTEP ##################################
    print "Witam w generatorze danych osobowych/podmiotowych/transakcynych"
    print "Wczytano nastepujace parametry konfiguracyjne:"

    print 'Liczba osob >> {}'.format(liczba_osob)
    print 'Podmioty gospodarcze >> {}'.format(liczba_podmiotow_gospodarczych)
    print 'Konta na podmiot >> {}'.format(konta_na_podmiot)
    print 'Konta na osobe >> {}'.format(konta_na_osobe)
    print 'Ilosc udzialowcow na podmiot >> {}'.format(ilosc_udzialowcow)

    print 'Sciezka zapisu plikow xlsx >> {}'.format(xlsx_sciezka)
    print 'Sciezka zapisu plikow csv >> {}'.format(csv_sciezka)
    print 'Wiodacy jezyk >> {}'.format(jezyk['wybrany_jezyk'])

    decyzja = raw_input("wpisz 'y' aby kontynuowac, cokolwiek innego zeby wyjsc..")
    if decyzja != 'y':
        return 'Zapraszam ponownie po poprawiemodyfikacji parametrów konfiguracyjnych!'

    ################ WYWOLANIA FUNKCJI GENERUJACYCH #####################
    # tworze generator
    fake_pl = common.create_generator(jezyk['wybrany_jezyk'])

    # TABELA  OSOBY_FIZYCZNE
    znajomosci = ['brak'] + ['male'] *10 + ['umiarkowane']*5 + ['duze']*2
    osoby_fizyczne = of.dane_osobowe(fake_pl, liczba_osob, znajomosci)
    #osoby_fizyczne.to_csv('export/csv/osoby_fizyczne.csv', encoding = 'utf-8')

    # TABELA KODY PKD
    kody_pkd = pkd.tworz_pkd()

    # TABELA PODMIOT GOSPODARCZY
    podmiot_gospodarczy = pg.dane_podmiotu(fake_pl, liczba_podmiotow_gospodarczych)
    temp = pg.przypisz_kody(kody_pkd, liczba_podmiotow_gospodarczych) # zawiera wylacznie kody PKD
    podmiot_gospodarczy = pandas.concat([podmiot_gospodarczy, temp], axis=1)

    # TABELA PODMIOT_KONTAKT
    podmiot_kontakt = pk.dane_kontaktowe(fake_pl, liczba_podmiotow_gospodarczych,
                                         podmiot_gospodarczy['id_podmiotu'].tolist())

    # TABELA UDZIALY W FIRMACH
    _, udzialowcy = uf.generuj_udzialowcow(ilosc_udzialowcow[0],
                                           ilosc_udzialowcow[1],
                                           osoby_fizyczne[['id_osoby', 'pochodzenie']],
                                           podmiot_gospodarczy[['id_podmiotu']])

    # TABELE KONTA BANKOWE PODMIOTOW oraz KONTA BANKOWE PRYWATNE
    konta_bankowe_podmiotow = kb.generuj_konta_bankowe(konta_na_podmiot[0],
                                                       konta_na_podmiot[1],
                                                       podmiot_gospodarczy['id_podmiotu'].tolist(),
                                                       'podmiot')

    konta_bankowe_prywatne = kb.generuj_konta_bankowe(konta_na_osobe[0],
                                                      konta_na_osobe[1],
                                                      osoby_fizyczne['id_osoby'].tolist(),
                                                      'osoba')

    konta_bankowe_prywatne.columns = ['id_konta', 'id_osoby', 'numer_konta', 'nazwa_banku']

    ########################### EKSPORT WYNIKOW ########################

    ######## PODMIOT GOSPODARCZY ##########
     # EXCEL
    print '\nZapisywanie do pliku excel..\nPrzy duzych zbiorach moze to potrwac kilka minut..'

    writer = pandas.ExcelWriter('{}/podmioty.xlsx'.format(xlsx_sciezka))
    podmiot_gospodarczy.to_excel(writer, 'informacje_podstawowe', index=False)
    podmiot_kontakt.to_excel(writer, 'podmiot_kontakt', index=False)
    konta_bankowe_podmiotow.to_excel(writer, 'konta_bankowe', index=False)
    udzialowcy.to_excel(writer, 'udzialowcy', index=False)
    #kody_pkd.to_excel(writer, 'A')
    writer.save()

    # CSV
    podmiot_gospodarczy.to_csv('{}podmioty_informacje_podstawowe.csv'.format(csv_sciezka),
                               sep=';', encoding='utf-8', index=False)

    podmiot_kontakt.to_csv('{}podmioty_kontakty.csv'.format(csv_sciezka),
                           sep=';', encoding='utf-8', index=False)

    konta_bankowe_podmiotow.to_csv('{}podmioty_konta_bankowe.csv'.format(csv_sciezka),
                                   sep=';', encoding='utf-8', index=False)

    udzialowcy.to_csv('{}podmioty_udzialowcy.csv'.format(csv_sciezka),
                      sep=';', encoding='utf-8', index=False)

    ######## OSOBY FIZYCZNE ##########
    # EXCEL
    writer = pandas.ExcelWriter('{}/osoby_fizyczne.xlsx'.format(xlsx_sciezka))
    osoby_fizyczne.to_excel(writer, 'informacje_podstawowe', index=False)
    konta_bankowe_prywatne.to_excel(writer, 'konta_bankowe', index=False)
    writer.save()

    # CSV
    osoby_fizyczne.to_csv('{}osoby_fizyczne_informacje_podstawowe.csv'.format(csv_sciezka),
                          sep=';', encoding='utf-8', index=False)

    konta_bankowe_prywatne.to_csv('{}osoby_fizyczne_konta_bankowe.csv'.format(csv_sciezka),
                                  sep=';', encoding='utf-8', index=False)

    udzialowcy.to_csv('{}osoby_fizyczne_udzialowcy.csv'.format(csv_sciezka),
                      sep=';', encoding='utf-8', index=False)

    return "Proces zakonczony powodzeniem!!"
