from pdf_reader import extract_text_from_pdf, is_pdf_text_based
import pandas as pd
from parser import process_invoice_text, parse_invoice
from OCR_Parser import run_ocr_on_pdf
from exporter import export_to_excel
from pathlib import Path

def main():
    samples_dir = Path("samples")
    if not samples_dir.exists():
        print(f"Błąd: Katalog '{samples_dir}' nie istnieje.")
        return

    all_data = []

    for file_path in samples_dir.rglob("*.pdf"):
        print(f"--- ANALIZA PLIKU: {file_path.name} ---")

        if is_pdf_text_based(str(file_path)):
            print("To jest plik tekstowy - pobieram dane...")
            invoice_text = extract_text_from_pdf(str(file_path))
            processed_data = process_invoice_text(invoice_text)
            all_data.append(processed_data)
        else:
            print("Plik wygląda na skan (brak tekstu). Uruchamiam funkcję OCR...")
            invoice_text = run_ocr_on_pdf(str(file_path))
            # Wywołujemy parse_invoice na tekście z OCR, jeśli funkcja to umożliwia
            processed_data = parse_invoice(invoice_text)
            processed_data["plik"] = file_path.name # Dodajemy informację o pliku dla skanów
            all_data.append(processed_data)

    if all_data:
        export_to_excel(all_data)
    else:
        print("Nie znaleziono danych do eksportu.")






if __name__ == "__main__":
    main()