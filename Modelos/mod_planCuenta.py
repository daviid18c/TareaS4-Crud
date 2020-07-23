class ModPlanCuenta:
    def __init__(self, id=0, cod=0, gru=0, desc='', natu='', est=True):
        self.__id= id
        self.__codigo= cod
        self.__grupo= gru
        self.__descripcion= desc
        self.__naturaleza= natu
        self.__estado= est