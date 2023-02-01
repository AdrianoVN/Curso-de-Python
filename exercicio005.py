# FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE NA TELA 
# O SEU SUCESSOR E SEU ANTECESSOR.
print("========== Desafio 005 ==========")

numero = int(input('Digite um numero:'))
antecessor = (numero - 1)
sucessor = (numero + 1)
print ("O numero digitado é {} e tem como antecessor {} e seu sucessor {}".format(numero, antecessor, sucessor))
n = int(input("Digite um numero"))
print("analisando o valor {}, seu antecessor é {} e seu sucessor é {}".format(n, (n-1), (n+1)))