def newton_raphson(f, df, x0, tol=1e-6, max_iter=1000):
    """
    Método de Newton-Raphson para encontrar una raíz de la función f en el punto x0.
    Parámetros:
    - f: función para la cual se busca una raíz
    - df: derivada de la función f
    - x0: punto en el que se busca la raíz
    - tol: tolerancia deseada para la solución
    - max_iter: número maximo de iteraciones permitidas
    """
    x = x0
    x_prev = x0*2  # Inicializar x_prev en un valor mayor que e
    iteraciones = 0
    print("  i                    xi                              |f(xi)|                                       |xi - xi-1|")
    print("----------------------------------------------------------------------------------------------------------------------")

    while (abs(f(x)) > tol) or (abs(x - x_prev) > tol) and  iteraciones < max_iter:
        if iteraciones:
            print("  {i:.14f}     {xi:.14f}                 {f:.14f}                              {dif:.14f}".format(i = iteraciones, xi = float(x), f = float(abs(f(x))), dif = abs(float(x - x_prev))))
        else:
            print("  {i:.14f}     {xi:.14f}                 {f:.14f}                              {dif}".format(i = iteraciones, xi = float(x), f = float(abs(f(x))), dif = "-"))
            
        x_prev = x  # Guarda el valor anterior de x
        x = x_prev - f(x_prev)/df(x_prev)
        iteraciones += 1
    print("  {i:.14f}     {xi:.14f}                 {f:.14f}                              {dif:.14f}".format(i = iteraciones, xi = float(x), f = float(abs(f(x))), dif = abs(float(x - x_prev))))
    
    if iteraciones == max_iter:
        print("Máximo nàmero de iteraciones alcanzado.")
    
    return x, iteraciones

# Ejemplo de uso:
import math
import sympy as sp


print("\n\n\tMétodo de newton-raphson para encontrar una raíz de la función f2 en el intervalo [0, 1], toleracion = {}.\n\n".format(0.001))

# Definir la variable simbólica
x = sp.symbols('x')

# Definir la función simbólica como f_sym
f_sym = -1 - sp.cos(x) + sp.exp(-x) + (1/2) * x

# Calcular la derivada
df_sym = sp.diff(f_sym, x)

# Convertir la función simbólica a una función numérica
f = sp.lambdify(x, f_sym)
df = sp.lambdify(x, df_sym)

raiz, iteraciones = newton_raphson(f, df, 1, 0.001)

if raiz is not None:
    print(f"\nRaíz encontrada: {raiz}")
    print(f"Número de iteraciones: {iteraciones}")
else:
    print("No se encontró una raíz en el intervalo dado.")