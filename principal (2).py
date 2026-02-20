from user import Usuario
from number import Numero
from calc import Calculadora

# Crear objetos (cedula, nombre)
usuario1 = Usuario("10191239", "Adriam")
numero1 = Numero(5)
numero2 = Numero(3)

# Calculadora trabaja con objetos Numero
calculadora1 = Calculadora(numero1, numero2)

# Obtener resultados (se calculan directamente)
suma = calculadora1.get_suma()
resta = calculadora1.get_resta()
multi = calculadora1.get_multi()
divi = calculadora1.get_divi()

# Manejo de fecha
calculadora1.set_fecha("2026-02-18")
fecha_actual = calculadora1.get_fecha()

# Mostrar información
usuario1.imprimir_info()
print(calculadora1.get_info())
numero1.imprimir_info()
numero2.imprimir_info()
# Permitir que el usuario elija la operación
calculadora1.set_info()

print(f"Operacion elegida (guardada): {calculadora1.operacion}")
print(f"Resultado guardado: {calculadora1.resultado}")
