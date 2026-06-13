# TP2 - Ejercicios de Programación

def mayores_que(x, valores):
    """Cuenta cuántos valores en la lista son mayores que x."""
    if not valores:
        return 0
    count = 0
    for v in valores:
        if v > x:
            count += 1
    return count

def todos_iguales(lista):
    """Indica si todos los elementos de la lista son iguales."""
    if not lista:
        return True  # o False, según convención
    primero = lista[0]
    for elem in lista[1:]:
        if elem != primero:
            return False
    return True

def todos_distintos(lista):
    """Indica si todos los elementos de la lista son distintos."""
    if not lista:
        return True
    return len(lista) == len(set(lista))

def contar_letras(oracion):
    """Retorna diccionario con conteo de letras (case insensitive, ignora espacios)."""
    conteo = {}
    for char in oracion:
        if char.isalpha():
            letra = char.lower()
            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1
    return conteo

def contar_vocales(oracion):
    """Retorna diccionario con conteo de vocales (a,e,i,o,u), 0 si no aparece."""
    vocales = 'aeiou'
    conteo = {v: 0 for v in vocales}
    for char in oracion.lower():
        if char in conteo:
            conteo[char] += 1
    return conteo

# Ejercicio 2: Programa principal
if __name__ == "__main__":
    print("Ejercicio 2:")
    n = int(input("Ingrese la cantidad de datos a ingresar: "))
    datos = []
    for i in range(n):
        dato = float(input(f"Ingrese dato {i+1}: "))
        datos.append(dato)
    if datos:
        promedio = sum(datos) / len(datos)
        mayores = sum(1 for d in datos if d > promedio)
        print(f"Cantidad de datos mayores al promedio: {mayores}")
    else:
        print("No se ingresaron datos.")

# Ejemplos de uso
print("\nEjemplos:")
print("mayores_que(5, [3,6,7,4,8]):", mayores_que(5, [3,6,7,4,8]))
print("todos_iguales([1,1,1]):", todos_iguales([1,1,1]))
print("todos_distintos([1,2,3]):", todos_distintos([1,2,3]))
print("contar_letras('Hola Mundo'):", contar_letras('Hola Mundo'))
print("contar_vocales('Hola Mundo'):", contar_vocales('Hola Mundo'))