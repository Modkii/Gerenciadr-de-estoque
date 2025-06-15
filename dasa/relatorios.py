
"""Módulo para geração de relatórios de estoque.

Fornece funções para gerar diversos relatórios de status do inventário,
incluindo itens em falta e com excesso de estoque.
"""

from utils import verificar_status

def itens_em_alerta(estoque, tipo="falta"):
    """Exibe itens que estão em falta ou em excesso no estoque.
    
    Args:
        estoque (dict): Dados do estoque para análise.
        tipo (str): Tipo de alerta a exibir ('falta' para itens em falta ou 'excesso' para itens com excesso).
    """
    print(f"\n{'🚨' if tipo == 'falta' else '🚀'} Itens {'EM FALTA' if tipo == 'falta' else 'EM EXCESSO'}")
    encontrou = False
    for categoria, itens in estoque.items():
        for nome, dados in itens.items():
            if tipo == "falta" and dados["quantidade"] < dados["minimo"]:
                print(f"{categoria} - {nome}: 🔴 FALTA ({dados['quantidade']})")
                encontrou = True
            elif tipo == "excesso" and dados["quantidade"] > dados["ideal"]:
                print(f"{categoria} - {nome}: 🟢 EXCESSO ({dados['quantidade']})")
                encontrou = True
    if not encontrou:
        print("✅ Nenhum item encontrado nessa condição.")

    input("\n▶️ Pressione ENTER para voltar ao menu...")