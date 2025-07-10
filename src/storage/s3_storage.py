# src/storage/s3_storage.py

#Faz a ingestão dos aqruivos .parquet no S3
import boto3
from botocore.exceptions import ClientError
from src.utils.config import CONFIG

# Lê da config
BUCKET_NAME = CONFIG["aws"]["bucket_name"]

# Inicializa a sessão boto3 com o perfil padrão do AWS CLI
session = boto3.Session()
s3_client = session.client("s3")

def upload_to_s3(local_file_path: str) -> None:
    """
    Envia um arquivo local para o bucket S3, mantendo a mesma estrutura relativa a partir de 'data/bronze'.

    Exemplo:
        local_file_path = data/bronze/2025-07-02/dados_originais.parquet
        s3_key = bronze/2025-07-02/dados_originais.parquet
    """
    try:
        # Extrai o caminho relativo a partir de "data/" e força barra "/"
        if local_file_path.startswith("data/") or local_file_path.startswith("data\\"):
            s3_key = local_file_path.replace("data\\", "").replace("data/", "")
            s3_key = s3_key.replace("\\", "/")  # <- aqui garantimos as barras corretas
        else:
            raise ValueError("O caminho local deve começar com 'data/'.")

        s3_client.upload_file(local_file_path, BUCKET_NAME, s3_key)
        print(f"✅ Upload realizado para s3://{BUCKET_NAME}/{s3_key}")
    except ClientError as e:
        print(f"❌ Erro ao enviar para S3: {e}")
        raise