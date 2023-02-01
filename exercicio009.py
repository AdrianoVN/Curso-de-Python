# FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA DE MULTIPLICAÇÃO.

print("========== Tabuada de Multiplicação ==========")

tabuada = int(input("Digite um numero da tabuada: "))
valor1 = tabuada*1 
valor2 = tabuada*2 
valor3 = tabuada*3 
valor4 = tabuada*4 
valor5 = tabuada*5 
valor6 = tabuada*6 
valor7 = tabuada*7
valor8 = tabuada*8 
valor9 = tabuada*9 
valor10 = tabuada*10 
print("{} x {} = {}".format(tabuada, 1, tabuada*1))
print("{} x {} = {}".format(tabuada, 2, tabuada*2))
print("{} x {} = {}".format(tabuada, 3, tabuada*3))
print("{} x {} = {}".format(tabuada, 4, tabuada*4))
print("{} x {} = {}".format(tabuada, 5, tabuada*5))
print("{} x {} = {}".format(tabuada, 6, tabuada*6))
print("{} x {} = {}".format(tabuada, 7, tabuada*7))
print("{} x {} = {}".format(tabuada, 8, tabuada*8))
print("{} x {} = {}".format(tabuada, 9, tabuada*9))
print("{} x {} = {}".format(tabuada, 10, tabuada*10))

#  FORMA 2 {:2} ESTA FUNÇÃO FAZ O ALINHAMENTO DOS NUMEROS NA COLUNA 
num = int(input("Digite um numero da tabuada:"))

print("{} x {:2} = {}".format(num, 1, num*1))
print("{} x {:2} = {}".format(num, 2, num*2))
print("{} x {:2} = {}".format(num, 3, num*3))
print("{} x {:2} = {}".format(num, 4, num*4))
print("{} x {:2} = {}".format(num, 5, num*5))
print("{} x {:2} = {}".format(num, 6, num*6))
print("{} x {:2} = {}".format(num, 7, num*7))
print("{} x {:2} = {}".format(num, 8, num*8))
print("{} x {:2} = {}".format(num, 9, num*9))
print("{} x {:2} = {}".format(num, 10, num*10))

