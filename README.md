# Intelig-ncia-de-Dados-TCG-Flash-and-Blood-
Projeto de inteligência de dados em TCG

# 🃏 Flash and Blood (FAB) - Competitive Meta-Game Insights

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.12-green?style=for-the-badge)

## 📌 Sobre o Projeto
Este projeto é uma ferramenta de **Inteligência de Dados** voltada para o cenário competitivo do Trading Card Game (TCG) **Flash and Blood**. O objetivo principal é automatizar a coleta de dados de torneios globais e correlacionar listas de decks com metadados técnicos dos heróis para identificar tendências no "meta-game".

## 🚀 Funcionalidades
- **Web Scraping Avançado:** Extração automatizada de resultados de torneios (Calling, Battle Hardened, Skirmish) diretamente do site oficial `fabtcg.com`.
- **Gestão de Sessões:** Uso de `requests.Session` e headers personalizados para garantir a estabilidade das requisições e evitar bloqueios.
- **Cruzamento de Dados:** Integração de dados de performance com uma base de metadados (Classes e Talentos) via API e arquivos estruturados.
- **Data Cleaning:** Tratamento de strings, normalização de datas e limpeza de dados complexos utilizando **Pandas**.

## 🛠️ Stack Tecnológica
- **Linguagem:** Python
- **Bibliotecas de Extração:** BeautifulSoup4, Requests
- **Análise de Dados:** Pandas
- **Visualização (em progresso):** Seaborn / Matplotlib

## 📂 Estrutura do Repositório
- `/notebooks`: Arquivos `.ipynb` contendo as Provas de Conceito (PoC) e análises exploratórias.
- `/data`: (Opcional) Exemplos de datasets gerados ou metadados de heróis.
- `/src`: (Em breve) Scripts refatorados e modulares.

## 🚧 Status do Projeto: Em Desenvolvimento
O projeto encontra-se atualmente em fase de **validação de lógica (PoC)**. 
**Próximos passos:**
- Refatoração do código para padrões de **Clean Code** e modularização.
- Implementação de um dashboard para visualização das taxas de vitória (win rate) por classe.

---
Desenvolvido por [Guilherme Henrick Lima de Paiva](mailto:guilhermehenrickhlp@gmail.com)
