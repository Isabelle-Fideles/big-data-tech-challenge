# src/storage/local_storage.py

import os
import json
from src.utils.helpers import parse_b3_date
from src.models.ibov import IbovResponse

def save_raw_json(data: IbovResponse, output_dir: str = "data/raw") -> str:
    """
    Salva a resposta da API (IbovResponse) como JSON puro no diretório data/raw/.
    O nome do arquivo segue o padrão YYYY-MM-DD.json com base na data de referência da API.

    Args:
        data (IbovResponse): Objeto Pydantic contendo a resposta da API.
        output_dir (str): Diretório de destino para o JSON.

    Returns:
        str: Caminho completo do arquivo salvo.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Extrai a data de referência da resposta
    iso_date = parse_b3_date(data.header.date)
    file_path = os.path.join(output_dir, f"{iso_date}.json")

    # Converte para dict e salva como JSON
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data.model_dump(by_alias=True), f, ensure_ascii=False, indent=2)
     
    #by_alias=True: garante que os campos com alias (como partAcum, theoricalQty) 
    # sejam preservados como no JSON original da API.
    return file_path
