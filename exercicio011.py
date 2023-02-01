# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS 
# CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSARIA PARA PINTA-LA 
# SABENDO QUE CADA LITRO DE TINTA, PINTA UMA AREA DE 2 METROS QUADRADO.
print("========== Desafio 011 ==========")

largura_parede = float(input("Digite a largura da parede em metros: "))
altura_parede = float(input( "Digite a altura da parede em metros: "))
rendimento_por_litro = float(input("Digite o rendimento por litro: "))
area_total = (largura_parede * altura_parede)
print("A area total a ser pintada é de:",area_total, "metros")

litros_de_tinta = (largura_parede * altura_parede) / rendimento_por_litro
print("Rendimento por litro:", rendimento_por_litro, "metros quadrados")
print("A quantidade de tinta necessaria para pintar uma area de {}m x {}m é de: {} Litros de tinta ".format(largura_parede, altura_parede, litros_de_tinta))
