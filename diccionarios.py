def run():
    mi_direccionario = {
        'llave1' : 1,
        'llave2' : 2,
        'llave3' : 3,
    }
    # print(mi_direccionario['llave3'])
    for llave, valor in mi_direccionario.items():
        print(llave + '=' + str(valor))

if __name__ == '__main__':
    run()