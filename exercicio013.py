# FAÇA UM ALGORITMO QUE LEIA O SALARIO DE UM FUNCIONARIO E MOSTRE SEU NOVO SALARIO, 
# COM 15% DE AUMENTO.

print("========== Desafio 013 ==========")

salario = int(input("Digite o seu salário: "))
percentual_de_reajuste = int(input("Digite o percentual de reajuste %: "))

valor_reajuste = (salario/100)*percentual_de_reajuste
print("Valor do acrescimo salarial é de:", valor_reajuste, "reais")
salario_atual = (salario + valor_reajuste)
print("O salário de {:.2f} reais foi reajustado em {}% e passará a ser de: {:.2f} reais".format(salario, percentual_de_reajuste, salario_atual))
