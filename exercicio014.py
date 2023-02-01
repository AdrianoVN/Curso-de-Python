# CONVERSOR DE TEMPERATURAS

# CELSIUS PARA FAHRENHEIT

print("========== Conversão de Temperatura Celcius C. para Fahrenheit F.) ==========")
celsius = float(input("Digite a temperatura em Celsius C: "))
fahrenheit = (celsius * 1.8) + 32
print("A temperatura de {:.0f}C corresponde a {:.0f}F".format(celsius, fahrenheit))

# FAHRENHEIT PARA CELSIUS

print("========== Conversão de Temperatura (Fahrenheit F. para Celcius C.)==========")

fahrenheit = float(input("Digite a temperatura em Fahrenheit F: "))
celsius = (fahrenheit - 32) / 1.8
print("A temperaturade de {:.0f}F corresponde a: {:.0f}C".format(fahrenheit, celsius))
