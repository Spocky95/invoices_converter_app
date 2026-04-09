from pdf_reader import extract_text_from_pdf, is_pdf_text_based
import pandas as pd
from parser import process_invoice_text
from OCR_Parser import run_ocr_on_pdf
from pathlib import Path

def main():
    samples_dir = Path("samples")
    if not samples_dir.exists():
        print(f"Błąd: Katalog '{samples_dir}' nie istnieje.")
        return

    for file_path in samples_dir.glob("*.pdf"):
        print(f"--- ANALIZA PLIKU: {file_path.name} ---")

        if is_pdf_text_based(str(file_path)):
            print("To jest plik tekstowy - pobieram dane...")
            invoice_text = extract_text_from_pdf(str(file_path))

            processed_data = process_invoice_text(invoice_text)
        else:
            print("Plik wygląda na skan (brak tekstu). Uruchamiam funkcję OCR...")
            invoice_text = run_ocr_on_pdf(str(file_path))
            print(invoice_text)






if __name__ == "__main__":
    main()