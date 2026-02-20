from Hola1 import Usuario
from Hola2 import Carro
from Hola3 import Parqueadero

print ("-------Sistema de parqueadero---------")

cedula = input("Ingrese su cedula:")
nombre = input ("Ingrese su nombre:")
rango = input("Ingrese el Tipo de usuario que es: (ADMIN/CLIENTE)")

usuario = Usuario(cedula, nombre, rango)

placa = input("Ingrese la placa del carro: ")
color = input ("Ingrese el color del carro: ")
marca = input("Ingrese la marca del carro: ")

carro = Carro (placa, color, marca)
    

parqueo = Parqueadero(usuario, carro)

parqueo.registrar_entrada()

opcion =  input ("Desea Registrar la salida? (Si/No)")

if opcion == "Si":
    parqueo.registrar_salida()
    
parqueo.mostrar_info()

