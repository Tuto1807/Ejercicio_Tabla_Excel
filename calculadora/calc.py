class Calculadora():
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.fecha = ""
        self.operacion = ""
        self.resultado = ""
        self.info = ""
    
    def get_fecha(self):
        return self.fecha
    
    def set_fecha(self, dato_fecha):
        self.fecha = dato_fecha
    
    def get_suma(self):
        return self.num1.get_numero() + self.num2.get_numero()
    
    def set_suma(self,nueva_suma):
        nueva_suma=(self.num1.get_numero() + self.num2.get_numero())
        self.suma= nueva_suma
    
    def get_resta(self):
        return self.num1.get_numero() - self.num2.get_numero()
    
    def set_resta(self,nueva_resta):
        nueva_resta=(self.num1.get_numero() - self.num2.get_numero())
        self.resta= nueva_resta

    def get_multi(self):
        return self.num1.get_numero() * self.num2.get_numero()
    
    def set_multi(self,nueva_multi):
        nueva_multi=(self.num1.get_numero() * self.num2.get_numero())
        self.multi= nueva_multi

    def get_divi(self):
        return self.num1.get_numero() / self.num2.get_numero()
    
    def set_divi(self,nueva_divi):
        nueva_divi=(self.num1.get_numero() / self.num2.get_numero())
        self.divi= nueva_divi
    
    def get_info(self):
        return f"Num1: {self.num1.get_numero()} | Num2: {self.num2.get_numero()} | Fecha: {self.fecha}"
    
    def set_info(self):
        print ("Elige una opcion 1.sumar, 2.restar, 3.multiplicar, 4.dividir")
        opcion = int(input("Elige una opcion: "))
        

        if opcion==1:
            self.operacion = "suma"
            self.resultado = self.get_suma()
        elif opcion==2:
            self.operacion = "resta"
            self.resultado = self.get_resta()
        elif opcion==3:
            self.operacion = "multiplicacion"
            self.resultado = self.get_multi()
        elif opcion==4:
            self.operacion = "division"
            self.resultado = self.get_divi()
        else:
            print("Error: opcion no valida")
            return

        print("Operacion elegida:", self.operacion)
        print("Resultado:", self.resultado)
