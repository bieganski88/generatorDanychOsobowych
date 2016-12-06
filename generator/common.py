# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 16:11:56 2016

@author: Przemysław Bieganski, bieg4n@gmail.com/ przemyslaw.bieganski88@gmail.com
"""
import random
from faker import Factory

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

