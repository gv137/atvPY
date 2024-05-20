# ATIVIDADE 8
# | Criar um algoritmo que calcule a média aritmética de valores numéricos lidos. 

print('\nprograma que calcula a média aritmética de valores lidos\n')

# utilizando *FOR*

i = int(input('insira a quantidade de números que serão calculados: '))
valores = 0

for i in range (1,i+1,1):
    numero = int(input(f'insira o {i}º número: '))
    valores = valores + numero
    


media = valores / i

print('\na média dos números é: ',media) 


# utilizando *WHILE*

quantidade = int(input('\ninsira a quantidade de números que serão calculados: '))

j = 1
valores2 = 0

while j <= quantidade:
   numero2 = int(input(f'insira o {j}º número: '))
   valores2 = valores2 + numero2
   j+=1
    

media2 = valores2 / quantidade

print('\na média dos números é: ',media2)
