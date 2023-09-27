def regula_falsi_modificada(f, a, b, tol=1e-6, max_iter=1000):
    """
    Método de regula falsi modificada para encontrar una raíz de la función f en el intervalo [a, b].

    Parámetros:
    - f: función para la cual se busca una raíz
    - a, b: extremos del intervalo
    - tol: tolerancia deseada para la solución
    - max_iter: número maximo de iteraciones permitidas
    """
    if f(a) * f(b) > 0:
        print("El método de regula falsi modificada requiere que f(a) y f(b) tengan signos opuestos.")
        return None

    iteracion = 1
    
    print("  i     a               b               c               f(a)            f(c)")
    print("-------------------------------------------------------------------------------------")
    
    F = f(a)
    G = f(b)
    w = f(a)
    
    c = ((a*f(b))-(b*f(a)))/(f(b)-f(a))
    
    while abs(f(c)) > tol and iteracion < max_iter:
        print(f"{iteracion:>3} {a:>15.9f} {b:>15.9f} {c:>15.9f} {f(a):>15.9f} {f(c):>15.9f}")
        if f(c) == 0: # Si la raíz es cero, se retorna la aproximación.
            break
        if f(c) * f(a) < 0: # Si la raíz está entre a y c, se cambia el intervalo.
            b = c
            G = f(c)
            if w* G > 0:
                F = F/2
        else:
            a = c
            F = f(c)
            if w* F > 0:
                G = G/2
        
        w = f(c)
        c = ((a*G)-(b*F))/(G-F)
        iteracion += 1
    
    print(f"{iteracion:>3} {a:>15.9f} {b:>15.9f} {c:>15.9f} {f(a):>15.9f} {f(c):>15.9f}")
    if iteracion == max_iter:
        print("Máximo número de iteraciones alcanzado.")
        
    return c, iteracion


# Ejemplo de uso:
import math
f1 = lambda x: x**3 - 2*x**2 + 4*x - 8

def f2(x):
    return math.exp(-x) - math.sin(x)

print("\n\n\tMétodo de regula falsi modificada para encontrar una raíz de la función f2 en el intervalo [0, 1], toleracion = {}.\n\n".format(0.001))

raiz, iteraciones = regula_falsi_modificada(f2, 0, 1, 0.001)
if raiz is not None:
    print(f"\nRaíz encontrada: {raiz}")
    print(f"Número de iteraciones: {iteraciones}")
else:
    print("No se encontró una raíz en el intervalo dado.")