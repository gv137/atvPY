# ATIVIDADE 12
# | Criar um algoritmo que receba duas notas de 60 alunos e calcule a média aritmética para cada  aluno. Exiba_ 
#_quantos alunos estão aprovados, quantos estão reprovados e quantos estão de exame, levando em consideração as condições abaixo: 

"""
Aprovado à média maior ou igual a 5; 
Reprovado à média menor do que 3; 
Exame à media entre 3 e 5;
"""

print('\nprograma que recebe duas notas de 60 alunos, calcula media e mostra a situação do aluno\n')

# utilizando *FOR*

aprovados = 0
reprovados = 0
exame = 0

for i in range (1,6,1):

    print(f'\nalunos {i}')
    nota1 = float(input('insira a primeira nota: '))
    nota2 = float(input('insira a segunda nota: '))

    media = (nota1 + nota2) / 2
    print(f'a média do aluno {i} é: ', media)

    if (media >=5 ):
        aprovados+=1
    elif(media >=3 and media <5):
       exame+=1 
    elif(media <3):
        reprovados+=1


print(f'\n{aprovados} alunos estão aprovados')
print(f'{exame} alunos estão de exame')
print(f'{reprovados} alunos estão reprovados')


# utilizando *WHILE*

j = 1
aprovados2 = 0
reprovados2 = 0
exame2 = 0

while j <= 5:

    print(f'\nalunos {j}')
    nota3 = float(input('insira a primeira nota: '))
    nota4 = float(input('insira a segunda nota: '))

    media2 = (nota3 + nota4) / 2
    print(f'a média do aluno {j} é: ', media2)

    if (media2 >=5 ):
        aprovados2+=1
    elif(media2 >=3 and media2 <5):
       exame2+=1 
    elif(media2 <3):
        reprovados2+=1

    j+=1


print(f'{aprovados2} alunos estão aprovados')
print(f'{exame2} alunos estão de exame')
print(f'{reprovados2} alunos estão reprovados')
