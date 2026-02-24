from Ingredientes import Cebolla, Tomate, Pasta
from Utileria import Cuchillo, Olla
from Cocina import Preguntas

def verificar_inventario():
    print("Entré a la verificación")

    ingredientes = ["Olla", "Cuchillo", "Cebolla", "Tomate", "Pasta", "Agua"]

    for ingredientes in ingredientes:
        while True:
            respuesta = input(f"¿Tienes {ingredientes}? (si/no): ").lower()
            if respuesta == "si":
                break
            elif respuesta == "no":
                print(f"No tienes {ingredientes}. No puedes continuar.")
                return False

    print("Inventario completo. ¡Puedes comenzar!")
    return True
    

def juego():
    if not verificar_inventario():
        return

    olla = Olla()
    cuchillo = Cuchillo()
    cebolla = Cebolla()
    tomate = Tomate()
    pasta = Pasta()
    agua = True

    print("---------Estacion de Batalla: COCINA---------")

    while not cebolla.esta_muerto():
        accion = input("¿Qué quieres hacer? (1-cortar/2-afilar cuchillo): ")
        if accion == "1":
            cuchillo.usar(cebolla)
            cebolla.mostrar_vida()
            if cebolla.esta_muerto():
                cebolla.morir()
        elif accion == "2":
            cuchillo.afilar()
        
    while not tomate.esta_muerto():
        accion = input("¿Qué quieres hacer? (1-cortar/2-afilar cuchillo): ")
        if accion == "1":
            cuchillo.usar(tomate)
            tomate.mostrar_vida()
            if tomate.esta_muerto():
                tomate.morir()
        elif accion == "2":
            cuchillo.afilar()
    
    print (" Has cortado los ingredientes. Agregando a la olla.... ")
    preguntas = Preguntas()
    preguntas.preguntar_capacidad()
    if not preguntas.agregar_olla():
        return
   

    while pasta.get_vida() < 100:
        respuesta = input("¿Quieres hervir la pasta? (s/n): ")
        if respuesta.lower() == "s":
            pasta.hervir()
        elif respuesta.lower() == "n":
            print("No herviste la pasta. Juego terminado.")
            return
    
    print ("Combate Culinario completado.")
    print ("La pasta ha sido servida con exito.")


juego()