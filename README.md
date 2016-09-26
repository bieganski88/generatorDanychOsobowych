# GENERATOR DANYCH OSOBOWYCH

### WYMAGANE BIBLIOTEKI ###

* numpy
* pandas
* fake-factory
* random


### GENEROWANIE DANYCH ###

Uruchmiać należy poprzez plik generator.py
W pliku PARAMETRY_KONFIGURACYJNE.py zawarte są wszelkie niezbedne zmienne dzięki, którym można modyfikować ilość generowanych danych, jak również ścieżki zapisu plików wynikowych.
**__WAŻNE__** : nie modyfikować nazw zmiennych w pliku konfiguracyjnym.

##### GENERWOANIE - spis plików #####

* generator.py -- główny plik, odpalający sekwencyjnie wszystkie pozostałe pliki, zapis wyników do Excela oraz CSV.
* PARAMETRY_KONFIGURACYJNE.py -- zawiera parametry konfiguracyjne

### ZAKRES GENEROWANYCH DANYCH ###

#### OSOBY FIZYCZNE
* informacje podstawowe w skład, których wchodzą: imie, nazwisko, pochodzenie, adres, pesel oraz stopień posiadnaych znajomości
* informacje o kontach bankowych: numer konta oraz nazwa banku
* adres email
* informacje o udziałach w firmach

#### PODMOTY GOSPODARCZE
* informacje podstawowe w skład, których wchodzą: nazwa formy, regon, KRD, NIP, data rejestracji, forma prawna, kapital oraz rodzaj prowadzonej działalności
* informacje kontaktowe: miejscowość, ulica, kod pocztowy, numer telefonu oraz adres email, jak i kraj rejestracji
* informacje o kontach bankowych: numer konta oraz nazwa banku