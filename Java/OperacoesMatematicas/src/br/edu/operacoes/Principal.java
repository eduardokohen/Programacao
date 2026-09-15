package br.edu.operacoes;

public class Principal {

    public static void main(String[] args) {

        Soma soma = new Soma();
        Divisao divisao = new Divisao();

        try {

            double resultadoSoma = soma.calcular(10, 5);
            System.out.println("Resultado da soma: " + resultadoSoma);

            double resultadoDivisao = divisao.calcular(10, 2);
            System.out.println("Resultado da divisão: " + resultadoDivisao);

            double divisaoPorZero = divisao.calcular(10, 0);
            System.out.println("Resultado: " + divisaoPorZero);

        } catch (DivisaoPorZeroException e) {

            System.out.println("Erro: " + e.getMessage());
        }
    }
}