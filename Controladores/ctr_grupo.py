import os
import sys
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir+'/Daos')
sys.path.append(base_dir+'/Modelos')

from dao_grupo import DaoGrupo
from mod_grupo import ModGrupo

class CtrGrupo:
    def __init__(self, gru=None):
        self.grupo = gru

    def consulta(self, buscar):
        objDao = DaoGrupo()
        return objDao.consultar(buscar)

    def ingresar(self, gru):
        objDao = DaoGrupo()
        return objDao.ingresar(gru)

    def modificar(self, gru):
        objDao = DaoGrupo()
        return objDao.modificar(gru)

    def eliminar(self, gru):
        objDao = DaoGrupo()
        return objDao.eliminar(gru)