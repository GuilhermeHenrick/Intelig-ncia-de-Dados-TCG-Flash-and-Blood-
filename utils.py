import os
from datetime import datetime

# Configurações de rede compartilhadas
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://google.com'
}

CLASSES_FAB = ['Guardian', "Warrior", "Runeblade", "Mechanologist", "Ninja", "Adjudicator", "Necromancer", "Bard", "Shapeshifter", "Thief", "Brute", "Assassin", "Wizard", "Illusionist", "Ranger", "Pirate", "Merchant", "Pit-Fighter", "cleric"]
TALENTOS_FAB = ["Elemental" ,"Draconic","Mystic","Light","Shadow","Royal","Reviled","Revered","Chaos"]

EVENT_MAPPING = {
    "tc": "tc",
    "upf": "calling",
    "calling": "calling",
    "battle hardened": "battle hardened",
    "proquest": "pro quest",
    "pro quest": "pro quest",
    "road to nationals": "road to nationals",
    "sunday showdown": "sunday showdown",
    "skirmish": "skirmish",
    "national": "national",
    "silver age spotlight": "silver age spotlight",
    "world championship": "world championships",
    "pro tour": "pro tour",
    "dumpster": "dumpster dive",
    "dev download": "dev download",
    "10k": "Road to $10k",
    "zero to eighty": "zero to eighty",
    "celebrational": "celebrational",
    "store champions": "store champions",
    "smash palace": "smash palace",
    "cat footprints shilin armed cup": "cat footprints shilin armed cup",
    "the savage lands showdown": "the savage lands showdown",
    "commoner": "commoner",
    "hong kong regional championship": "hong kong regional championship",
    "bulk up": "bulk up",
    "primed to fight": "primed to fight",
    "masterclass": "masterclass",
    "world tour": "world tour"
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