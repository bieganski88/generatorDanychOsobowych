# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:24:25 2016

@author: Przemysław Bieganski, bieg4n@gmail.com/ przemyslaw.bieganski88@gmail.com
"""

# sciezki do zapisu wynikow
podmiot_sciezka = 'export/xlsx/podmiot_gospodarczy.xlsx'
osoby_sciezka = 'export/xlsx/osoby_fizyczne.xlsx'


# zmienne startowe >> ilosci generowanych danych
liczba_osob = 200
liczba_podmiotow_gospodarczych = 50
konta_na_podmiot = [1, 5] # min, max
konta_na_osobe = [1, 2] # min, max
adresy_mail_na_osobe = [1,2] # min, max
ilosc_udzialowcow = [1, 5] # min, max udzialowcow na podmiot