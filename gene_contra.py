import random
def gene_contra():
    mayus = ['A', 'B', 'C', 'D']
    minus = ['a', 'b', 'c', 'd']
    simbolos = ['!', '*', '#', '&']
    numeros = ['1', '2', '3', '4'] 

    caracteres = mayus + minus + simbolos + numeros
    contra = []
    for i in range(15):
        carac_randon = random.choice(caracteres)
        contra.append(carac_randon)
    contra = "".join(contra) #une los caracteres
    return contra


def run():
    contra = gene_contra()
    print('Tu nueva contraseña es: ' + contra)


if __name__ == '__main__':
    run()