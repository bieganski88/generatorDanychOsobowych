# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 16:11:56 2016

@author: Przemysław Bieganski, bieg4n@gmail.com/ przemyslaw.bieganski88@gmail.com
"""
import random
import pandas


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
    '''Tworzy generator fikcyjnych danych:
    dostepne jezyki to : bg_BG - Bulgarian, cs_CZ - Czech, de_DE - German, dk_DK - Danish, el_GR - Greek, en_AU - English (Australia),
    en_CA - English (Canada), en_GB - English (Great Britain), en_US - English (United States), es_ES - Spanish (Spain),
    es_MX - Spanish (Mexico), fa_IR - Persian (Iran), fi_FI - Finnish, fr_FR - French, hi_IN - Hindi, hr_HR - Croatian,
    it_IT - Italian, ja_JP - Japanese, ko_KR - Korean, lt_LT - Lithuanian, lv_LV - Latvian, ne_NP - Nepali,
    nl_NL - Dutch (Netherlands), no_NO - Norwegian, pl_PL - Polish, pt_BR - Portuguese (Brazil), pt_PT - Portuguese (Portugal),
    ru_RU - Russian, sl_SI - Slovene, sv_SE - Swedish, tr_TR - Turkish, zh_CN - Chinese (China), zh_TW - Chinese (Taiwan)'''
    
    dostepne_jezyki = {'BG' : 'bg_BG', 'CZ' : 'cs_CZ', 'DE' : 'de_DE', 'DK' : 'dk_DK', 'GR' : 'el_GR', 'AU' : 'en_AU',
                       'CA' : 'en_CA', 'GB' : 'en_GB', 'US' : 'en_US', 'ES' : 'es_ES', 'MX' : 'es_MX', 'IR' : 'fa_IR',
                       'FI' : 'fi_FI', 'FR' : 'fr_FR', 'IN' : 'hi_IN', 'HR' : 'hr_HR', 'IT' : 'it_IT', 'JP' : 'ja_JP',
                       'KR' : 'ko_KR', 'LT' : 'lt_LT', 'LV' : 'lv_LV', 'NP' : 'ne_NP', 'NL' : 'nl_NL', 'NO' : 'no_NO',
                       'PL' : 'pl_PL', 'BR' : 'pt_BR', 'PT' : 'pt_PT', 'RU' : 'ru_RU', 'SI' : 'sl_SI', 'SE' : 'sv_SE',
                       'TR' : 'tr_TR', 'CN' : 'zh_CN', 'TW' : 'zh_TW'}
    
    from faker import Factory
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

