import os
from datetime import datetime

# Configurações de rede compartilhadas
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://google.com'
}

def arquivo_e_atual(caminho_arquivo):

    if not os.path.exists(caminho_arquivo):
        return False
    
    data_modificacao = datetime.fromtimestamp(os.path.getmtime(caminho_arquivo)).date()
    data_atual = datetime.now().date()
    
    return data_modificacao == data_atual

def apagar_arquivo(caminho_arquivo):
    if os.path.exists(caminho_arquivo):
        print(f"Apagando o arquivo antigo: {caminho_arquivo}")
        os.remove(caminho_arquivo)
        print("Arquivo apagado com sucesso.")
    else:
        print("O arquivo não existe.")