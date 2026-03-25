#include<stdio.h>

int main(){
    int num;

    printf("Digite um número entre 0 e 9999: ");
    scanf("%d", &num);

    int u = num / 1 % 10;
    int d = num / 10 % 10;
    int c = num / 100 % 10;
    int m = num / 10000 % 10;
    
    printf("\nUnidade: %d", u);
    printf("\nDezena: %d", d);
    printf("\nCentena: %d", c);
    printf("\nMilhar: %d\n", m);

    return(0);
}