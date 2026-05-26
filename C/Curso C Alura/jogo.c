#include<stdio.h>

#define J 5

int main (){

	//Imprime o cabeçalho do nosso jogo

	printf("\n*****************************************\n");
    printf("*Bem vindo ao nosso jogo de adivinhação!*\n");
    printf("*****************************************\n" );

    int numero_secreto = 42;

    int chute = 0;

    for(int i = 1; i <= J; i++){

    	printf("Tentativa %d de %d\n", i, J);

	    printf("Qual é o seu chute?\n");
	    scanf("%d",&chute);
	    printf("Seu chute foi %d!\n", chute);

	    if (chute<0){
	    	printf("Você não pode chutar números negativos!\n");
	    	i--;
	    	continue;
	    }

	    int acertou = (chute == numero_secreto);
	   	int maior = chute > numero_secreto;


	    if (acertou){

	    	printf("Parabéns! Você acertou!\n");
	    	printf("Você acertou em %d tentativas!\n", i);
	    	printf("Jogue de novo, você é um bom jogador!\n");	
	    	break;
	    }
	    else if (maior){
	    	printf("Seu chute foi maior que o número secreto\n");
	    	}
	    
	    else{
	    	printf("Seu chute foi menor que o número secreto\n");
	    	}
	    }

	printf("Fim de Jogo!\n");
    return 0;
}