# ⚔️ Inteligência de Dados - TCG Flesh and Blood

## 📜 Sobre o Projeto
Este projeto de Inteligência de Dados e Web Scraping foca no card game **Flesh and Blood (TCG)**. O objetivo principal é extrair, processar e consolidar informações diretamente do site oficial do jogo, criando um banco de dados estruturado sobre torneios, *decklists* (listas de cartas) e heróis.

O resultado é um *dataset* limpo (disponível em formatos `.csv` e `.parquet`), construído para viabilizar análises estatísticas avançadas, estudos de performance de classes/talentos e visualização do *metagame* atual. O pipeline de dados foi desenhado para ser automatizado, atualizando as informações de forma eficiente através do processamento paralelo.

## 📊 Dashboard Interativo
Os dados processados por este pipeline alimentam um painel de visualização de dados construído no **Google Looker Studio**. Através dele, é possível explorar de forma visual e interativa o cenário competitivo do jogo, filtrando heróis, torneios e tendências de vitórias.

🔗 **[Acesse o Dashboard Interativo Clicando Aqui](https://lookerstudio.google.com/reporting/8307ae14-615f-4199-9449-857cd4650f39)**

## 🛠️ Tecnologias Utilizadas
O projeto foi desenvolvido utilizando a linguagem **Python 3** e as seguintes bibliotecas e ferramentas:

* **Manipulação e Análise de Dados:** `pandas`
* **Web Scraping:** `BeautifulSoup` (bs4) e `requests`
* **Processamento Paralelo:** `concurrent.futures` (para otimização e velocidade na extração)
* **Orquestração e Automação:** `papermill` (para execução programática de notebooks)
* **Visualização de Dados:** Google Looker Studio
* **Ambiente de Desenvolvimento:** Jupyter Notebook

## 📂 Estrutura do Projeto
A organização dos arquivos reflete as etapas do pipeline de dados:

* **`utils.py`**: Módulo central contendo as funções de requisição web, paginação e raspagem de dados em HTML.
* **`Fab_decklists.ipynb` / `Fab_herois.ipynb` / `Fab_LL.ipynb`**: Notebooks responsáveis pelas etapas de extração e transformação de entidades específicas do jogo (Decks, Heróis e sistema de *Living Legend*).
* **`teste.py`**: Script de automação que orquestra a execução dos notebooks e consolida os dados finais utilizando caminhos relativos.
* **Datasets**: Arquivos consolidados (`dataset.csv` e `dataset.parquet`) prontos para consumo e análise.