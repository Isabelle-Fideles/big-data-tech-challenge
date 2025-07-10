from pydantic import BaseModel, Field
from typing import Optional, List

# Define o modelo para a seção 'page' da resposta da API
class Page(BaseModel):
    """
    Modelo Pydantic para a estrutura de paginação da resposta da API da B3.
    Mapeia nomes de campos JSON (camelCase) para Python (snake_case) usando Field(alias).
    """
    page_number: int = Field(alias="pageNumber", description="Número da página atual")
    page_size: int = Field(alias="pageSize", description="Tamanho da página (quantidade de registros por página)")
    total_records: int = Field(alias="totalRecords", description="Número total de registros disponíveis")
    total_pages: int = Field(alias="totalPages", description="Número total de páginas disponíveis")

# Define o modelo para cada item na seção 'results' (ou seja, cada ativo individual)
class IbovItem(BaseModel):
    """
    Modelo Pydantic para um item individual (ativo) dentro da seção 'results' da API.
    Os campos 'part' e 'theoricalQty' são mantidos como string aqui
    para refletir o formato bruto da API (com vírgulas e pontos para decimais/milhares).
    A conversão para float/int ocorrerá na camada de transformação (AWS Glue).
    """
    segment: Optional[str] = Field(description="Segmento do ativo (pode ser nulo)")
    cod: str = Field(description="Código de negociação do ativo (ex: ALOS3)")
    asset: str = Field(description="Nome do ativo (ex: ALLOS, AMBEV S/A)")
    type: str = Field(description="Tipo do ativo (ex: ON, ON ED NM)")
    part: str = Field(description="Participação do ativo na carteira teórica (formato string com vírgula decimal)")
    part_acum: Optional[str] = Field(alias="partAcum", description="Participação acumulada (pode ser nulo)")
    theorical_qty: str = Field(alias="theoricalQty", description="Quantidade teórica do ativo (formato string com pontos de milhar)")

# Define o modelo para a seção 'header' da resposta da API
class IbovHeader(BaseModel):
    """
    Modelo Pydantic para o cabeçalho da resposta da API da B3, contendo dados agregados.
    Os campos 'part', 'reductor' e 'theoricalQty' são mantidos como string
    para refletir o formato bruto da API. A conversão ocorrerá na camada de transformação.
    """
    date: str = Field(description="Data de referência dos dados ")
    text: str = Field(description="Texto descritivo para a quantidade teórica total")
    part: str = Field(description="Participação percentual total (ex: 100,000)")
    part_acum: Optional[str] = Field(alias="partAcum", description="Participação acumulada total (pode ser nulo)")
    text_reductor: str = Field(alias="textReductor", description="Texto descritivo para o redutor")
    reductor: str = Field(description="Valor do redutor (formato string com pontos e vírgula decimal)")
    theorical_qty: str = Field(alias="theoricalQty", description="Quantidade teórica total do índice (formato string com pontos de milhar)")

class IbovResponse(BaseModel):
    """
    Modelo Pydantic principal que encapsula a resposta completa da API do IBOV.
    Contém as seções de paginação, cabeçalho e a lista de resultados (ativos).
    Este modelo garante a validação da estrutura geral da resposta bruta.
    """
    page: Page = Field(description="Informações de paginação da resposta")
    header: IbovHeader = Field(description="Informações de cabeçalho e sumário do IBOV")
    results: List[IbovItem] = Field(description="Lista de ativos que compõem o índice IBOV")

'''
Isso espelha exatamente o formato de resposta da API da B3:

{
  "pages": {...},
  "header": { ... },
  "results": [ {...}, {...}, {...} ]
}
'''