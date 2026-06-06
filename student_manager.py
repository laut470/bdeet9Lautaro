print("=== Gestor de Datos de Estudiante - Python ===")

# Solicitar datos
nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad: "))
promedio = float(input("Ingrese el promedio: "))
activo = input("¿Está activo? (sí/no): ").lower() == 'sí'

# Mostrar datos
print("\nDatos del estudiante:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Promedio: {promedio}")
print(f"Activo: {'Sí' if activo else 'No'}")

# Operaciones
edad += 1
promedio_entero = round(promedio)
estado = "Activo" if activo else "Inactivo"

print("\nDespués de operaciones:")
print(f"Edad incrementada: {edad}")
print(f"Promedio redondeado: {promedio_entero}")
print(f"Estado: {estado}")

# Mostrar tipos
print("\nTipos de datos:")
print(f"Nombre: {type(nombre)}")
print(f"Edad: {type(edad)}")
print(f"Promedio: {type(promedio)}")
print(f"Activo: {type(activo)}")

# Casos especiales
print("\nCasos especiales:")
try:
    edad_decimal = 20.5
    edad_int = int(edad_decimal)
    print(f"Asignar decimal {edad_decimal} a entero: {edad_int}")
except Exception as e:
    print(f"Error: {e}")

try:
    suma = 5 + "10"
except Exception as e:
    print(f"Sumar número + string: Error - {e}")

# En Python, variable sin inicializar da error
print("Usar variable sin inicializar: Error (NameError)")

print("\nPrograma completado.")