//Faça um programa que receba um número do usuário e calcule sua tabuada.

#include<stdio.h>

int main(){

	int num = 0;

	printf("Digite um número para calcular a tabuada: \n");
	scanf("%d", &num);

	printf("Tabuada do %d\n", num);


	for (int i = 1; i <= 10; i++){

		int mult = num * i;

		printf("%d x %d = %d\n", num, i, mult);
	}
	return 0;
}