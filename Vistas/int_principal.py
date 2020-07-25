import sys
import os
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from funciones import menu, PreContinuar
from int_grupo import ejecutar_grupo
from int_planCuenta import ejecutar_planCuenta


def ejecutar_menuPrincipal():
    opc = ''
    while opc != '3':
        opc = str(menu(
            ['Grupo de cuentas', 'Plan de cuentas', 'Salir'],
            'MENU PRINCIPAL'))
        if opc == '1':
            print('\n<<<--------------->>> ')
            os.system('cls')
            ejecutar_grupo()
        elif opc == '2':
            print('\n<<<--------------->>>')
            os.system('cls')
            ejecutar_planCuenta()
        elif opc == '3':
            print('<<<Gracias por utilizar este sistema>>>')
        elif opc != '3':
            print('Seleccione una opción correcta')
            PreContinuar()
    
ejecutar_menuPrincipal()