#!/usr/bin/env python3
# ============================================
# SISTEMA DE VENDAS - LINUX
# ============================================

import sqlite3
import os
import sys

# ============================================
# FUNÇÃO PARA LIMPAR TELA (Linux/Mac)
# ============================================

def limpar_tela():
    os.system("clear")

# ============================================
# CAMINHO DO BANCO
# ============================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "sistema_festa.db")

# ============================================
# CONEXÃO COM BANCO
# ============================================

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ============================================
# CRIAÇÃO DAS TABELAS
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
    valor_total REAL
)
""")

conn.commit()

# ============================================
# FUNÇÕES
# ============================================

def cadastrar_produto():
    print("\n=== CADASTRAR PRODUTO ===")
    nome = input("Nome: ")

    try:
        preco = float(input("Preço: R$ "))
    except ValueError:
        print("Valor inválido.")
        return

    cursor.execute(
        "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
        (nome, preco)
    )

    conn.commit()
    print("Produto cadastrado!")

def listar_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if not produtos:
        print("\nNenhum produto.")
        return

    print("\n===============================")
    print("      LISTA DE PRODUTOS")
    print("===============================")
    print(f"{'ID':<5}{'Nome':<15}{'Preço':<10}")
    print("-"*30)

    for p in produtos:
        print(f"{p[0]:<5}{p[1]:<15}R$ {p[2]:.2f}")

    print("="*30)

def buscar_produto():
    termo = input("\nBuscar produto: ")

    cursor.execute(
        "SELECT * FROM produtos WHERE LOWER(nome) LIKE LOWER(?)",
        ('%' + termo + '%',)
    )

    resultados = cursor.fetchall()

    if resultados:
        print("\nResultados:")
        for p in resultados:
            print(f"{p[0]} - {p[1]} (R$ {p[2]:.2f})")
    else:
        print("Nada encontrado.")

# ============================================
# MODO CONTÍNUO DE VENDAS
# ============================================

def registrar_venda():
    print("\n=== MODO VENDAS ===")
    print("Digite 0 para sair.\n")

    while True:
        listar_produtos()

        entrada = input("\nID do produto (0 para sair): ")

        if entrada == "0":
            break

        try:
            produto_id = int(entrada)
            quantidade = int(input("Quantidade: "))
        except ValueError:
            print("Entrada inválida.")
            continue

        cursor.execute(
            "SELECT nome, preco FROM produtos WHERE id = ?",
            (produto_id,)
        )

        produto = cursor.fetchone()

        if not produto:
            print("Produto não encontrado.")
            continue

        nome, preco = produto
        total = preco * quantidade

        print(f"\nProduto: {nome}")
        print(f"Total: R$ {total:.2f}")

        try:
            valor_pago = float(input("Valor pago: R$ "))
        except ValueError:
            print("Valor inválido.")
            continue

        if valor_pago < total:
            print("Valor insuficiente.")
            continue

        troco = valor_pago - total
        print(f"Troco: R$ {troco:.2f}")

        confirmar = input("Confirmar venda? (s/n): ").lower()

        if confirmar != "s":
            print("Cancelado.")
            continue

        cursor.execute(
            "INSERT INTO vendas (produto_id, quantidade, valor_total) VALUES (?, ?, ?)",
            (produto_id, quantidade, total)
        )

        conn.commit()
        print("Venda registrada!")

# ============================================
# RELATÓRIO
# ============================================

def relatorio():
    print("\n=== RELATÓRIO ===")

    cursor.execute("""
    SELECT p.nome, SUM(v.quantidade), SUM(v.valor_total)
    FROM vendas v
    JOIN produtos p ON v.produto_id = p.id
    GROUP BY p.nome
    """)

    dados = cursor.fetchall()

    total = 0

    for nome, qtd, valor in dados:
        print(f"{nome}: {qtd} un - R$ {valor:.2f}")
        total += valor

    print(f"\nTOTAL: R$ {total:.2f}")

# ============================================
# CONSOLIDAÇÃO
# ============================================

def consolidar():
    try:
        qtd = int(input("Quantos caixas? "))
    except ValueError:
        print("Erro.")
        return

    total = 0

    for i in range(qtd):
        try:
            valor = float(input(f"Caixa {i+1}: "))
            total += valor
        except ValueError:
            print("Erro.")
            return

    gastos = float(input("Gastos: R$ "))
    lucro = total - gastos

    print(f"\nTOTAL: R$ {total:.2f}")
    print(f"GASTOS: R$ {gastos:.2f}")
    print(f"LUCRO: R$ {lucro:.2f}")

# ============================================
# MENU
# ============================================

def menu():
    while True:
        print("\n===== SISTEMA =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Modo vendas")
        print("5 - Relatório")
        print("6 - Consolidar")
        print("0 - Sair")

        op = input("Opção: ")

        if op == "1":
            cadastrar_produto()
        elif op == "2":
            listar_produtos()
        elif op == "3":
            buscar_produto()
        elif op == "4":
            registrar_venda()
        elif op == "5":
            relatorio()
        elif op == "6":
            consolidar()
        elif op == "0":
            break
        else:
            print("Opção inválida.")

# ============================================
# EXECUÇÃO
# ============================================

if __name__ == "__main__":
    limpar_tela()
    menu()
    conn.close()