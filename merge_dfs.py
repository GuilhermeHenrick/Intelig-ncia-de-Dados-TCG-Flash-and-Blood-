import pandas as pd
import papermill as pm
import os

pasta_raiz = os.path.dirname(os.path.abspath(__file__))
notebooks = [
    os.path.join(pasta_raiz, "Fab_decklists.ipynb"),
    os.path.join(pasta_raiz, "Fab_herois.ipynb")]

for arquivo in notebooks:

    nome_arquivo = os.path.basename(arquivo)
    arquivo_saida = os.path.join(pasta_raiz, f"saida_{nome_arquivo}")

    print(nome_arquivo)
    
    pm.execute_notebook(
        arquivo,
        arquivo_saida,
        cwd=pasta_raiz
    )

    if os.path.exists(arquivo_saida):
        print(f"Apagando o arquivo antigo: {arquivo_saida}")
        os.remove(arquivo_saida)
        print("Arquivo apagado com sucesso.")
    else:
        print(f"O arquivo {arquivo_saida} não existe.")

caminho_decklists = os.path.join(pasta_raiz, "decks_fabtcg.parquet")
caminho_herois = os.path.join(pasta_raiz, "herois_fabtcg.parquet")

decklists = pd.read_parquet(caminho_decklists)
herois = pd.read_parquet(caminho_herois)
df = pd.merge(decklists, herois, on='Heroi')

print(df.head())

saida_parquet = os.path.join(pasta_raiz, 'dataset.parquet')
saida_csv = os.path.join(pasta_raiz, 'dataset.csv')
df.to_parquet(saida_parquet)
df.to_csv(saida_csv)