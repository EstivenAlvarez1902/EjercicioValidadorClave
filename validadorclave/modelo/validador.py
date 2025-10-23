from abc import ABC, abstractmethod




class ReglaValidacion(ABC):


    def __init__(self, longitud_esperada):
        self.longitud_esperada = longitud_esperada


    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self.longitud_esperada



    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(c.isupper() for c in clave)



    def _contiene_minuscula(self, clave: str) -> bool:
        return any(c.islower() for c in clave)



    def _contiene_numero(self, clave: str) -> bool:
        return any(c.isdigit() for c in clave)


    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass





class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self):
        super().__init__(8)


    def contiene_caracter_especial(self, clave: str) -> bool:
        especiales = "@_#$%"
        return any(c in especiales for c in clave)

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):





class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self):
        super().__init__(6)

    def contiene_calisto(self, clave: str) -> bool:
        palabra = "calisto"
        if palabra.lower() not in clave.lower():
            return False

