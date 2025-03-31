# Cálculo del Factorial de un Número
# Autor: Esteban Lobaton - Jonathan Urueña
# Licencia: MIT License - Este código es libre y puede ser modificado y distribuido.

def factorial(n):
    """
    Calcula el factorial de un número positivo.
    Si n es 0, retorna 1 (por definición: 0! = 1).
    """
    if n < 0:
        raise ValueError("El número debe ser positivo")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

if __name__ == "__main__":
    try:
        num = int(input("Introduce un número positivo: "))
        print("El factorial de", num, "es:", factorial(num))
    except ValueError as e:
        print("Error:", e)
