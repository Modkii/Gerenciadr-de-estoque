def verificar_status(quantidade, minimo, ideal):
    if quantidade < minimo:
        return "🔴 FALTA"
    elif quantidade > ideal:
        return "🟢 EXCESSO"
    else:
        return "🟡 OK"


def escolher_categoria(estoque):
    """Exibe categorias existentes e permite escolha por número."""
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
