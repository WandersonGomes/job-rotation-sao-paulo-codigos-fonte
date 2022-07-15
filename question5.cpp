/*
Author: Wanderson Gomes da Costa
E-mail: dersom100@gmail.com

Problema:
    5) Escreva um programa que inverta os caracteres de uma string.

    IMPORTANTE:
    a) Essa string pode ser informada atraves de qualquer entrada de sua preferencia ou pode ser definida no codigo;
    b) Evite usar funcoes prontas, como, por exemplo, reverse;

Executar:
    Para executar o programa em um terminal do linux use os seguintes comandos:
    
    g++ question5.cpp
    ./a.out
*/
#include <iostream>

using namespace std;

string inverterTexto(string texto) {
    int tamanho = texto.size();
    string resultado = "";

    for (int i = tamanho-1; i > -1; i--)
        resultado += texto[i];
    
    return resultado;
}

int main() {
    string texto;
    string textoInvertido;

    cout << "Informe um texto para ser invertido: ";
    getline(cin, texto);

    textoInvertido = inverterTexto(texto);
    cout << "Texto invertido: " << textoInvertido << endl;

    return 0;
}