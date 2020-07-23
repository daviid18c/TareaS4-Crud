import sys
import os
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
sys.path.append(base_dir+'/Controladores')
sys.path.append(base_dir+'/Modelos')

from ctr_grupo import CtrGrupo
from mod_grupo import ModGrupo
from funciones import menu, PreContinuar

ctr = CtrGrupo()
def insertar(rango):
    for i in range(int(rango)):
        descripcion = input('Ingrese descripcion: ')
        cli = ModGrupo(desc=descripcion)
        if ctr.ingresar(cli):
            print('Registro grabado correctamente')
        else:
            print('Error al grabar el Registro')

def modificar():
    codigo = input('Ingrese codigo: ')
    descripcion = input('Ingrese descripcion: ')
    cli = ModGrupo(cod=codigo,desc=descripcion)
    if ctr.modificar(cli):
        print('Registro modificado correctamente')
    else:
        print('Error al modificar el Registro')

def eliminar():
    codigo = input('--Ingrese codigo: ')
    cli = ModGrupo(cod=codigo)
    if ctr.eliminar(cli):
        print('Registro eliminado correctamente')
    else:
        print('Error al eliminar el Registro')

#Modificacion: Añadi un motivo, para que se presente de manera directa 
# sin pedir un nombre, cuando se haga la eliminacion y modificacion
def consultar(motivo):
    if motivo == 'C':
        buscar = input('Ingrese nombre a buscar: ')
    else:
        buscar=''
    cli = ctr.consulta(buscar)
    print('{:^10} {:^3} {:^20}'.format('Codigo','|', 'Descripcion'))
    for registro in cli:
        print('{:^10} {:^3} {:^20}'.format(registro[0],'|', registro[1]))


def ejecutar_grupo():
    opc = ''
    while opc != '5':
        opc = str(menu(
            ['Ingresar', 'Modificar', 'Eliminar', 'Consultar', 'Salir'],
            'Menu Grupo'))
        if opc == '1':
            print('\n<<<Insertar datos>>> ')
            valor = input('-Ingrese cantidad de datos a Ingresar')
            insertar(valor)
            PreContinuar()
        elif opc == '2':
            print('\n<<<Modificar datos>>>')
            consultar('M')
            modificar()
            PreContinuar()
        elif opc == '3':
            print('\n<<<Eliminar datos>>>')
            consultar('E')
            eliminar()
            PreContinuar()
        elif opc == '4':
            print('\n<<<Consultar datos>>>')
            consultar('C')
            PreContinuar()
        elif opc == '5':
            print('<<<Gracias por usar el Sistema>>>')
            PreContinuar()
        elif opc != '5':
            print('Seleccione una opción correcta')
            PreContinuar()
ejecutar_grupo()