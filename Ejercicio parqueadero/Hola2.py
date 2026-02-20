class Carro:
    def __init__(self, marca, color, placa):
        self.marca = marca
        self.color = color
        self.placa = placa
    
    def get_marca (self):
        return self.marca
    def set_marca(self, dato_marca):
        self.marca = dato_marca
    
    def get_color (self):
        return self.color
    def set_color (self, dato_color):
        self.color = dato_color
    
    def get_placa(self):
        return self.placa
    def set_placa (self, dato_placa):
        self.placa = dato_placa
    
    
    def imprimir_datos(self):
        print(f"Marca carro: {self.marca}")
        print(f"Color Carro: {self.color}")
        print(f"Placa Carro: {self.placa}")
        
        