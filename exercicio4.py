# TIPOS PRIMITIVOS DE SAIDAS DE DADOS: 
# int (NUMERO INTEIRO) , float (NUMERO REAIS DE PONTO FLUTUANTE), bool(BOLEANOS), str (STRING).

# int = NUMERO INTEIROS EX.1, 2, 3, 4, 0, - 1 - 10, 9875 
# float = NUMERO REAIS OU NUMEROS DE PONTO FLUTUANTE EX. (4.5), (0.076), (-15.223)
# bool = NUMEROS BOLEANOS OU LÓGICOS EX. True (VERDADEIRO) False (FALSO)
# str = STRING É UMA SEQUENCIA DE LETRAS, NUMEROS OU SIMBOLOS. EX.("NOME", "1234", "$+%#@") FICAM ENTRE AS ASPAS.

# FAÇA A SOMA DE DOIS NUMEROS E A CONCATENAÇÃO DO PRINT 
numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite novamente outro valor: "))
s = (numero1 + numero2)
print ("O resultado da soma é igual:",s)

# EXEMPLO 2 DE CONCATENAÇÃO DO PRINT
numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite novamente outro valor: "))
s = (numero1 + numero2)
print ("A Soma entre {} + {} = {}".format(numero1, numero2, s))

# FAÇA A UNIÃO ENTRE DOIS NUMEROS
numero1 = int(input("Digite o numero: "))
numero2 = int(input("Digite o outro numero: "))
print("a união entre os dois numeros:",numero1, numero2)
print(numero1,numero2)


# NUMEROS REAIS DE PONTO FLUTUANTE (float)
numero = float(input("Digite um numero: "))
print("O numero é do tipo ponto flutuante:", numero)


# NUMERO INTEIRO (int)
numero = int(input("Digite o numero: "))
print ("O numero é do tipo inteiro: ", numero)


