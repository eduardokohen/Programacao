//Faça um programa que receba do usuário um número inteiro e calcule sua progressão aritmética:

#include<stdio.h>

int main(){

	int contador = 1;
	int soma = 0;
	int num = 0;

	printf("Digite o número que você quer fazer a progressão aritmética: \n");
	scanf("%d", &num);

	while(contador <= num){
		
		soma = soma + contador;
		
		contador ++;
	}
	printf("A soma é 1 até %d é %d\n", num, soma);

	return 0;

}