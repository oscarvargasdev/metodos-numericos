def secante(f, x0, x1, tol=1e-6, max_iter=1000):
    """
    Método de la secante para encontrar una raíz de la función f en el punto x0.
    Parámetros:
    - f: función para la cual se busca una raíz
    - x0: punto en el que se busca la raíz
    - x1: punto en el que se busca la raíz
    - tol: tolerancia deseada para la solución
    - max_iter: nónmero máximo de iteraciones permitidas
    """
    x_prev = x0  # Guarda el valor anterior de x
    x = x1
    x_sig = (x_prev*f(x)-x*f(x_prev))/(f(x)-f(x_prev))
    iteraciones = 1
    print("  i     x_ant                xi                   xi+1                           |f(xi))|                           |xi+1 - xi|")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    while (abs(f(x)) > tol) or ((abs(x_sig - x) > tol) and  (iteraciones < max_iter)):
        print("  {i}     {x_ant:.14f}     {xi:.14f}     {x_sig:.14f}                 {f:.14f}                              {dif:.14f}".format(i = iteraciones, x_ant=float(x_prev), xi = float(x), x_sig=float(x_sig), f = float(abs(f(x))), dif = abs(float(x_sig - x))))
        
        x_prev = x  # Guarda el valor anterior de x
        x = x_sig
        x_sig = (x_prev*f(x)-x*f(x_prev))/(f(x)-f(x_prev))
        iteraciones += 1
    
    print("  {i}     {x_ant:.14f}     {xi:.14f}     {x_sig:.14f}                 {f:.14f}                              {dif:.14f}".format(i = iteraciones, x_ant=float(x_prev), xi = float(x), x_sig=float(x_sig), f = float(abs(f(x))), dif = abs(float(x_sig - x))))
    
    if iteraciones == max_iter:
        print("Máximo nàmero de iteraciones alcanzado.")
    
    return x_sig, iteraciones



# Ejemplo de uso:
import math
import sympy as sp


print("\n\n\tMétodo de newton-raphson para encontrar una raíz de la función f2 en el intervalo [0, 1], toleracion = {}.\n\n".format(0.001))

# Definir la variable simbólica
x = sp.symbols('x')

# Definir la función simbólica como f_sym
f_sym = -1 - sp.cos(x) + sp.exp(-x) + (1/2) * x

# Convertir la función simbólica a una función numérica
f = sp.lambdify(x, f_sym)

raiz, iteraciones = secante(f, 1, 4, 0.001)

if raiz is not None:
    print(f"\nRaíz encontrada: {raiz}")
    print(f"Número de iteraciones: {iteraciones}")
else:
    print("No se encontró una raíz en el intervalo dado.")