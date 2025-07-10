# Pipeline Batch Bovespa - POS Tech MLE

API para coleta dos dados da B3: "https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay"
- Fornece dados da carteeira diária da B3.

## 📋 Sumário

- [📋 Descrição](#-descrição)
- [🏗️ Arquitetura](#️-arquitetura)
- [🚀 Funcionalidades](#-funcionalidades)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [📦 Instalação](#-instalação)
- [🚀 Como Usar](#-como-usar)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [🔧 Componentes Principais](#-componentes-principais)
- [🔄 Fluxo de Desenvolvimento](#-fluxo-de-desenvolvimento)
- [📊 Dados Processados](#-dados-processados)
- [🔧 Desenvolvimento](#-desenvolvimento)
- [📝 Configurações](#-configurações)
- [🤝 Contribuição](#-contribuição)
- [📞 Suporte](#-suporte)
- [📚 Documentação Adicional](#-documentação-adicional)
- [🔄 Status do Projeto](#-status-do-projeto)

## 📋 Descrição

O pipeline de dados B3 é uma solução completa para coleta, processamento, transformação e armazenamento de dados financeiros do Ibovespa. O sistema foi desenvolvido seguindo uma arquitetura em camadas (Bronze e Silver) na AWS, fornecendo insights valiosos sobre o mercado financeiro brasileiro.

## 🏗️ Arquitetura

### Camadas de Dados
- **Bronze (Raw)**: Dados brutos exatamente como recebidos da API B3
- **Silver (Refined)**: Dados processados e separados (header e ativos)

### Componentes AWS
- **S3**: Armazenamento de dados em camadas
- **AWS Glue**: ETL e catalogação de dados
- **AWS Lambda**: Automação de pipeline
- **AWS Athena**: Consultas SQL nos dados
- **AWS QuickSight**: Visualização e BI (Opcional)

## 🚀 Funcionalidades

- **Coleta Automática**: Integração com APIs da B3 para coleta de dados do Ibovespa
- **Processamento ETL**: Transformação e limpeza de dados via AWS Glue
- **Armazenamento Escalável**: Sistema de armazenamento em camadas no S3
- **Automação**: Pipeline automatizado com Lambda e S3 Events
- **Análise**: Consultas SQL via Athena e visualizações no QuickSight
- **Validação**: Modelos Pydantic para validação de dados

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**: Linguagem principal do projeto
- **Pandas**: Manipulação e análise de dados
- **Boto3**: Integração com serviços AWS
- **Pydantic**: Validação de dados e configurações
- **FastParquet**: Processamento de arquivos Parquet
- **Requests**: Requisições HTTP para API B3
- **PyYAML**: Leitura de arquivos de configuração YAML

## 📦 Instalação

### Pré-requisitos

- Python 3.12 ou superior
- pip (gerenciador de pacotes Python)
- AWS CLI configurado
- Acesso aos serviços AWS (S3, Glue, Lambda, Athena)

### Configuração do Ambiente

1. **Clone o repositório**:
```bash
git clone <url-do-repositorio>
cd b3_data_pipeline
```

2. **Crie um ambiente virtual**:
```bash
python -m venv venv
```

3. **Ative o ambiente virtual**:

**Windows**:
```bash
venv\Scripts\activate
```

**Linux/Mac**:
```bash
source venv/bin/activate
```

4. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

### Configuração AWS

Configure suas credenciais AWS usando:

```bash
# Configurar credenciais AWS
aws configure

# Ou configurar um perfil específico
aws configure --profile b3-pipeline
```

**Informações necessárias:**
- AWS Access Key ID
- AWS Secret Access Key  
- Default region (ex: us-east-1)
- Default output format (json)

## 🚀 Como Usar

### Execução Local

```bash
# Ativar ambiente virtual
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Execute sempre a partir da raiz do projeto:
python -m src.main
```

### Estrutura de Dados Gerados

Após a execução, os dados são organizados em:

```
data/
├── bronze/                    # Dados brutos (Parquet)
│   └── YYYY-MM-DD/
│       └── dados_originais.parquet  # Header + Results juntos
└── raw/                      # Dados originais (JSON)
    └── YYYY-MM-DD.json       # Resposta completa da API
```

## 📁 Estrutura do Projeto

```
b3_data_pipeline/
├── 📄 README.md                    # Documentação principal
├── 📄 requirements.txt             # Dependências Python
├── 📄 fluxo de desenvolvimento.txt # Guia sequencial de implementação
├── 📄 arquitetura_aws.txt          # Diagrama da arquitetura AWS
├── 📁 venv/                       # Ambiente virtual Python
├── 📁 src/                        # Código fonte principal
│   ├── 📁 collectors/             # Coletores de dados
│   │   ├── b3_scraper.py         # Módulo principal de coleta
│   │   └── api_client.py         # Cliente HTTP para APIs
│   ├── 📁 models/                 # Modelos de dados Pydantic
│   │   └── ibov.py               # Modelos para dados do Ibovespa
│   ├── 📁 storage/                # Camada de armazenamento
│   │   ├── save_raw.py           # Salvar dados brutos em Parquet
│   │   ├── local_storage.py      # Armazenamento local
│   │   └── s3_storage.py         # Integração com AWS S3
│   ├── 📁 utils/                  # Utilitários gerais
│   │   ├── config.py             # Gerenciamento de configurações
│   │   └── helpers.py            # Funções auxiliares
│   └── main.py                   # Script principal de execução
├── 📁 data/                       # Dados processados localmente
│   ├── 📁 bronze/                # Camada Bronze - Dados brutos
│   └── 📁 raw/                   # Dados originais da API (JSON)
├── 📁 config/                     # Configurações
│   └── config.yaml               # Configurações do projeto
└── 📄 test_api_dates.py          # Script de teste de datas
```

## 🔧 Componentes Principais

### **1. `src/collectors/`**
- **`b3_scraper.py`**: Módulo principal que faz requisições HTTP para a API da B3, obtendo dados do Ibovespa
- **`api_client.py`**: Cliente HTTP reutilizável com configurações de timeout e headers

### **2. `src/models/`**
- **`ibov.py`**: Modelos Pydantic para validação da estrutura dos dados recebidos da API (pages, header e results)

### **3. `src/storage/`**
- **`save_raw.py`**: Função principal para salvar dados brutos em formato Parquet (pages + header + results juntos)
- **`local_storage.py`**: Operações de arquivo local
- **`s3_storage.py`**: Upload de dados para AWS S3

### **4. `src/utils/`**
- **`config.py`**: Gerenciamento de configurações do projeto
- **`helpers.py`**: Funções auxiliares reutilizáveis

### **5. `src/main.py`**
- Script principal que orquestra a coleta, validação e salvamento dos dados

## 🔄 Fluxo de Desenvolvimento

O projeto segue um fluxo de desenvolvimento sequencial conforme documentado em `fluxo de desenvolvimento.txt`:

### **Tarefa 1: Configuração do Ambiente Local** ✅
- Python 3.12 instalado
- Ambiente virtual configurado
- Dependências instaladas
- AWS CLI configurado

### **Tarefa 2: Desenvolvimento do Código de Extração e Salvamento Local** ✅
- Módulo `b3_scraper.py` implementado
- Modelos Pydantic em `ibov.py` definidos
- Função `save_raw.py` implementada
- Script principal `main.py` criado

### **Tarefa 3: Teste e Geração Inicial de Dados Locais** ✅
- Script `main.py` funcional
- Dados sendo gerados em `data/bronze/` e `data/raw/`

### **Próximas Tarefas:**
- **Tarefa 4**: Configuração inicial na AWS - S3 (Camada Bronze)
- **Tarefa 5**: Ingestão manual de dados para o S3
- **Tarefa 6**: Configuração do AWS Glue (Funções IAM)
- **Tarefa 7**: Desenvolvimento e execução do AWS Glue Job
- **Tarefa 8**: Verificação do Catálogo de Dados e teste de consultas (Athena)
- **Tarefa 9**: Configuração e desenvolvimento da automação (Lambda e S3 Events)
- **Tarefa 10**: Teste da automação de ponta a ponta
- **Tarefa 11**: Configuração de Business Intelligence (AWS QuickSight)

## 📊 Dados Processados

### Formato dos Dados

Os dados são coletados da API da B3 e incluem:

- **Header**: Informações sobre a data de referência e paginação
- **Results**: Lista de ativos do Ibovespa com informações como:
  - Código do ativo
  - Nome da empresa
  - Tipo de ativo
  - Participação no índice

### Estrutura de Arquivos

```
data/
├── bronze/
│   └── 2025-07-08/
│       └── dados_originais.parquet  # Header + Results juntos
└── raw/
    ├── 2025-06-30.json
    ├── 2025-07-01.json
    ├── 2025-07-02.json
    └── ... (arquivos JSON por data)
```

## 🔧 Desenvolvimento

### Adicionando Novas Funcionalidades

1. Crie uma nova branch para sua feature
2. Implemente a funcionalidade seguindo os padrões do projeto
3. Adicione testes unitários
4. Atualize a documentação
5. Faça o merge após revisão

### Executando Testes

```bash
# Teste da API de datas
python test_api_dates.py
```

## 📝 Configurações

### Arquivo `config/config.yaml`

```yaml
aws:
  region: us-east-1
  bucket_name: b3-techchallenge-fase2-andrea
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📞 Suporte

Para suporte e dúvidas:

- Abra uma issue no GitHub
- Consulte o arquivo `fluxo de desenvolvimento.txt` para orientações
- Verifique a documentação da API B3

## 📚 Documentação Adicional

- [Fluxo de Desenvolvimento](fluxo de desenvolvimento.txt)
- [Arquitetura AWS](arquitetura_aws.txt)
- [Estrutura do Projeto](estrutura do projeto.txt)
- [Documentação da API B3](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/)

## 🔄 Status do Projeto

### ✅ Concluído
- Configuração do ambiente local
- Desenvolvimento dos módulos de coleta
- Implementação dos modelos de dados
- Sistema de armazenamento local
- Script principal funcional

### 🚧 Em Desenvolvimento
- Configuração AWS
- Implementação do pipeline ETL
- Automação com Lambda

### 📋 Próximos Passos
- Deploy na AWS
- Configuração do Glue Job
- Implementação da automação
- Configuração do BI

---

**Nota**: Este projeto está em desenvolvimento ativo seguindo o fluxo documentado. Para acompanhar o progresso, consulte o arquivo `fluxo de desenvolvimento.txt`.

## 📄 Licença
MIT License.