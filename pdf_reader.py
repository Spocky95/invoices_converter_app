from pypdf import PdfReader


def extract_text_from_pdf(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    pages_text = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages_text.append(text)

    full_text = "\n".join(pages_text).strip()
    return full_text


def is_pdf_text_based(pdf_path: str) -> bool:
    """
    Sprawdza, czy PDF zawiera tekst (warstwę tekstową).
    Jeśli nie, prawdopodobnie jest skanem/obrazem wymagającym OCR.
    """
    text = extract_text_from_pdf(pdf_path)
    # Jeśli wyodrębniony tekst jest zbyt krótki (np. tylko kilka znaków śmieciowych),
    # możemy uznać, że to skan, ale na razie prosty check na puste.
    return len(text) > 0