# tp2.py - Trabajo Práctico Nro 2

def mayores_que(x, valores):
    """Cuenta cuántos valores en la lista son mayores que x."""
    count = 0
    for v in valores:
        if v > x:
            count += 1
    return count

def todos_iguales(lista):
    """Indica si todos los elementos son iguales."""
    if not lista:
        return True
    first = lista[0]
    for item in lista[1:]:
        if item != first:
            return False
    return True

def todos_distintos(lista):
    """Indica si todos los elementos son distintos."""
    if not lista:
        return True
    seen = set()
    for item in lista:
        if item in seen:
            return False
        seen.add(item)
    return True

def contar_letras(oracion):
    """Diccionario con conteo de letras (case insensitive, ignora espacios)."""
    from collections import defaultdict
    conteo = defaultdict(int)
    for char in oracion:
        if char.isalpha():
            conteo[char.lower()] += 1
    return dict(conteo)

def contar_vocales(oracion):
    """Diccionario con conteo de vocales."""
    vocales = 'aeiou'
    conteo = {v: 0 for v in vocales}
    for char in oracion.lower():
        if char in conteo:
            conteo[char] += 1
    return conteo

def programa_punto2():
    """Programa para punto 2."""
    n = int(input("¿Cuántos datos ingresará? "))
    datos = [float(input(f"Dato {i+1}: ")) for i in range(n)]
    if datos:
        prom = sum(datos) / len(datos)
        print(sum(1 for d in datos if d > prom))

if __name__ == "__main__":
    print('Pruebas TP2:')
    print('mayores_que(5, [1,6,3,7,4]):', mayores_que(5, [1,6,3,7,4]))
    print('todos_iguales([1,1,1]):', todos_iguales([1,1,1]))
    print('todos_distintos([1,2,3]):', todos_distintos([1,2,3]))
    print('contar_letras("Hola Mundo"):', contar_letras("Hola Mundo"))
    print('contar_vocales("Hola Mundo"):', contar_vocales("Hola Mundo"))