# Ab  def frenar(self):
ea(self):
    return 3.14 * (self.radio ** 2)

class Cuadrado(Figura):
  def __init__(self, nombre, lado):
    super().__init__(nombre)
    self.lado = lado

  def calcular_area(self):
    return self.lado ** 2

# Ejecución
vehiculo = Vehiculo() # Error, no se puede instanciar una clase abstracta

cuenta = Cuenta(1000)
cuenta.depositar(500)
print(cuenta.get_saldo()) # 1500
cuenta.retirar(200)
print(cuenta.get_saldo()) # 1300

empleado = Empleado("Juan", "Pérez", 5000)
print(empleado.nombre) # Juan
print(empleado.salario) # 5000

gerente = Gerente("María", "González", 10000, "Ventas")
print(gerente.nombre) # María
print(gerente.departamento) # Ventas

figura1 = Circulo("Círculo", 5)
print(figura1.calcular_area()) # 78.5

figura2 = Cuadrado("Cuadrado", 4)
print(figura2.calcular_area()) # 16
