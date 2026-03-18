# ⚔️ Inteligência de Dados - TCG Flesh and Blood

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Ativo-brightgreen)

## 📜 Sobre o Projeto

Este projeto de **Inteligência de Dados e Web Scraping** foca no card game **Flesh and Blood (TCG)**. O objetivo principal é extrair, processar e consolidar informações diretamente do site oficial do jogo, criando um banco de dados estruturado sobre torneios, *decklists* (listas de cartas) e heróis.

O resultado é um *dataset* limpo (disponível em formatos `.csv` e `.parquet`), construído para viabilizar análises estatísticas avançadas, estudos de performance de classes/talentos e visualização do *metagame* atual. O pipeline de dados foi desenhado para ser automatizado, atualizando as informações de forma eficiente através do processamento paralelo.

> 📌 **Fonte dos dados:** [fabtcg.com](https://fabtcg.com) — site oficial do jogo Flesh and Blood.

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia |
|---|---|
| Linguagem | Python 3.10+ |
| Manipulação de Dados | `pandas` |
| Web Scraping | `BeautifulSoup` (bs4), `requests` |
| Processamento Paralelo | `concurrent.futures` |
| Orquestração | `papermill` |
| Visualização | Google Looker Studio |
| Ambiente | Jupyter Notebook |

---

## 📂 Estrutura do Projeto

```
├── utils.py               # Funções compartilhadas: requisições, paginação e scraping
├── merge_dfs.py           # Orquestra os notebooks e consolida o dataset final
├── Fab_decklists.ipynb    # Extração e transformação das decklists
├── Fab_herois.ipynb       # Extração e transformação dos heróis
├── Fab_LL.ipynb           # Extração do sistema Living Legend
├── dataset.csv            # Dataset consolidado (formato CSV)
├── dataset.parquet        # Dataset consolidado (formato Parquet)
├── decks_fabtcg.csv       # Dados intermediários de decks
├── herois_fabtcg.csv      # Dados intermediários de heróis
└── requirements.txt       # Dependências do projeto
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10 ou superior
- pip

### Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/GuilhermeHenrick/Intelig-ncia-de-Dados-TCG-Flash-and-Blood-.git
cd Intelig-ncia-de-Dados-TCG-Flash-and-Blood-

# 2. (Recomendado) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Instale as dependências
pip install -r requirements.txt
```

### Execução do Pipeline

```bash
# Roda o pipeline completo: extrai, transforma e consolida os dados
python merge_dfs.py
```

O script irá executar automaticamente os notebooks `Fab_decklists.ipynb` e `Fab_herois.ipynb` e gerar os arquivos `dataset.csv` e `dataset.parquet` na raiz do projeto.

---

## ⚠️ Uso Ético do Web Scraping

Este projeto realiza scraping de dados públicos do site oficial do Flesh and Blood para fins exclusivamente educacionais e analíticos. O pipeline foi desenvolvido com respeito às boas práticas:

- Requisições com intervalo de tempo entre chamadas para não sobrecarregar o servidor.
- Nenhum dado privado ou protegido é coletado.
- Os dados são utilizados apenas para análise do cenário competitivo público.

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
