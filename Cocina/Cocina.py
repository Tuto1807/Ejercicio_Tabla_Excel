class Preguntas:
    def __init__(self):
        pass

    def preguntar_capacidad(self):
        while True:
            respuesta = input("¿Cuanta capacidad tiene tu olla (Mucha/Poca)?: ").lower()
            
            if respuesta == "mucha":
                print("Tu olla es grande, puedes agregar mas ingredientes.")
                break
            elif respuesta == "poca":
                print("Tu olla es pequeña, no agregues mas ingredientes.")
                break
            else:
                print("Respuesta inválida. Escribe 'Mucha' o 'Poca'.")

    def agregar_olla(self):

        
        while True:
            respuesta = input("¿Desea agregar Cebolla a tu olla (si/no)?: ").lower()
            
            if respuesta == "si":
                print("Has agregado cebolla a tu olla.")
                break
            elif respuesta == "no":
                print("No has agregado cebolla a tu olla. Juego terminado.")
                return False
            else:
                print("Respuesta inválida. Escribe 'si' o 'no'.")

        
        while True:
            respuesta = input("¿Desea agregar Tomate a tu olla (si/no)?: ").lower()
            
            if respuesta == "si":
                print("Has agregado tomate a tu olla.")
                break
            elif respuesta == "no":
                print("No has agregado tomate a tu olla. Juego terminado.")
                return False
            else:
                print("Respuesta inválida. Escribe 'si' o 'no'.")

        
        while True:
            respuesta = input("¿Desea agregar Pasta a tu olla (si/no)?: ").lower()
            
            if respuesta == "si":
                print("Has agregado pasta a tu olla.")
                break
            elif respuesta == "no":
                print("No has agregado pasta a tu olla. Juego terminado.")
                return False
            else:
                print("Respuesta inválida. Escribe 'si' o 'no'.")

        return True