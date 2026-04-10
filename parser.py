import re


def process_invoice_text(invoice_text: str) -> dict:
    data = parse_invoice(invoice_text)

    print("Wyodrębnione dane:")
    print(data)
    print("-" * 40)

    return data


def find_first(patterns, text):
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return ""
def parse_invoice(text: str) -> dict:

    invoice_number = find_first([
        r"Faktura\s*(?:VAT)?\s*nr[:\s]*([A-Z0-9/\-]+)",
        r"Faktura\s*numer\s*([0-9/]+)"
    ], text)

    issue_date = find_first([
        r"Data\s*wystawienia\s*([0-9]{2}\.\s*[0-9]{2}\.\s*[0-9]{4})",
        r"Data\s*wystawienia[:\s]*([0-9]{2}[.\-]\s*[0-9]{2}[.\-]\s*[0-9]{4})",
        r"Data\s*wystawienia[:\s\r\n]+(?:[\w\.\s]+,\s*)?([0-9]{4}-[0-9]{2}-[0-9]{2})"
    ], text)

    amount = find_first([
        r"Razem\s*do\s*zapłaty[:\s]*([0-9\s,]+[.,][0-9]{2})",
        r"Do\s*zapłaty\s*([0-9\s,]+[.,][0-9]{2})"
    ], text)

    return {
        "numer_faktury": invoice_number,
        "data": issue_date,
        "kwota": amount
    }