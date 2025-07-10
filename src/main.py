# src/main.py

from src.collectors.b3_scraper import obter_dados_ibov
from src.models.ibov import IbovResponse
from src.storage.save_raw import save_raw_ibov_data
from src.storage.s3_storage import upload_to_s3
from src.storage.local_storage import save_raw_json
import os
import logging

logging.basicConfig(level=logging.INFO)

def main():
    try:
        logging.info("🔍 Iniciando extração de dados do IBOV via API da B3...")
        dados: IbovResponse = obter_dados_ibov()
        # Salvar localmente
        local_path = save_raw_ibov_data(dados)
        #file_name = os.path.basename(local_path)
        #s3_key = f"bronze/{file_name}"

        # Salva JSON bruto
        json_path = save_raw_json(dados)

        # Enviar para S3
        upload_to_s3(local_path)

        # Exibindo um resumo dos dados
        print("\n📅 Data de referência:", dados.header.date)
        print("📈 Total de ativos recebidos:", len(dados.results))
        print("📄 Página atual:", dados.page.page_number)
        print("📄 Total de páginas:", dados.page.total_pages)
        #print(f"\n✅ Dados salvos em: {file_name }")
        print(f"📄 JSON bruto salvo em: {json_path}")

        # Exibir os 3 primeiros ativos como exemplo
        print("\n🧾 Primeiros ativos:")
        for item in dados.results[:3]:
            print(f" - {item.cod}: {item.asset} ({item.type}) — Part: {item.part}")

    except Exception as e:
        logging.error(f"❌ Erro ao obter dados: {e}")

if __name__ == "__main__":
    main()
