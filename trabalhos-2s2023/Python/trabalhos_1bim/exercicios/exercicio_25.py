class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")

livro1 = Livro("Dom Quixote", "Miguel de Cervantes")
livro2 = Livro("A Morenzinha", "Joaquim Manuel do Macedo")

livro1.mostrar_informacoes()
print()
livro2.mostrar_informacoes()