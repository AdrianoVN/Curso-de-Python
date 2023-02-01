# CRIE UM ALGORITMO QUE LEIA UM NUMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA.
print("========== Desafio 006 ==========")

numero = int(input("Digite um numero:"))
dobro = (numero * 2)
triplo = (numero * 3)
raiz = (numero ** (1/2))

print("O dobro de {} é igual: {}".format(numero, dobro))
print("O triplo de {} é igual: {}".format(numero, triplo))
print("A raiz quadrada de {} é igual: {}".format(numero, round(raiz, 2)))
