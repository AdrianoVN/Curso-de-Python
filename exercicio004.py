# DISSECANDO UMA VARIAVEL
# FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA SEU TIPO PRIMITIVO E TODAS
# AS INFORMAÇÕES POSSIVEIS SOBRE ELA. 

print("========== Desafio 004 ==========")

a = input("digite algo:")
print("O tipo primitivo desse valor é:", type(a)) # type - tipo primitivo
print("So tem espaços?", a.isspace()) # isspace() contem apenas espaços
print("É somente numerico?", a.isnumeric()) # isnumeric() contem apenas caracteres numericos
print("É alfabetico?", a.isalpha()) # isalpha() contem apenas caracteres alfabeticos
print("É alfanumerico?", a.isalnum()) # isalnum() contem caracteres numericos e alfabeticos 
print("Esta em maiusculas?", a.isupper()) # isupper() contem apenas caracteres maiusculos
print("Esta em minusculas?", a.islower()) # islower() contem apenas caracteres minusculos
print("Esta capítalizada", a.istitle()) # istitle() contem caracteres maiusculos e minusculos





 

 


