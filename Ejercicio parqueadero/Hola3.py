class Parqueadero:
    def __init__(self, usuario, carro):
        self.usuario = usuario
        self.carro = carro 
        self.fecha_entrada = ""
        self.hora_entrada = ""
        self.hora_salida = ""
        self.estado = ""
        
        
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
        print("Fecha de entrada:", self.fecha_entrada)
        print("Hora de entrada:", self.hora_entrada)
        print("Hora de salida:", self.hora_salida)
        print("Estado:", self.estado)