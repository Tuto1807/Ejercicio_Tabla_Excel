class Parqueadero:
    def __init__(self, usuario, carro):
        self.usuario = usuario
        self.carro = carro 
        self.fecha_entrada = ""
        self.hora_entrada = ""
        self.hora_salida = ""
        self.estado = ""
        self.textotabla = "
        
        
    def registrar_entrada(self):
        self.fecha_entrada = input("Ingrese la fecha de entrada (DD/MM/AAAA): ")
        self.hora_entrada = input("Ingrese la hora de entrada (HH:MM): ")
        self.estado = "ADENTRO"
        print("Entrada registrada correctamente.")
        
    def registrar_salida(self):
        self.hora_salida = input("Ingrese la hora de salida (HH:MM)")
        self.estado = "SALIÓ"
        print("Salida registrada correctamente.")
    
    def mostrar_info(self):
        self.textotabla = self.textotabla + f"{'Cedula':<12} | {'Nombre':<12} | {'Rango':<10} | {'Marca':<10} | {'Placa':<12} | {'Color':<10} | {'Fecha Entrada':<12} | {'Hora Entrada':<10} | {'Hora Salida':<10} | {'Estado':<10} \n"
        self.textotabla = self.textotabla + "-"*130 + "\n"
        self.textotabla += f"{self.usuario.cedula:<12} | {self.usuario.nombre:<12} | {self.usuario.rango:<10} | {self.carro.placa:<10} | {self.carro.marca:<12} | {self.carro.color:<10} | {self.fecha_entrada:<12} | {self.hora_entrada:<10} | {self.hora_salida:<10} | {self.estado:<10}\n"

        print(self.textotabla)
