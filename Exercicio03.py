import time
verifica = 1
while (verifica != 0):

    valor = int(input('\nDigite um valor inteiro diferente de 0 >> '))

    inicio = time.time()

    verifica = valor
    if(valor>-32767 and valor<32767):

        print('Constant {}'.format(valor))

        if(valor == 0):
            print('Fim do programa.')
            break

        if (valor>0):
            print('PLUSONE')

        else:
            print('MINUSONE')

    else:
        print('Valor invalido')

    final = time.time()
    print('Tempo de execução {}'.format(final))

verifica = valor