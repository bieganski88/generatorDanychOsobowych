# GENERATOR DANYCH OSOBOWYCH/PODMIOTOWYCH
### GŁÓWNE ZAŁOŻENIA
Generowanie danych dotyczacych osób fizycznych oraz podmiotów gospodarczych w oparciu o parametry konfiguracyjne zawarte w pliku JSON (opis parametrów poniżej). Jako baza do generowania dnaych służy moduł __faker__.
##### Zakres generowanych danych
---------------------
OSOBY FIZYCZNE:  
imię, nazwisko,  kraj pochodzenia, miasto, adres, kod pocztowy, numer telefonu, pesel, zawód, numer konta bankowego, nazwa banku.

PODMIOTY GOSPODARCZE:  
informacje ogólne >> nazwa firmy, regon, numer KRS, NIP, data rejestracji, forma prawna, ilośc kapitału własnego, dziedzina, dominująca działalność według PKD.  
informacje kontaktowe >> miejscowość, ulica, kod pocztowy, numer telefonu, adres email kontaktowy, siedziba mieszkanie prywatne czy biura, kraj rejestracji.  
informacje pozostałe >> numer konta bankowego, nazwa banku, informacje o udziałowcach (identyfikator osoby, pochodzenie, procent udziałów).  

### WYMAGANE BIBLIOTEKI ###

* pandas
* fake-factory
* json


### PLIK KONFIGURACYJNY
1 . Ścieżki zapisu danych wynikowych.
````
(..)
    "sciezki_zapisu": {
    	"xlsx": "./export/xlsx/",
    	"csv": "./export/csv/"
    },
(..)
````
__xlsx__ - ścieżka względna zapisu wygenerowanych danych w postaci arkusza kalkulacyjnego.  
__csv__ - ścieżka względna zapisu wygenerowanych danych w postaci plików csv.  

2.Parametry ilościowe:
````
(..)
	"parametry_ilosciowe": {
		"liczba_osob": 500,
		"liczba_podmiotow": 250,
		"konta_podmiot": [1, 5],
		"konta_osoba": [1, 2],
		"ilosc_udzialowcow": [1, 5]
	},
(..)
````
__liczba_osob__ - liczba rekordów z danymi osobowymi do wygenerowania  
__liczba_podmiotow__ - liczba fikcyjnych firm do wygenerowania, wraz z danymi adresowymi, numerami kont itd..  
__konta_podmiot__ - ilośc konta na firmę do wygenerowania, w postaci przedziału - pierwsza wartość min, druga wartość max.  
__konta_osoba__ - ilośc konta przypisanych do osoby fizycznej, w postaci przedziału - pierwsza wartość min, druga wartość max.  
__ilosc_udzialowcow__ - przypisanie udziałowców do firmy wraz z wartością udziału. Przypisywane są osoby z puli tych wczesniej wygenerowanych.  

3.Ustawienia językowe:
````
	"jezyk": {
		"dostepne_jezyki": {
			"Bulgarian": "bg_BG",
			"Czech": "cs_CZ",
			"German": "de_DE",
			"Danish": "dk_DK",
			"Greek": "el_GR",
			"Australia": "en_AU",
			"Canada": "en_CA",
			"English": "en_GB",
			"USA": "en_US",
			"Spanish": "es_ES",
			"Mexico": "es_MX",
			"Persian": "fa_IR",
			"Finnish": "fi_FI",
			"French": "fr_FR",
			"Hindi": "hi_IN",
			"Croatian": "hr_HR",
			"Italian": "it_IT",
			"Japanese": "ja_JP",
			"Korean": "ko_KR",
			"Lithuanian": "lt_LT",
			"Latvian": "lv_LV",
			"Nepali": "ne_NP",
			"Dutch": "nl_NL",
			"Norwegian": "no_NO",
			"Polish": "pl_PL",
			"Brazil": "pt_BR",
			"Portugal": "pt_PT",
			"Russian": "ru_RU",
			"Slovene": "sl_SI",
			"Swedish": "sv_SE",
			"Turkish": "tr_TR",
			"China": "zh_CN",
			"Taiwan": "zh_TW"
		},
		"wybrany_jezyk": "Polish"
	}
````
__dostepne_jezyki__ - lista obsługiwanych języków przez wykorzystywany generator.  
__wybrany_jezyk__ - wiodący język będący bazą dla generowanych danych, wartość musi znajdować się w kluczach dostępnych języków. Parametr określający język jest przekazywany jako argument podczas tworzenia obiektu generatora z modułu __fake_factory__. W oparciu o język generowane są swojsko brzmiące imiona, nazwiska, miasta, ulice, nazwy firm.. 

### PROCES GENEROWANIE DANYCH ###
W celu uruchomienia procesu generowania danych należy odpalić plik __start.py__.  
Treśc pliku poniżej:
````
# moduly wlasne
from generator import common
import proces

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
