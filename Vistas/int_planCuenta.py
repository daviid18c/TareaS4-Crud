import sys
import os
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
sys.path.append(base_dir+'/Controladores')
sys.path.append(base_dir+'/Modelos')

from ctr_planCuenta import CtrPlanCuenta
from mod_planCuenta import ModPlanCuenta
from funciones import menu, PreContinuar
from int_grupo import consultarGru
 #Importo esta funcion de Vista 'int_grupo' para vizualizar los codigos de grupo 
 #y asi poder ingresar o modificar el campo en PlanCuenta

ctr = CtrPlanCuenta()
def insertarPlC():
    codigo = input('Ingrese codigo: ')
    consultarGru('V')
    grupo = input('Ingrese grupo(id): ')
    descripcion = input('Ingrese descripcion: ')
    naturaleza = input('Ingrese naturaleza(A/D): ')
    estado = input('Ingrese estado(1/0): ') #1=True ; 0=False
    if codigo.isnumeric() and grupo.isnumeric() and (naturaleza=='A' or naturaleza== 'D') and (estado==1 or naturaleza== 0):
        cli = ModPlanCuenta(cod=codigo, gru=grupo, desc=descripcion, natu=naturaleza, est=estado)
        if ctr.ingresar(cli):
            print('Registro grabado correctamente')
        else:
            print('Error al grabar el Registro')
    else:
        print('--Valores ingresados inadecuados')

def modificarPlC():
    idplc=input('ingrese id: ')
    codigo = input('Ingrese codigo: ')
    consultarGru('V')
    grupo = input('Ingrese grupo(id): ')
    descripcion = input('Ingrese descripcion: ')
    naturaleza = input('Ingrese naturaleza(A/D): ')
    estado = input('Ingrese estado(1/0): ') #1=True ; 0=False
    if idplc.isnumeric() and codigo.isnumeric() and grupo.isnumeric() and (naturaleza=='A' or naturaleza== 'D') and (estado==1 or naturaleza== 0):
        cli = ModPlanCuenta(id=idplc ,cod=codigo, gru=grupo, desc=descripcion, natu=naturaleza, est=estado)
        if ctr.modificar(cli):
            print('Registro modificado correctamente')
        else:
            print('Error al modificar el Registro')
    else:
        print('--Valores ingresados inadecuados')

def eliminarPlC():
    idplc = input('Ingrese id: ')
    cli = ModPlanCuenta(id=idplc)
    if idplc.isnumeric():
        if ctr.eliminar(cli):
            print('Registro eliminado correctamente')
        else:
            print('Error al eliminar el Registro')
    else:
        print('--Valores ingresados inadecuados')

#Modificacion: Añadi un motivo, para que se presente de manera directa 
# sin pedir un nombre, cuando se haga la eliminacion y modificacion
def consultarPlC(motivo):
    if motivo == 'C':
        buscar = input('Ingrese nombre de cuenta a buscar: ')
    else:
        buscar=''
    cli = ctr.consulta(buscar)
    print('-----------------------------------------------------------------------------------------------')
    print('{:^5} {:^3} {:^5} {:^3} {:^20} {:^3} {:^20} {:^3} {:^10} {:^3} {:^8}'.format('Id','|','Codigo','|','Grupo', '|', 'Descripcion', '|','Naturaleza','|','Estado'))
    print('-----------------------------------------------------------------------------------------------')
    for registro in cli:
        print('{:^5} {:^3} {:^6} {:^3} {:^20} {:^3} {:^20} {:^3} {:^10} {:^3} {:^8}'.format(registro[0],'|', registro[1],'|', registro[2],'|',registro[3],'|',registro[4],'|','True' if registro[5]==1 else 'False'))
    print('-----------------------------------------------------------------------------------------------')

def ejecutar_planCuenta():
    opc = ''
    while opc != '5':
        opc = str(menu(
            ['Ingresar', 'Modificar', 'Eliminar', 'Consultar', 'Retornar Menú Principal'],
            'MENU PLAN DE CUENTAS'))
        if opc == '1':
            print('\n<<<Insertar datos>>> ')
            insertarPlC()
            PreContinuar()
        elif opc == '2':
            print('\n<<<Modificar datos>>>')
            consultarPlC('M')
            modificarPlC()
            PreContinuar()
        elif opc == '3':
            print('\n<<<Eliminar datos>>>')
            consultarPlC('E')
            eliminarPlC()
            PreContinuar()
        elif opc == '4':
            print('\n<<<Consultar datos>>>')
            consultarPlC('C')
            PreContinuar()
        elif opc == '5':
            print('<<<Retornando al menú principal>>>')
            PreContinuar()
        elif opc != '5':
            print('Seleccione una opción correcta')
            PreContinuar()
