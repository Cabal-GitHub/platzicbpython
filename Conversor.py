menu = """
Bienvenido al conversor de monedas 😁
1 - Pesos Argentinos
2 - Pesos Colombianos
3 - Pesos Mexicanos

Elige una opción: 
"""
opcion = int(input(menu))
if opcion == 1:
    pesos = input ("¿Cuantos pesos argetinos tienes?")
    pesos = float(pesos)
    valor_dolar = 107
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 2:
    pesos = input ("¿Cuantos pesos Colombianos tienes?")
    pesos = float(pesos)
    valor_dolar = 3785
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 3:
    pesos = input ("¿Cuantos pesos Mexicanos tienes?")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
else:
    print("ingrese una opción correcta")
