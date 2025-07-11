BASE_URL = "https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay"

# Payload em formato dicionário (será codificado em base64)
PAYLOAD_DICT = {
    "language": "pt-br",
    "pageNumber": 1,
    "pageSize": 500,
    "index": "IBOV",
    "segment": "2"
}

# Headers da requisição GET
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json",
}
