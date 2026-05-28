//Faça um programa que leia um número qualquer do usuário e, usando a fórmula de Gauss, calcule a PA:

#include<stdio.h>

int main(){

	int soma = 0;
	int num = 0;

	printf("Informe o número para fazer a progressão aritmética: \n");
	scanf("%d", &num);

	soma = num*(num+1)/2;

	printf("A progressão aritmética de %d é %d.\n", num, soma);
	return 0;
}