#include<stdio.h>

int main (){

	int num = 0;

	printf("Informe o número para calcular a tabuada: \n");
	scanf("%d", &num);

	for (int i=1; i<=10; i++){

		printf("%d x %d = %d\n", num, i, num*i);
	}

	return 0;

}