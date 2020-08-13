pesos = input ("¿Cuantos pesos argetinos tienes?")
pesos = float(pesos)
valor_dolar = 107
dolares = pesos / valor_dolar
dolares = round(dolares,2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")