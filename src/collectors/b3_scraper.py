import requests
import base64
import json
from .api_client import BASE_URL, HEADERS, PAYLOAD_DICT
from ..models.ibov import IbovResponse


def obter_dados_ibov() -> IbovResponse:
    """
    Faz o request à API da B3 e retorna os dados validados com Pydantic
    """
    payload_str = json.dumps(PAYLOAD_DICT)
    b64_payload = base64.b64encode(payload_str.encode()).decode()
    url = f"{BASE_URL}/{b64_payload}"

    #print(f"🔍 Requisitando: {url}")
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()

    data = response.json()
    return IbovResponse(**data)