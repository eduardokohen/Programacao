//Faça um programa que receba um número do usuário e retorne se o número é positivo, negativo ou 0

#include<stdio.h>

int main(){

	int num = 0;

	printf("Digite um número: \n");
	scanf("%d", &num);

	if (num > 0){
		printf("O número %d é positivo!\n", num);
	}
	else if (num < 0){
		printf("O número %d é negativo!\n", num);
	}else{
		printf("O número %d é zero!\n", num);
	}
	return 0;

}