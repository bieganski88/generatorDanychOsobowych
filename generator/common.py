# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 16:11:56 2016

@author: Przemysław Bieganski, bieg4n@gmail.com/ przemyslaw.bieganski88@gmail.com
"""
# wbudowane moduly
import random
import os

# moduly zewnetrzne
import json
from faker import Factory

def sprawdz_konfiguracje(path):
    '''
    Wczytuje oraz sprawdza poprawnosc pliku konfiguracyjnego.
    Wejsciowe:
    path - sciezka do pliku JSON z parametrami konfiguracyjnymi.
    Wyjscie powodzenie:
    True - wczytywanie zakonczylo sie pomyslnie
    data - zawartosc wczytanego pliku JSON
    Wyjscie niepowodzenie:
    False - wczytywanie zakonczylo sie niepowodzeniem.
    data - komunikat o bledzie.
    '''
    # wczytywanie danych
    try:
        with open(path) as data_file:    
            data = json.load(data_file)
    except:
        return False, "Nieprawidlowa sciezka do pliku konfiguracyjnego"

    # czy istnieja zadeklarowane sciezki
    if os.path.isdir(data['sciezki_zapisu']['xlsx']) is False:
        return False, "Folder zapisu xlsx nie istnieje."

    if os.path.isdir(data['sciezki_zapisu']['csv']) is False:
        return False, "Folder zapisu csv nie istnieje."
    
    # czy wybrany jezyk glowny jest prawidlowy
    if data['jezyk']['wybrany_jezyk'] not in data['jezyk']['dostepne_jezyki'].keys():
        return False, "Wybrany jezyk poza zbiorem dostepnych jezykow."

    parametry = data['parametry_ilosciowe']
    
    # ilosc osob oraz podmiotow
    if (parametry['liczba_osob'] <= 0 or parametry['liczba_podmiotow'] <=0 or 
        parametry['konta_podmiot'][0] <= 0 or parametry['konta_podmiot'][1] <= 0
        or parametry['konta_osoba'][0] <= 0 or parametry['konta_osoba'][1] <= 0
        or parametry['ilosc_udzialowcow'][0] <= 0 or parametry['ilosc_udzialowcow'][1] <= 0):
        return False, "Parametry ilosciowe musza nalezec do liczb dodatnich calkowitych."

    # czy pierwszy parametr mniejszy od drugiego
    do_sprawdzenia = ['konta_podmiot', 'konta_osoba', 'ilosc_udzialowcow']
    for element in do_sprawdzenia:
        if parametry[element][0] > parametry[element][1]:
            return False, "Blad - {} - pierwszy parametr wiekszy od drugiego.".format(element)

    return True, data



def losujKraj():
    '''
    Zwraca losowy kraj obslugiwany przez generator.
    '''
    # TWORZE LISTE WSZYSTKICH WARTOSCI
    duzo = ['Polish'] * 40
    srednio = ['Czech', 'German', 'Danish', 'Greek', 'Australia', 'Canada',
        'English', 'USA', 'Spanish', 'Mexico', 'Finnish', 'French', 'Italian',
        'Dutch', 'Norwegian', 'Polish','Portugal', 'Russian', 'Slovene', 'Swedish'] * 2
    malo = ['Turkish', 'China', 'Taiwan', 'Nepali', 'Brazil', 'Japanese',
        'Korean', 'Hindi', 'Persian', 'Bulgarian', 'Lithuanian', 'Latvian']
    wszystko = duzo + srednio + malo
    
    return random.choice(wszystko)



def dodaj_miasto(language):
    '''
    Dodaje miasto lezace w zadeklarowanym miescie.
    Wejscie: kod dwuliterowy kraju, wyjscie string z nazwa miasta.
    '''
    generator =  create_generator(language)   
    string = generator.city()
    
    return string

   
    
def dodaj_ulice(language):
    '''
    Dodaje ulice o nazwie pasujacej do zadeklarowanego jezyka
    Wejscie: kod dwuliterowy kraju, wyjscie string z nazwa ulicy.
    '''
    generator =  create_generator(language)   
    string = generator.street_name()
    
    return string   
    


def create_generator(language):
    '''Tworzy generator fikcyjnych danych.
    Agrument wejsciowy: jezyk - musi znajdowac sie w zakresie kluczy
    zdefiniowanych w 'dostepnych jezykach'.
    Zwraca: obiekt generatora danych w podanych jezyku.
    '''
    
    dostepne_jezyki = {
			'Bulgarian': 'bg_BG', 'Czech': 'cs_CZ', 'German': 'de_DE',
			'Danish': 'dk_DK', 'Greek': 'el_GR', 'Australia': 'en_AU',
			'Canada': 'en_CA', 'English': 'en_GB', 'USA': 'en_US',
			'Spanish': 'es_ES', 'Mexico': 'es_MX', 'Persian': 'fa_IR',
			'Finnish': 'fi_FI', 'French': 'fr_FR', 'Hindi': 'hi_IN',
               'Italian': 'it_IT', 'Japanese': 'ja_JP',
			'Korean': 'ko_KR', 'Lithuanian': 'lt_LT', 'Latvian': 'lv_LV',
			'Nepali': 'ne_NP', 'Dutch': 'nl_NL', 'Norwegian': 'no_NO',
			'Polish': 'pl_PL', 'Brazil': 'pt_BR', 'Portugal': 'pt_PT',
			'Russian': 'ru_RU', 'Slovene': 'sl_SI', 'Swedish': 'sv_SE',
			'Turkish': 'tr_TR', 'China': 'zh_CN', 'Taiwan': 'zh_TW'
		}
    
    fake = Factory.create(dostepne_jezyki[language])
    
    return fake



def rwNd(n):
    '''Losowy INT o ścisle określonej dlugosci.'''
    from random import randint
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)



def paruj_klucze(kolumna1, kolumna2):
    ''' Paruje numeryczne identyfikatory obiektow z obecnym atrybutem sluzacym do identyfikacji.
    Wejsciowe: kolumna1, kolumna2 - kolumny w formacie data frame o tej samej dlugosci.
    Zwraca: slownik sparowanych wartosci 'stary identyfikator' : nowy id.
    '''
    slownik = {}
    stare_id = kolumna1.ix[:,0].tolist()
    nowe_id = kolumna2.ix[:,0].tolist()
    
    if len(stare_id) == len(nowe_id):
        for k in range(len(stare_id)):
            slownik[stare_id[k]] = nowe_id[k]
    else:
        print 'PARUJ KLUCZE >> PODANE KOLUMNY NIE SA ROWNEJ DLUGOSCI!'
    
    return slownik

