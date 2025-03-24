class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
    
meu_retangulo = Retangulo(5, 3)
area = meu_retangulo.calcular_area()
print(f"Área do retângulo: {area}")