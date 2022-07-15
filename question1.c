/*
Author: Wanderson Gomes da Costa
E-mail: dersom100@gmail.com

Problema:
    Observe o trecho de codigo abaixo:
    
    int INDICE = 13, SOMA = 0, K = 0;

    enquanto K < INDICE faca
    {
    K = K + 1;
    SOMA = SOMA + K;
    }
    
    imprimir(SOMA);

    Ao final do processamento, qual sera o valor da variavel SOMA?

Executar:
    Para executar utilize os seguintes comandos em um terminal linux:
    
    gcc question1.c
    ./a.out
*/

/* 
TESTE DE MESA 
    INDICE = 13, SOMA = 0,  K =  0
    INDICE = 13, SOMA = 1,  K =  1
    INDICE = 13, SOMA = 3,  K =  2
    INDICE = 13, SOMA = 6,  K =  3
    INDICE = 13, SOMA = 10, K =  4
    INDICE = 13, SOMA = 15, K =  5
    INDICE = 13, SOMA = 21, K =  6
    INDICE = 13, SOMA = 28, K =  7
    INDICE = 13, SOMA = 36, K =  8
    INDICE = 13, SOMA = 45, K =  9
    INDICE = 13, SOMA = 55, K = 10
    INDICE = 13, SOMA = 66, K = 11
    INDICE = 13, SOMA = 78, K = 12
    INDICE = 13, SOMA = 91, K = 13
*/

/*
CALCULO POR PA
    k0 = 0
    k13 = 13

    n = 13 + 1 = 14

    Sn = (k0 + k13) * 14/2 = (0 + 13) * 7 = 91
*/

#include <stdio.h>

int main() {
    //dados
    int indice = 13,
        soma = 0,
        k = 0;
    
    //processamento
    while (k < indice) {
        k = k + 1;
        soma = soma + k;
    }

    //saida
    printf("%d\n", soma);

    return 0;
}