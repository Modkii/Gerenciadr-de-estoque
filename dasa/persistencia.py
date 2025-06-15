import json
import time

def carregar_estoque(arquivo="estoque.json"):
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("\n⚠️ Arquivo 'estoque.json' não encontrado. Criando um novo...\n")
        time.sleep(1)
        return {}

def salvar_estoque(estoque, arquivo="estoque.json"):
    with open(arquivo, "w") as f:
        json.dump(estoque, f, indent=4)
    print("\n✅ Dados salvos no arquivo 'estoque.json'!\n")
    time.sleep(1)
