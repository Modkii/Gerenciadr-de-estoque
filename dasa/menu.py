
"""Módulo contendo a interface do menu principal do sistema de gestão de estoque.

Este módulo fornece uma interface console amigável para operações de gestão de inventário,
incluindo gestão de itens, categorias, movimentações de estoque e relatórios.
"""

import os
import time
from persistencia import carregar_estoque, salvar_estoque
from estoque import gerenciar_item, consultar_estoque, movimentar_item, gerenciar_categoria
from relatorios import itens_em_alerta

def menu():
    """Exibe o menu principal e gerencia as interações do usuário.
    
    Carrega os dados do estoque e apresenta um loop contínuo do menu até que o usuário escolha sair.
    Gerencia todas as operações principais delegando para funções apropriadas de outros módulos.
    """
    estoque = carregar_estoque()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("╔════════════════════════════════════════╗")
        print("║     📦 Gerenciador de Estoque DASA     ║")
        print("╚════════════════════════════════════════╝")
        print("\nEscolha uma opção abaixo:")
        print("[1] 🛠️ Adicionar novo item ou remover item")
        print("[2] 🗂️ Gerenciar Categorias (criar/remover)")
        print("[3] 🔼 Registrar ENTRADA de itens")
        print("[4] 🔽 Registrar SAÍDA de itens")
        print("[5] 📋 Consultar estoque completo")
        print("[6] 🚨 Ver itens EM FALTA")
        print("[7] 🚀 Ver itens EM EXCESSO")
        print("[8] 💾 Salvar e Sair")
        print("------------------------------------------")
        opcao = input("Digite sua opção: ").strip()

        if opcao == "1":
            gerenciar_item(estoque)
        elif opcao == "2":
            gerenciar_categoria(estoque)
        elif opcao == "3":
            movimentar_item(estoque, tipo="entrada")
        elif opcao == "4":
            movimentar_item(estoque, tipo="saida")
        elif opcao == "5":
            consultar_estoque(estoque)
        elif opcao == "6":
            itens_em_alerta(estoque, tipo="falta")
        elif opcao == "7":
            itens_em_alerta(estoque, tipo="excesso")
        elif opcao == "8":
            salvar_estoque(estoque)
            print("\n👋 Saindo... Obrigado por usar o Gerenciador DASA!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")
            time.sleep(1)