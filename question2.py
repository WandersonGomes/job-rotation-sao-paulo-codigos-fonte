# Author: Wanderson Gomes da Costa
# E-mail: dersom100@gmail.com

# Problema:
# 2) Dado a sequencia de Fibonacci, onde se inicia por 0 e 1 e o proximo valor sempre sera a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...),
# escreva um programa na linguagem que desejar onde, informado um numero, ele calcule a sequencia de Fibonacci e retorne uma mensagem avisando se o
# numero informado pertence ou nao a sequencia.
#
# IMPORTANTE:
# Esse numero pode ser informado atraves de qualquer entrada de sua preferencia ou pode ser previamente definido no codigo;
#

# Executar:
# Utilize o seguinte comando em um terminal Linux para executar o script.
#
# python3 question2.py

def pertenceSequenciaFibonacciInterativo(numero):
    '''
    Documentacao:
    Funcao que retorna True se o numero passado por 
    parametro pertence a sequencia de Fibonacci e False
    caso contrario.

    Obs: A funcao utiliza um metodo interativo para gerar
    a sequencia e fazer a analise. Complexidade: O(n)

    Exemplo:
    pertenceSequenciaFibonacciInterativo(-1) -> False
    pertenceSequenciaFibonacciInterativo(0)  -> True
    pertenceSequenciaFibonacciInterativo(1)  -> True
    pertenceSequenciaFibonacciInterativo(34) -> True
    pertenceSequenciaFibonacciInterativo(24) -> False
    '''
    # numeros negativos nao pertencem
    if numero < 0:
        return False
    
    # se for igual aos dois iniciais
    if numero == 0 or numero == 1:
        return True
    
    # realiza a verificacao e ao mesmo tempo gera a sequencia
    anterior = 0
    atual = 1
    while True:
        tmp = atual
        atual = atual + anterior
        anterior = tmp

        if numero == atual:
            return True
        elif numero < atual:
            return False

# testes
resultado = pertenceSequenciaFibonacciInterativo(-1) 
assert resultado == False

resultado = pertenceSequenciaFibonacciInterativo(0)
assert resultado == True

resultado = pertenceSequenciaFibonacciInterativo(1)
assert resultado == True

resultado = pertenceSequenciaFibonacciInterativo(34)
assert resultado == True

resultado = pertenceSequenciaFibonacciInterativo(24)
assert resultado == False

# EXECUCAO
if __name__ == "__main__":
    while True:
        try:
            numero = int(input("Informe um numero que deseja saber se pertence a sequencia de Fibonacci: "))
            print("[LOG] => processando...\n")
            if pertenceSequenciaFibonacciInterativo(numero):
                print(f'O numero {numero} pertence!\n')
            else:
                print(f'O numero {numero} nao pertence!\n')

            # pergunta se deseja sair ou fazer um novo teste
            opcao = input("Digite 0 para sair ou qualquer tecla para continuar: ")
            if opcao == '0':
                break
        except:
            print("Error: falha ao informar o numero!! Tente novamente.")  