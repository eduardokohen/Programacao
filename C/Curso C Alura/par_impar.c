//Crie um programa que recebe 1 número e verifica se ele é par ou ímpar:

#include<stdio.h>

int main (){

	int num = 0;

	printf("Digite um número para verificar se é par ou ímpar:\n");
	scanf("%d", &num);

	if (num%2 == 0){

		printf("O número digitado, %d, é par!\n", num);

	}else{

		printf("O número digitado, %d, é ímpar!\n", num);
	}

	return 0;
}