from pdf_reader import extract_text_from_pdf
import pandas as pd
from parser import parse_invoice

def main():
    #import danych z pdf
    pdf_path = "samples/faktura2-fakturownia.pdf"
    text_faktura_example = extract_text_from_pdf(pdf_path)
    #import danych z pdf

    #Parsowanie danych
    data = parse_invoice(text_faktura_example)
    #Parsowanie danych

    #Wyswietl all
    print("=== TEKST Z PDF ===")
    print(text_faktura_example)
    #Wyswietl all

    #Wyswietl parsowane dane
    print("=== PARSOWANE DANE ===")
    print(data)
    #Wyswietl parsowane dane



if __name__ == "__main__":
    main()