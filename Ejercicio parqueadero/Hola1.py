class Usuario():
    def __init__(self, cedula, nombre, rango):
        self.cedula = cedula
        self.nombre = nombre
        self.rango = rango
    
    def get_cedula(self):
        return self.cedula
    def set_cedula (self, dato_cedula):
        self.cedula = dato_cedula
    
    def get_nombre (self):
        return self.nombre
    def set_nombre (self, dato_nombre):
        self.nombre = dato_nombre
        
    def get_rango (self):
        return self.rango
    def set_rango (self, dato_rango):
        self.rango = dato_rango
             
    def imprimir_info(self):
        print (f"Nombre: {self.nombre}")
        print (f"Cedula: {self.cedula}")
        print (f"Tipo de Usuario: {self.rango}")