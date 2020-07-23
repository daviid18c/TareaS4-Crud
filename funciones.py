import os

def menu(opciones, titulo):
    print('\n* * * * * * * {} * * * * * * *'.format(titulo))
    for op in range(0, len(opciones)):
        print("{}) {}".format(op+1, opciones[op]))
    opc = input('Elija Opcion [1...{}]: '.format(len(opciones)))
    return opc

def PreContinuar ():
    input('Presione "Enter" para continuar')
    os.system('cls')