from hola1 import Cebolla, Tomate, Pasta
from hola2 import Cuchillo, Olla

def verificar_inventario():
    print("Entré a la verificación")

    tiene_olla = input("¿Tienes Olla? (s/n): ")
    tiene_cuchillo = input("¿Tienes Cuchillo? (s/n): ")
    tiene_cebolla = input("¿Tienes Cebolla? (s/n): ")
    tiene_tomate = input("¿Tienes Tomate? (s/n): ")
    tiene_pastas = input("¿Tienes Pastas? (s/n): ")
    tiene_agua = input("¿Tienes Agua? (s/n): ")

    if (tiene_olla.lower() == "s" and
        tiene_cuchillo.lower() == "s" and
        tiene_cebolla.lower() == "s" and
        tiene_tomate.lower() == "s" and
        tiene_pastas.lower() == "s" and
        tiene_agua.lower() == "s"):

        print("Inventario completo. ¡Puedes comenzar!")
        return True
    else:
        print("Faltan elementos. No puedes iniciar la receta.")
        return False

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
    olla.agregar(cebolla)
    olla.agregar(tomate)
    olla.agregar(pasta)

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