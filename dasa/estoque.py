import time
from utils import verificar_status, escolher_categoria

def gerenciar_item(estoque):
    print("\n🛠️ Gerenciar Itens")
    print("[1] ➕ Adicionar novo item")
    print("[2] ❌ Remover item")
    acao = input("Escolha a ação: ").strip()

    if acao == "1":
        categoria = escolher_categoria(estoque)
        if not categoria:
            return

        nome = input("🔸 Nome do novo item: ").strip().title()
        if nome in estoque.get(categoria, {}):
            print("❌ Item já existe nessa categoria.")
            return

        try:
            quantidade = int(input("🔢 Quantidade inicial: "))
            minimo = int(input("⚠️ Estoque mínimo: "))
            ideal = int(input("⭐ Estoque ideal: "))
        except ValueError:
            print("❌ Entrada inválida. Digite números válidos.")
            return

        estoque[categoria][nome] = {
            "quantidade": quantidade,
            "minimo": minimo,
            "ideal": ideal
        }
        print(f"✅ Item '{nome}' adicionado à categoria '{categoria}' com {quantidade} unidades.")
        time.sleep(1)

    elif acao == "2":
        categoria = escolher_categoria(estoque)
        if not categoria:
            return

        print(f"\nItens em '{categoria}':")
        itens = list(estoque[categoria].keys())
        for idx, item in enumerate(itens, start=1):
            print(f"[{idx}] {item}")

        try:
            escolha = int(input("Escolha o número do item a remover: ")) - 1
            if 0 <= escolha < len(itens):
                removido = itens[escolha]
                del estoque[categoria][removido]
                print(f"✅ Item '{removido}' removido da categoria '{categoria}'.")
            else:
                print("❌ Escolha inválida.")
        except ValueError:
            print("❌ Entrada inválida.")
        time.sleep(1)
    else:
        print("❌ Ação inválida.")
        time.sleep(1)


def consultar_estoque(estoque):
    print("\n📊 Consulta Completa do Estoque")
    if not estoque:
        print("\n⚠️ Estoque vazio.\n")
        time.sleep(1)
        return

    for categoria, itens in estoque.items():
        print(f"\n📂 Categoria: {categoria}")
        for nome, dados in itens.items():
            status = verificar_status(dados["quantidade"], dados["minimo"], dados["ideal"])
            print(f"  🔸 {nome}: {dados['quantidade']} unidades (Status: {status})")
    input("\n▶️ Pressione ENTER para voltar ao menu...")


def movimentar_item(estoque, tipo):
    print(f"\n{'🔼 Entrada' if tipo == 'entrada' else '🔽 Saída'} de Itens")
    categoria = escolher_categoria(estoque)
    if not categoria:
        return

    nome = input("🔸 Nome do item: ").strip().title()

    try:
        quantidade = int(input("🔢 Quantidade: "))
    except ValueError:
        print("❌ Entrada inválida. Digite um número.")
        return

    if tipo == 'saida':
        quantidade = -quantidade

    try:
        estoque[categoria][nome]["quantidade"] += quantidade
        print(f"\n✅ Movimentação realizada! Agora '{nome}' tem {estoque[categoria][nome]['quantidade']} unidades.\n")
    except KeyError:
        print("\n❌ Item não encontrado. Verifique se digitou corretamente os nomes.\n")
    time.sleep(1)

def gerenciar_categoria(estoque):
    print("\n📁 Gerenciar Categorias")
    print("[1] ➕ Criar nova categoria")
    print("[2] ❌ Remover categoria")
    acao = input("Escolha a ação: ").strip()

    if acao == "1":
        nova = input("Nome da nova categoria: ").strip().title()
        if nova in estoque:
            print("❌ Categoria já existe.")
        else:
            estoque[nova] = {}
            print(f"✅ Categoria '{nova}' criada.")
        time.sleep(1)

    elif acao == "2":
        categoria = escolher_categoria(estoque)
        if not categoria:
            return
        confirm = input(f"Tem certeza que deseja remover a categoria '{categoria}'? (s/n): ").strip().lower()
        if confirm == "s":
            del estoque[categoria]
            print(f"✅ Categoria '{categoria}' removida.")
        else:
            print("❌ Remoção cancelada.")
        time.sleep(1)

    else:
        print("❌ Ação inválida.")
        time.sleep(1)
