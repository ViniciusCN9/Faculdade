class Animal:
    def emitir_som(self):
        print("Som de animal genérico")

class Cachorro(Animal):
    def emitir_som(self):
        print("Latido")

class Gato(Animal):
    def emitir_som(self):
        print("Miado")

animal1 = Animal()
cachorro1 = Cachorro()
gato1 = Gato()

animal1.emitir_som()
cachorro1.emitir_som()
gato1.emitir_som()
