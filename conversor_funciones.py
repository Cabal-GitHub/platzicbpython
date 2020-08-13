menu = """
Bienvenido al conversor de monedas 😁
1 - Pesos Argentinos
2 - Pesos Colombianos
3 - Pesos Mexicanos

Elige una opción: 
"""
opcion = int(input(menu))
def conversor(moneda,valor):
    pesos = input ("¿Cuantos pesos "+ moneda + " tienes?")
    pesos = float(pesos)
    dolares = pesos / valor
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
if opcion == 1:
    conversor("Argentinos",65)
elif opcion == 2:
    conversor("Colombianos",3875)
elif opcion == 3:
    conversor("Mexicanos",24)
else:
    print("ingrese una opción correcta")