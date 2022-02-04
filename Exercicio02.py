verificaQuantidade = 0
listaPalavras = []

while (verificaQuantidade <3):
        palavra = str(input('Digite uma palavra >> '))
        listaPalavras.append(palavra)
        verificaQuantidade+=1

while((verificaQuantidade) >0):

        armazenaPalavra = (listaPalavras[verificaQuantidade - 1]).split('os')
        if(armazenaPalavra[0] == 'cas'):
                print((listaPalavras[0]) + ' - verb casen, '+'present tense, '+'2nd person')

        verificaQuantidade -= 1