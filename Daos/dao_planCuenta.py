import sys
import os
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from conexion import Conector

class DaoPlanCuenta(Conector):
    def __init__(self):
        super().__init__()

    def consultar(self, buscar):
        result = False
        try:
            sql = "Select  pc.id, codigo, g.descripcion, pc.descripcion, naturaleza, estado FROM plancuenta pc INNER JOIN grupo g ON pc.grupo=g.id where pc.descripcion like '%" + str(buscar) + "%' order by pc.id"
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta: Plan de Cuenta",e)
            self.conn.rollback()
        finally: self.cerrar()
        return result

    def ingresar(self, planc):
        correcto = True
        try:
            sql = "insert into plancuenta (codigo, grupo, descripcion, naturaleza, estado) values (%s,%s,%s,%s,%s)"
            self.conectar()
            self.conector.execute(sql, (planc.codigo, planc.grupo, planc.descripcion, planc.naturaleza, planc.estado))
            self.conn.commit()
        except Exception as e:
            print("Error al insertar: Plan de Cuenta",e)
            correcto = False
            self.conn.rollback()
        finally: self.cerrar()
        return correcto

    def modificar(self, planc):
        correcto = True
        try:
            sql = 'Update plancuenta set codigo = %s, grupo = %s, descripcion  = %s, naturaleza = %s, estado = %s where id = %s'
            self.conectar()
            self.conector.execute(sql, (planc.codigo, planc.grupo, planc.descripcion, planc.naturaleza, planc.estado, planc.id))
            self.conn.commit()
        except Exception as e:
            print("Error al modificar: Plan de Cuenta",e)
            correcto = False
            self.conn.rollback()
        finally: self.cerrar()
        return correcto

    def eliminar(self, planc):
        correcto = True
        try:
            sql = 'delete from plancuenta where id = %s'
            self.conectar()
            self.conector.execute(sql, (planc.id))
            self.conn.commit()
        except Exception as e:
            print("Error al eliminar: Plan de Cuenta",e)
            correcto = False
            self.conn.rollback()
        finally: self.cerrar()
        return correcto
