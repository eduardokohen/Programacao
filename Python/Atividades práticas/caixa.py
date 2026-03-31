# ============================================
# SISTEMA DE CONTROLE DE VENDAS - EVENTOS
# ============================================
# Autor: (coloque seu nome aqui)
# Descrição:
# Sistema para controle de produtos, vendas,
# cálculo de troco e consolidação de caixa.
# ============================================

import sqlite3

# ============================================
# CONEXÃO COM O BANCO DE DADOS
# ============================================

# Cria (ou conecta) ao banco de dados local
conn = sqlite3.connect("sistema_festa.db")
cursor = conn.cursor()

# ============================================
# CRIAÇÃO DAS TABELAS (SE NÃO EXISTIREM)
# ============================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER,
    quantidade INTEGER,
    valor_total REAL,
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
)
""")

conn.commit()

# ============================================
# FUNÇÃO: CADASTRAR PRODUTO
# ============================================

def cadastrar_produto():
    print("\n=== CADASTRAR PRODUTO ===")
    nome = input("Nome do produto: ")
    
    try:
        preco = float(input("Preço: R$ "))
    except ValueError:
        print("Preço inválido.")
        return

    cursor.execute(
        "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
        (nome, preco)
    )

    conn.commit()
    print("Produto cadastrado com sucesso!")

# ============================================
# FUNÇÃO: LISTAR PRODUTOS (TABELA)
# ============================================

def listar_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if not produtos:
        print("\nNenhum produto cadastrado.")
        return

    print("\n===============================")
    print("      LISTA DE PRODUTOS")
    print("===============================")
    print(f"{'ID':<5}{'Nome':<15}{'Preço':<10}")
    print("-"*30)

    for p in produtos:
        print(f"{p[0]:<5}{p[1]:<15}R$ {p[2]:.2f}")

    print("="*30)

# ============================================
# FUNÇÃO: BUSCAR PRODUTO POR NOME
# ============================================

def buscar_produto():
    termo = input("\nDigite o nome do produto: ")

    cursor.execute(
        "SELECT * FROM produtos WHERE LOWER(nome) LIKE LOWER(?)",
        ('%' + termo + '%',)
    )

    resultados = cursor.fetchall()

    if resultados:
        print("\nResultados encontrados:")
        print("="*30)
        print(f"{'ID':<5}{'Nome':<15}{'Preço':<10}")
        print("-"*30)

        for p in resultados:
            print(f"{p[0]:<5}{p[1]:<15}R$ {p[2]:.2f}")

        print("="*30)
    else:
        print("Nenhum produto encontrado.")

# ============================================
# FUNÇÃO: REGISTRAR VENDA + TROCO
# ============================================

def registrar_venda():
    listar_produtos()

    try:
        produto_id = int(input("Digite o ID do produto: "))
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Entrada inválida.")
        return

    cursor.execute(
        "SELECT nome, preco FROM produtos WHERE id = ?",
        (produto_id,)
    )

    produto = cursor.fetchone()

    if not produto:
        print("Produto não encontrado.")
        return

    nome, preco = produto
    total = preco * quantidade

    print(f"\nProduto: {nome}")
    print(f"Total da compra: R$ {total:.2f}")

    try:
        valor_pago = float(input("Valor pago pelo cliente: R$ "))
    except ValueError:
        print("Valor inválido.")
        return

    if valor_pago < total:
        print("Valor insuficiente!")
        return

    troco = valor_pago - total

    print(f"Troco: R$ {troco:.2f}")

    # Salva a venda no banco
    cursor.execute(
        "INSERT INTO vendas (produto_id, quantidade, valor_total) VALUES (?, ?, ?)",
        (produto_id, quantidade, total)
    )

    conn.commit()
    print("Venda registrada com sucesso!")

# ============================================
# FUNÇÃO: RELATÓRIO DE VENDAS
# ============================================

def relatorio_vendas():
    print("\n=== RELATÓRIO DE VENDAS ===")

    cursor.execute("""
    SELECT p.nome, SUM(v.quantidade), SUM(v.valor_total)
    FROM vendas v
    JOIN produtos p ON v.produto_id = p.id
    GROUP BY p.nome
    """)

    dados = cursor.fetchall()

    total_geral = 0

    if not dados:
        print("Nenhuma venda registrada.")
        return

    for nome, qtd, total in dados:
        print(f"{nome}: {qtd} unidades - R$ {total:.2f}")
        total_geral += total

    print("---------------------------")
    print(f"TOTAL: R$ {total_geral:.2f}")

# ============================================
# FUNÇÃO: TOTAL DESTE COMPUTADOR
# ============================================

def total_computador():
    cursor.execute("SELECT SUM(valor_total) FROM vendas")
    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print(f"\nTotal deste computador: R$ {total:.2f}")
    return total

# ============================================
# FUNÇÃO: CONSOLIDAR VÁRIOS CAIXAS
# ============================================

def consolidar_totais():
    print("\n=== CONSOLIDAÇÃO DE CAIXAS ===")

    try:
        qtd = int(input("Quantos caixas deseja somar? "))
    except ValueError:
        print("Entrada inválida.")
        return

    total_geral = 0

    for i in range(qtd):
        try:
            valor = float(input(f"Total do caixa {i+1}: "))
            total_geral += valor
        except ValueError:
            print("Valor inválido.")
            return

    try:
        gastos = float(input("Informe o total de gastos: R$ "))
    except ValueError:
        print("Valor inválido.")
        return

    lucro = total_geral - gastos

    print("\n===========================")
    print(f"TOTAL GERAL: R$ {total_geral:.2f}")
    print(f"GASTOS: R$ {gastos:.2f}")
    print(f"LUCRO: R$ {lucro:.2f}")
    print("===========================")

# ============================================
# MENU PRINCIPAL
# ============================================

def menu():
    while True:
        print("\n===== SISTEMA DE VENDAS =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Registrar venda (com troco)")
        print("5 - Relatório de vendas")
        print("6 - Total deste computador")
        print("7 - Consolidar caixas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            buscar_produto()
        elif opcao == "4":
            registrar_venda()
        elif opcao == "5":
            relatorio_vendas()
        elif opcao == "6":
            total_computador()
        elif opcao == "7":
            consolidar_totais()
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida.")

# ============================================
# INÍCIO DO PROGRAMA
# ============================================

menu()

# Fecha conexão ao sair
conn.close()