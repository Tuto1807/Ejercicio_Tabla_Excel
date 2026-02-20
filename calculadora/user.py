class Usuario:
    def __init__(self,cedula,nombres):
        self.nombres=nombres
        self.cedula=cedula
    
    def get_nombre(self):
        return self.nombres
    
    def set_nombre(self,dato_nombre):
        self.nombres=dato_nombre

    def get_cedula(self):
        return self.cedula
    
    def set_cedula(self,dato_cedula):
        self.cedula=dato_cedula

    def imprimir_info(self):
        print(f"Cedula: {self.cedula}")
        print(f"Nombre: {self.nombres}")

