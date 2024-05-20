# ATIVIDADE 11
# |Criar um algoritmo que imprima na tela os números de 1 a 100 exceto os números múltiplos de 3.

print('\nprograma que imprime na tela números de 1 a 100 exceto múltiplos de 3\n')


# utilizando *FOR*

numero = 0

for numero in range(1,101,1):
    if(numero % 3 != 0):
        print('número: ',numero)

    
# utilizando *WHILE*

i = 0

while i <= 100:
    if (i % 3 != 0):
        print('número:', i)

    i+=1


