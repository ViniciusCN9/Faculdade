class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
meu_carro = Carro("Ford", "Fiesta")
print(f"Marca: {meu_carro.marca}, Modelo: {meu_carro.modelo}")