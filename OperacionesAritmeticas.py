class OperacionesAritmeticas():

    def ingresoNumeros(self):
        numero01 = float(input("Ingrese sumando uno: "))
        numero02 = float(input("Ingrese sumando dos: "))
        return numero01, numero02

    def suma(self, numero01, numero02):
        return numero01 + numero02

