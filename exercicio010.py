# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UM PESSOA TEM NA CARTEIRA E MOSTRE
# QUANTOS DOLARES ELA PODE COMPRAR. CONSIDERE US$ 1,00 = R$3,27

print("=============== Desafio 010 ===============")

moeda_real = float(input("Qual a quantia em reais R$:"))
moeda_dolar = float(input("Qual a cotação do dolar atual US$: "))
valor_convertido = (moeda_real / moeda_dolar )
print("Valor convertido em dolar US$:", round(valor_convertido, 2))
print("===========================================")

real = float(input("Digite o valor em reais R$: "))
cotacao_dolar = 3.27
conversao = (real / cotacao_dolar)
print("Valor convertido para cotação de 3.27 US$:", round(conversao,2))


