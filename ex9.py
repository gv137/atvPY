# ATIVIDADE 9
# |Criar um algoritmo que receba duas notas de 10 alunos_
# _e calcule a média para cada um deles e exiba a média individual dos alunos e a média total.

print('\nprograma que recebe duas notas de 10 alunos e calcula a media\n')


# utilizando *FOR*


for i in range (1,11,1):

    print(f'\nalunos {i}')
    nota1 = float(input('insira a primeira nota: '))
    nota2 = float(input('insira a segunda nota: '))

    media = (nota1 + nota2) / 2

    print(f'\na media do aluno {i} é: ',media) 


# utilizando *WHILE*

j = 1

while j <= 10:
  print(f'\nalunos {j}')
  nota3 = float(input('insira a primeira nota: '))
  nota4 = float(input('insira a segunda nota: '))

  media2 = (nota3 + nota4) / 2

  print(f'\na media do aluno {j} é: ',media2)

  j+=1


