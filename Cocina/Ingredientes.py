class Ingrediente:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
    
    def recibir_daño(self, daño):
        self.vida -= daño
        if self.vida < 0:
            self.vida = 0
       
    def morir(self):
        print (f"{self.nombre} Ha sido procesado correctamente.")
    
    def esta_muerto(self):
        return self.vida <= 0

    def get_vida(self):
        return self.vida

class Cebolla(Ingrediente):
    def __init__(self):
        super().__init__("Cebolla", 100)
    
    def mostrar_vida(self):
        print(f"La cebolla tiene {self.vida}% de vida restante.")

    def morir(self):
        print("La cebolla ha sido picada.")
    
class Tomate(Ingrediente):
    def __init__(self):
        super().__init__("Tomate", 100)

    def mostrar_vida(self):
        print(f"El tomate tiene {self.vida}% de vida restante.")
    
    def morir(self):
        print("El tomate ha sido picado.")

class Pasta(Ingrediente):
    def __init__(self):
        super().__init__("Pasta", 0)

    def hervir(self):
        self.vida += 20
        if self.vida > 100:
            self.vida = 100 
        print(f"La pasta está hirviendo. Hervida al {self.vida}%")

    def morir(self):
        print("La pasta ha sido cocida.")
