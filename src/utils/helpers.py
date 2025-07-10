# src/utils/helpers.py

from datetime import datetime

def parse_b3_date(date_str: str) -> str:
    """
    Converte a data retornada pela API da B3 (ex: '28/06/25') 
    para o formato ISO: '2025-06-28'.

    Args:
        date_str (str): Data no formato 'DD/MM/YY'.

    Returns:
        str: Data no formato 'YYYY-MM-DD'.
    """
    try:
        parsed_date = datetime.strptime(date_str, "%d/%m/%y").date()
        return parsed_date.isoformat()
    except ValueError as e:
        raise ValueError(f"Erro ao converter data '{date_str}': {e}")
