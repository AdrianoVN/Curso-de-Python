# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, 
# COM 5% DE DESCONTO.

print("========== Desafio 012 ==========")

preco = float(input("Digite o preço: "))
percentual = float(input("Digite o percentual de desconto %: "))
preco_com_desconto = (preco * percentual) / 100 
print("O valor do desconto:", preco_com_desconto,"R$")
print("O valor a pagar com desconto: R$:", preco - preco_com_desconto,)
