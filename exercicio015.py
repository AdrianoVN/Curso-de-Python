# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE
# DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA
# E 0.15 POR KM RODADO. 

# FORMA 1 OS VALORES JA ESTÃO PRÉ-DEFINIDOS NA FORMULA DE CALCULO

print("========== Desafio 015 ==========")
dias = int(input("Por quantos dias o carro foi alugado? "))
km = int(input("Qual a quantidade de km percorrida? "))
pagamento_total = (dias * 60) + (km * 0.15)
print("O total a pagar é de R${:.2f}".format(pagamento_total))

# FORMA 2 O USUÁRIO FARÁ A INSERÇÃO DE TODOS OS VALORES
dias = int(input("Por quantos dias o carro foi alugado? "))
km = int(input("Qual a quantidade de km percorrida? "))
preco_diaria = float(input("Qual o valor da diaria do veiculo? "))
preco_km = float(input("Qual o valor por km rodado? "))
pagamento_total = (preco_diaria * dias) + (preco_km * km)
print("O total a pagar é de R${:.2f}".format(pagamento_total))

    
 