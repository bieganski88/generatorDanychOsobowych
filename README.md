# README #

### WYMAGANE BIBLIOTEKI ###

* numpy
* pandas
* fake-factory
* random


### GENEROWANIE DANYCH ###

Odpalac bezpośrednio można poprzez plik START_GENERATOR.bat.
W pliku PARAMETRY_KONFIGURACYJNE.py zawarte są wszelkie niezbedne zmienne dzięki,
którym można modyfikować ilość generowanych danych, jak również ścieżki zapisu
plików wynikowych.



##### GENERWOANIE - spis plików #####

* generator.py -- główny plik, odpalający sekwencyjnie wszystkie pozostałe pliki, zapis do Excela // można zmodyfikowac na CSV, JSON, SQL
* PARAMETRY_KONFIGURACYJNE.py -- zawiera parametry konfiguracyjne

**
* adresy_email.py
* bilingi.py
* faktury_vat.py - 
* klasyfikacja_towarow.py
* konta_bankowe.py
* osoby_fizyczne.py
* partnerzy_handlowi.py
* pkd.py
* podmiot_gospodarczy.py
* podmiot_kontakt.py
* przelewy_bankowe.py
* udzialy_w_firmach.py
* znajomi.py
* common.py -- kilka powszechnie używanych funkcji


### TRANSFORMACJA PLIKOW XLSX ###

W folderze trojki znajduje się plik konwerterXLSX.py oraz (powinny się znajdować) dwa foldery 'src' oraz 'dest'.
'src' - dane oryginalnie wygenerowane, 'dest' - dane po konwersji.