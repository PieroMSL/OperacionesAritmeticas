def ingresoNumeros():
    # Solicita al usuario ingresar dos números
    numero01 = float(input("Ingrese sumando uno: "))
    numero02 = float(input("Ingrese sumando dos: "))
    return numero01, numero02

def suma(numero01, numero02):
    # Suma los dos números y retorna el resultado
    return numero01 + numero02

if __name__ == "__main__":
    # Llama a ingresoNumeros para obtener los dos números
    num1, num2 = ingresoNumeros()
    # Imprime el resultado de la suma
    print(f"{num1} + {num2} = {suma(num1, num2)}")
