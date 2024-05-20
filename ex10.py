# ATIVIDADE 10
# |Criar um algoritmo que receba N números e contar quantos deste números são pares. 

print('\nprograma que recebe números e mostra quantos são pares\n')

#utilizando *FOR*

n = int(input('insira quantos números deseja comparar: '))
par = 0

for i in range(1,n+1,1):
    numero = int(input(f'insira o {i} número: '))
    
    if(numero % 2 == 0 ):
        par+=1


        

print(f'existem {par} números pares')

#utilizando *WHILE*

quantidade = int(input('insira quantos números deseja comparar: '))
par2 = 0
j = 1

while j <= quantidade:
    numero2 = int(input(f'insira o {i} número: '))
    
    if(numero2 % 2 == 0 ):
        par2+=1
    
    j+=1



print(f'existem {par2} números pares')
    