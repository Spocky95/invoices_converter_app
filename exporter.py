import pandas as pd

def export_to_excel(data_list, output_path="faktury.xlsx"):
    """
    Eksportuje listę słowników z danymi faktur do pliku Excel.
    """
    if not data_list:
        print("Brak danych do eksportu.")
        return

    df = pd.DataFrame(data_list)
    try:
        df.to_excel(output_path, index=False)
        print(f"Dane zostały wyeksportowane do pliku: {output_path}")
    except Exception as e:
        print(f"Błąd podczas zapisu do Excela: {e}")
