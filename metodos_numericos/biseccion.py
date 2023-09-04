def biseccion(f, a, b, tol=1e-6, max_iter=1000):
    """
    Método de bisección para encontrar una raíz de la función f en el intervalo [a, b].

    Parámetros:
    - f: función para la cual se busca una raíz
    - a, b: extremos del intervalo
    - tol: tolerancia deseada para la solución
    - max_iter: número máximo de iteraciones permitidas

    Retorna:
    - Una aproximación de la raíz si se encuentra en el intervalo dado.
    - None si no se cumple el criterio de parada en max_iter iteraciones.
    """

    if f(a) * f(b) > 0:
        print("El método de bisección requiere que f(a) y f(b) tengan signos opuestos.")
        return None

    iteracion = 0
    while (b - a) / 2.0 > tol and iteracion < max_iter:
        c = (a + b) / 2.0
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteracion += 1

    if iteracion == max_iter:
        print("Máximo número de iteraciones alcanzado.")
        return None

    return (a + b) / 2.0

# Ejemplo de uso:
import math
f = lambda x: x**3 - 2*x**2 + 4*x - 8
raiz = biseccion(f, 1, 6)
if raiz is not None:
    print(f"Raíz encontrada: {raiz}")
else:
    print("No se encontró una raíz en el intervalo dado.")
