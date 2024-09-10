class RaizCuadrada:
    def __init__(self, a):
        self.a = a
        self.x = 1.0

    def calcular_raiz(self, iteraciones):
        for k in range(1, iteraciones + 1):
            self.x = (self.x + self.a / self.x) / 2
            print(f"La raíz después de {k} iteraciones es {self.x:.5f}")


a = float(input("Dame el valor de a: \n"))
iteraciones = int(input("Dame el número de iteraciones: \n"))
mi_raiz = RaizCuadrada(a)
mi_raiz.calcular_raiz(iteraciones)
