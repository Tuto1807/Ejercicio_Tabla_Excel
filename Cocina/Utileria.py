class Cuchillo:
    def __init__(self):
        self._filo = 100
    
    def usar(self, ingrediente):
        if self._filo <= 0:
            print("El cuchillo está sin filo. No puedes usarlo.")
            return
        ingrediente.recibir_daño(20)
        self._filo -= 25
        print(f"Usaste el cuchillo para cortar {ingrediente.nombre}. Filo restante: {self._filo}%")

    def afilar(self):
        self._filo = 100
        print("Has afilado el cuchillo. Filo al 100%.")

class Olla:
    def __init__(self):
        self._capacidad = []
    
    def agregar(self, ingrediente):
        self._capacidad.append(ingrediente)
        print(f"Agregaste {ingrediente.nombre} a la olla.")