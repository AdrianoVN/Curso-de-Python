# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO 
# EM CENTIMETROS E MILIMETROS
print("========== Desafio 008 ==========")

metros = float(input("digite o valor em metros: "))
centimetros = (100 * metros)
milimetros = (10 * centimetros)
print("A medida de {:.2f} metro(s) equivale a {:.2f} cm e {:.2f} mm:".format(metros, centimetros, milimetros))
 
 # CONVERSOR DE MEDIDAS
 
medida_metros = float(input("Digite a medida em metros: "))
kilometros_km = (medida_metros / 1000) 
hectometros_hm = (medida_metros / 100)
decametro_dam = (medida_metros / 10)
decimetro_dm = (medida_metros * 10)
centimetros_cm = (medida_metros * 100)
milimetros_mm = (medida_metros * 1000)
print("A medida de {} metros equivale a {} kilometros, {} hectometros, {} decametros, {} decimetros, {} centimetros, {} milimetros".format(medida_metros, kilometros_km, hectometros_hm, decametro_dam, decimetro_dm, centimetros_cm, milimetros_mm))