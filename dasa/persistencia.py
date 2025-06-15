
"""Módulo para operações de persistência de dados.

Fornece funções para carregar e salvar dados de estoque em arquivos JSON,
garantindo a persistência dos dados entre execuções do programa.
"""

import json
import time

def carregar_estoque(arquivo="estoque.json"):
    """Carrega dados do estoque a partir de um arquivo JSON.
    
    Args:
        arquivo (str): Caminho para o arquivo JSON. Padrão: "estoque.json".
        
    Returns:
        dict: Dados do estoque carregados. Retorna um dicionário vazio se o arquivo não existir.
    """
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("\n⚠️ Arquivo 'estoque.json' não encontrado. Criando um novo...\n")
        time.sleep(1)
        return {}

def salvar_estoque(estoque, arquivo="estoque.json"):
    """Salva os dados do estoque em um arquivo JSON.
    
    Args:
        estoque (dict): Dados do estoque a serem salvos.
        arquivo (str): Caminho para o arquivo JSON. Padrão: "estoque.json".
    """
    with open(arquivo, "w") as f:
        json.dump(estoque, f, indent=4)
    print("\n✅ Dados salvos no arquivo 'estoque.json'!\n")
    time.sleep(1)