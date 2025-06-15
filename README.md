# 📦 Gerenciador de Estoque DASA

Sistema simples de gerenciamento de estoque em Python, com interface via terminal, que permite controlar categorias, itens, entradas, saídas e emitir relatórios de itens em falta ou em excesso.

Este projeto é ideal para pequenos negócios, farmácias, clínicas ou projetos acadêmicos que precisam de um controle eficiente de estoque.

---

## 🚀 Funcionalidades

- 📁 **Gerenciamento de Categorias**  
  ➕ Criar novas categorias  
  ❌ Remover categorias existentes  

- 🏷️ **Gestão de Itens**  
  ➕ Adicionar novos itens ao estoque  
  ❌ Remover itens existentes  

- 🔄 **Movimentação de Estoque**  
  🔼 Registrar entrada de produtos  
  🔽 Registrar saída de produtos  

- 📊 **Consultas e Relatórios**  
  📋 Consulta completa do estoque com status (Falta, OK, Excesso)  
  🚨 Visualizar itens em **FALTA** (abaixo do mínimo)  
  🚀 Visualizar itens em **EXCESSO** (acima do ideal)  

- 💾 **Persistência dos Dados**  
  Armazena os dados do estoque em um arquivo `estoque.json` para garantir que nada seja perdido entre sessões.

---

## 🗂️ Estrutura do Projeto

```
📦 Gerenciador-de-Estoque
├── main.py               # Arquivo principal (ponto de entrada)
├── menu.py               # Interface do menu principal
├── estoque.py            # Operações principais de estoque
├── persistencia.py       # Salvamento e carregamento dos dados (JSON)
├── relatorios.py         # Geração de relatórios (falta e excesso)
├── utils.py              # Funções auxiliares
├── estoque.json          # Arquivo de dados (criado após primeiro uso)
└── README.md             # Documentação do projeto
```

---

## ▶️ Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/gerenciador-de-estoque.git
cd gerenciador-de-estoque
```

2. **Execute o programa:**

```bash
python main.py
```

> ⚠️ **Observação:** É necessário ter o **Python 3.8** ou superior instalado no seu computador.

---

## 💾 Dados Salvos

Os dados são armazenados automaticamente no arquivo `estoque.json` no mesmo diretório do projeto. Este arquivo guarda as categorias, itens, quantidades, mínimos e ideais definidos.

---

## 🏗️ Tecnologias Utilizadas

- 🐍 Python (puro, sem bibliotecas externas)
- 📁 Armazenamento em JSON
- 💻 Interface via terminal

---

## 🧠 Organização do Código

O projeto foi desenvolvido utilizando uma arquitetura modular, separando as responsabilidades em diferentes arquivos:

- `menu.py`: Interface e navegação do sistema.  
- `estoque.py`: Manipulação de itens e categorias, além das movimentações.  
- `relatorios.py`: Funções para visualizar itens em falta e em excesso.  
- `persistencia.py`: Leitura e escrita dos dados no arquivo JSON.  
- `utils.py`: Funções auxiliares, como escolha de categorias e verificação de status dos itens.  
- `main.py`: Arquivo principal que executa o menu do sistema.

---


