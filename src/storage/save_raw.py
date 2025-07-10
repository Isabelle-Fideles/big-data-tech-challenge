# src/storage/save_raw.py

import os
import pandas as pd
from datetime import datetime
from src.models.ibov import IbovResponse
from src.utils.helpers import parse_b3_date


def save_raw_ibov_data(data: IbovResponse, output_dir: str = "data/bronze") -> str:
   """
   Salva os dados da API da B3 (pages + header + results) em um único arquivo Parquet.
   O arquivo é salvo em: data/bronze/YYYY-MM-DD/dados_originais.parquet
   """
  
 # Extrai a data e cria o subdiretório
   iso_date = parse_b3_date(data.header.date)
   subdir = os.path.join(output_dir, iso_date)
   os.makedirs(subdir, exist_ok=True)

   # Converte header e page para dict e prefixa campos para evitar conflito
   header_dict = {f"header_{k}": v for k, v in data.header.model_dump(by_alias=True).items()}
   page_dict = {f"page_{k}": v for k, v in data.page.model_dump(by_alias=True).items()}

   # Transforma cada resultado e inclui metadados
   results_list = [item.model_dump(by_alias=True) for item in data.results]
   full_data = [{**item, **header_dict, **page_dict} for item in results_list]

   # DataFrame final com todos os dados
   df = pd.DataFrame(full_data)
   print(df.columns)

   # Salva como Parquet
   output_path = os.path.join(subdir, "dados_originais.parquet")
   df.to_parquet(output_path, index=False)

   return output_path
