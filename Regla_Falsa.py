import numpy as np
import matplotlib.pyplot as plt


#Func Principal
def falsa_posicion(f, a, b, tolerancia=1e-9, max_iter=1000):

    if f(a) * f(b) >= 0:
        print("El intervalo no cumple el criterio de Bolzano.")
        return None

    for i in range(max_iter):

        if f(b) - f(a) == 0:
            print("División entre cero detectada.")
            return None

        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        error = abs(f(c))

        print(f"Iteración {i+1}: c = {c:.10f}, f(c) = {f(c):.3e}")

        if error < tolerancia:
            print("\nRaíz aproximada encontrada.")
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("\nSe alcanzó el número máximo  de iteraciones.")
    return c

#Grafica
def grafica(f, a, b, raiz=None):

    x_vals = np.linspace(a, b, 400)
    y_vals = [f(x) for x in x_vals]

    plt.figure()
    plt.axhline(0)
    plt.plot(x_vals, y_vals, label="f(x)")

    if raiz is not None:
        plt.scatter(raiz, f(raiz), s=80, color='red', zorder=5)
        plt.annotate(
            f"{raiz:.6f}",
            (raiz, f(raiz)),
            textcoords="offset points",
            xytext=(10,10),
            ha='left'
        )

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Método de Falsa Posición")
    plt.legend()
    plt.grid()
    plt.show()

#Revisar Func
def c_func(funcion_str):
    try:
        def f(x):
            return eval(funcion_str, {"__builtins__": None}, {"x": x, "np": np})
        f(1)  
        return f
    except Exception:
        return None

#Validar int
def vint(f, a, b):
    if a >= b:
        print("El valor de 'a' debe ser menor que 'b'.")
        return False
    if f(a) * f(b) >= 0:
        print("El intervalo no cumple el criterio de Bolzano.")
        return False
    return True

#metodo
def metodo():

    print("\nInstrucciones:")
    print("Ingresar funciones con la figura ejemplo: x**2 + 2*x - 100")
    print("En caso de no ingresar polinomios, utilizar la biblioteca numpy (ejemplo: np.sin(x), np.cos(x))\n")
    print("----------------------------------------------------------------------")
    
    funcion_str = input("Introduce la función en términos de x: ")

    f = c_func(funcion_str)

    if f is None:
        print("Error en la función. Revisa la sintaxis.")
        return

    try:
        a = float(input("Introduce el valor de a: "))
        b = float(input("Introduce el valor de b: "))
        tolerancia = float(input("Introduce la tolerancia (ej: 1e-9): "))
        max_iter = int(input("Introduce el número máximo de iteraciones: "))
    except ValueError:
        print("Debes ingresar valores numéricos válidos.")
        return

    if not vint(f, a, b):
        return

    raiz = falsa_posicion(f, a, b, tolerancia, max_iter,)

    print("\nRaíz aproximada:", raiz)

    if raiz is not None:
        while True:
            print("\n1) Graficar")
            print("2) Regresar al menú principal")

            subopcion = input("Selecciona una opción: ")

            if subopcion == "1":
                grafica(f, a, b, raiz)
                print("\n *Grafica generada exitosamente.*")
                
            elif subopcion == "2":
                break
            else:
                print("Opción inválida.")

#ponme 10 Carlos, tuve que aprender a hacer una funcion d menu :D 

def menu():

    while True:

        print("\n-----------MÉTODO DE FALSA POSICIÓN -------------")
        print("1) Ejecutar método")
        print("2) Salir")
        print("---------------------------------------------------")

        opcion = input("\n Selecciona una opción: ")

        if opcion == "1":
            metodo()
        elif opcion == "2":
            print("...")
            break
        else:
            print("Opción inválida.")

def main():
    menu()
if __name__ == "__main__":
    main()