#include<stdio.h>

int main(){

	int a = 0;
	int b = 0;

	printf("Digite o numerador da divisão: \n");
	scanf("%d", &a);

	printf("Digite o denominador da divisão: \n");
	scanf("%d", &b);

	double div = a/(double)b;

	printf("O valor da divisão de %d por %d é %f.\n", a, b, div);
	return 0;
}