
"""Funções utilitárias para o sistema de gestão de estoque.

Contém funções auxiliares utilizadas em vários módulos da aplicação.
"""

def verificar_status(quantidade, minimo, ideal):
    """Determina o status de um item com base nos níveis de estoque.
    
    Args:
        quantidade (int): Quantidade atual em estoque.
        minimo (int): Nível mínimo necessário de estoque.
        ideal (int): Nível ideal de estoque.
        
    Returns:
        str: Indicador de status (🔴 FALTA, 🟢 EXCESSO ou 🟡 OK).
    """
    if quantidade < minimo:
        return "🔴 FALTA"
    elif quantidade > ideal:
        return "🟢 EXCESSO"
    else:
        return "🟡 OK"

def escolher_categoria(estoque):
    """Exibe categorias disponíveis e permite seleção por número.
    
    Args:
        estoque (dict): Dados do estoque contendo as categorias.
        
    Returns:
        str: Nome da categoria selecionada, ou None se seleção inválida.
    """
    if not estoque:
        print("⚠️ Nenhuma categoria encontrada.")
        return None

    print("\n📂 Categorias disponíveis:")
    categorias = list(estoque.keys())
    for idx, cat in enumerate(categorias, start=1):
        print(f"[{idx}] {cat}")

    try:
        escolha = int(input("Escolha o número da categoria: ")) - 1
        if 0 <= escolha < len(categorias):
            return categorias[escolha]
        else:
            print("❌ Escolha inválida.")
            return None
    except ValueError:
        print("❌ Entrada inválida.")
        return None