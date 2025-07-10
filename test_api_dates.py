import requests
import base64
import json
from datetime import datetime, timedelta

BASE_URL = "https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay"

def test_api_with_date(date_str=None):
    """
    Testa a API da B3 com diferentes datas
    """
    # Payload base
    payload = {
        "language": "pt-br",
        "pageNumber": 1,
        "pageSize": 500,
        "index": "IBOV",
        "segment": "1"
    }
    
    # Adiciona data se fornecida
    if date_str:
        payload["date"] = date_str
        print(f"🔍 Testando com data: {date_str}")
    else:
        print("🔍 Testando sem especificar data (padrão)")
    
    # Headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json",
    }
    
    # Codifica payload em base64
    payload_str = json.dumps(payload)
    b64_payload = base64.b64encode(payload_str.encode()).decode()
    url = f"{BASE_URL}/{b64_payload}"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        
        # Extrai informações relevantes
        header_date = data.get('header', {}).get('date', 'N/A')
        total_results = len(data.get('results', []))
        
        print(f"📅 Data retornada pela API: {header_date}")
        print(f"📈 Total de ativos: {total_results}")
        print(f"🔗 URL completa: {url}")
        print("-" * 50)
        
        return data
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return None

def main():
    print("🧪 Testando API da B3 com diferentes datas\n")
    
    # Data atual
    today = datetime.now()
    
    # Teste 1: Sem especificar data (padrão atual)
    test_api_with_date()
    
    # Teste 2: Com data atual
    today_str = today.strftime("%d/%m/%Y")
    test_api_with_date(today_str)
    
    # Teste 3: Com data de ontem
    yesterday = today - timedelta(days=1)
    yesterday_str = yesterday.strftime("%d/%m/%Y")
    test_api_with_date(yesterday_str)
    
    # Teste 4: Com data de 2 dias atrás
    two_days_ago = today - timedelta(days=2)
    two_days_ago_str = two_days_ago.strftime("%d/%m/%Y")
    test_api_with_date(two_days_ago_str)
    
    # Teste 5: Com data de 30/06/2025 (data que está sendo retornada)
    test_api_with_date("30/06/2025")
    
    # Teste 6: Com data de 30/06/2024 (ano passado)
    test_api_with_date("30/06/2024")

if __name__ == "__main__":
    main() 