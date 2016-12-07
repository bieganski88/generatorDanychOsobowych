# -*- coding: utf-8 -*-
"""
Created on Mon Dec 06 12:29:02 2016

@author: Przemysław Bieganski, bieg4n@gmail.com/ przemyslaw.bieganski88@gmail.com
"""

# moduly wlasne
from generator import common
import proces

###########################################################################
# wczytywanie konfiguracji
print "Wczytywanie oraz weryfikacja konfiguracji.."
sukces, data = common.sprawdz_konfiguracje('parametry_konfiguracyjne.json')

if sukces:
    print "Weryfikacja zakończona pozytywnie..\n"
    wynik = proces.przetwarzanie(data)
else:
    print data
    print 'Prosze poprawic konfiguracje i sprobowac ponownie!'

print wynik
