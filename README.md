# Invoice App

Aplikacja do odczytywania danych z faktur PDF, zarówno tekstowych, jak i zeskanowanych.  
Program przetwarza pliki z folderu `samples`, wyciąga tekst z PDF, a następnie parsuje podstawowe dane z faktury.

## Funkcje

- odczyt tekstu z plików PDF
- obsługa wielu plików z folderu `samples`
- wykrywanie, czy PDF jest tekstowy czy skanowany
- uruchamianie OCR dla zeskanowanych faktur
- parsowanie podstawowych danych:
  - numer faktury
  - data wystawienia
  - kwota do zapłaty

## Struktura projektu
