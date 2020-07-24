import os
import sys
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir+'/Daos')
sys.path.append(base_dir+'/Modelos')

from dao_planCuenta import DaoPlanCuenta
from mod_planCuenta import ModPlanCuenta

class CtrPlanCuenta:
    def __init__(self, planc=None):
        self.planCuenta = planc

    def consulta(self, buscar):
        objDao = DaoPlanCuenta()
        return objDao.consultar(buscar)

    def ingresar(self, planc):
        objDao = DaoPlanCuenta()
        return objDao.ingresar(planc)

    def modificar(self, planc):
        objDao = DaoPlanCuenta()
        return objDao.modificar(planc)

    def eliminar(self, planc):
        objDao = DaoPlanCuenta()
        return objDao.eliminar(planc)