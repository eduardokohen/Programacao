#include<stdio.h>

int main (){

	int x;
	int y;

	printf("Informe a primeira variável, x: \n");
	scanf("%d", &x);

	printf("Informe a segunda variável, y: \n");
	scanf("%d", &y);

	int mult = x * y;

	printf("O valor de %d multiplicado por %d é de %d\n", x, y, mult);

	return 0;
}