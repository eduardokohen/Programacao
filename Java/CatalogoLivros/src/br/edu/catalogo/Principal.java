package br.edu.catalogo;

public class Principal {

    public static void main(String[] args) {

        Livro[] livros = new Livro[5];

        livros[0] = new Livro("Java: Como Programar", "Paul Deitel", 2017);
        livros[1] = new Livro("Introdução à Programação com Python", "Nilo Ney Coutinho Menezes", 2019);
        livros[2] = new Livro("Java Efetivo", "Joshua Bloch", 2018);
        livros[3] = new Livro("Estruturas de Dados e Algoritmos", "Robert Lafore", 2002);
        livros[4] = new Livro("Java para Iniciantes", "Herbert Schildt", 2019);

        System.out.println("Livros que possuem 'Java' no título:");
        System.out.println();

        for (int i = 0; i < livros.length; i++) {

            if (livros[i].titulo.contains("Java")) {
                livros[i].exibirInformacoes();
            }
        }
    }
}