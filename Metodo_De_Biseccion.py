
#Librerias papoi
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')

#funciones GOD
def c_func(expresion):
    expr = sp.sympify(expresion)
    f = sp.lambdify(x, expr, "math")
    return f
 
def Teorema(f, a, b, tolerancia, max_iter=100):

    if f(a) * f(b) >= 0:
        print("-------------------------RESULTADO-------------------------------")
        print("\n El intervalo dado no cumple el teorema de Bolzano.")
        
        return None, []
    i = 0
    error = float("inf")
    p_m = []   

    while error > tolerancia and i < max_iter:

        pm = (a + b) / 2
        p_m.append(pm)

        error = abs(b - a) / 2

        if f(a) * f(pm) < 0:
            b = pm
        else:
            a = pm

        i += 1
    print("-------------------------RESULTADO-------------------------------")
    print("\nLa raiz tiene un porcentaje de error del:", error*100,"%")    
     
    return pm, p_m

#Graficock
def grafica(f, a, b, raiz=None, puntos_medios=None):

    x_vals = np.linspace(a, b, 400)
    y_vals = [f(x) for x in x_vals]

    plt.figure()
    plt.axhline(0)
    plt.plot(x_vals, y_vals, label="f(x)")

    if raiz is not None:
        plt.scatter(raiz, f(raiz), color='red', s=50, label="Raíz")
        plt.annotate(
            f"{raiz:.4f}",          
            (raiz, f(raiz)),        
            textcoords="offset points",
            color='black',
            xytext=(10,10),         
            ha='left'
        )
    plt.xlabel("x")
    plt.ylabel("F(x)")
    plt.title("Método de Bisección")
    plt.legend()
    plt.grid()
    plt.show()

#----------------------------MENU paputroll 10000xd------------------------------------------

print("-----------------------MENU------------------------")
print("")
expresion = input("Introduce la función en términos de x (ejemplo: x^2 + 3*x - 2): ")
a = float(input("Introduce el punto A: "))
b = float(input("Introduce el punto B: "))
tolerancia = float(input("Introduce un valor de tolerancia: "))

f = c_func(expresion)
raiz, pm = Teorema(f, a, b, tolerancia)
grafica(f, a, b, raiz, pm)

print("\nla raíz aproximada tiene un valor de:", raiz)