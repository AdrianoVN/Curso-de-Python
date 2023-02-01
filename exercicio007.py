# DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE SUA MÉDIA.
print("========== Desafio 007 ==========")

nota1 = float(input("Digite a nota 1 "))
nota2 = float(input("Digite a nota 2 "))
media = (nota1 + nota2) / 2
print("A média é igual:", media)
print ("A média de {:.1f} + {:.1f} é igual a: {:.1f}".format(nota1, nota2, media))

# :.1f serve para fazer o arredondamento para cima exemplo 3.75 ficaria 3.8