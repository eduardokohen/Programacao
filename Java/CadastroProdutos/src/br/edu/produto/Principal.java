package br.edu.produto;

public class Principal {

    public static void main(String[] args) {

        Produto produto1 = new Produto();

        Produto produto2 = new Produto("Arroz", 25.90);

        Produto produto3 = new Produto("Feijão", 8.50);

        produto1.exibirDados();
        produto2.exibirDados();
        produto3.exibirDados();

        Produto.exibirQuantidadeTotal();
    }
}