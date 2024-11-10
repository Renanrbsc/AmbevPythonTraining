from Aula50_Desafio_Fortwo_OO.Resolucoes.r2.local import Local

class Aviao(Local):
    def __init__(self):
        self.__pessoas = []
        super().__init__(self.__pessoas)

    def __str__(self):
        return 'Avião'