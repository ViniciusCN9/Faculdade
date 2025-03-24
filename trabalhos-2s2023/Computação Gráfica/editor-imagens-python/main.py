import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageTk

class EditorSimplesDeImagem:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Titulo')
        self.janela.geometry('900x600')

        self.criar_menu()

        self.area_desenho = tk.Canvas(self.janela, bg='white')
        self.area_desenho.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        self.area_desenho.bind('<B1-Motion>', self.desenhar)
        self.area_desenho.bind('<Button-1>', self.desenhar)

        self.imagem = Image.new('RGB', (900, 600), 'white')
        self.desenho = ImageDraw.Draw(self.imagem)

        self.imagem_tk = ImageTk.PhotoImage(self.imagem)
        self.id_imagem = self.area_desenho.create_image(0, 0, anchor=tk.NW, image=self.imagem_tk)

        self.modificado = False

    def criar_menu(self):
        self.menu = tk.Menu(self.janela)
        self.janela.config(menu=self.menu)

        menu_arquivo = tk.Menu(self.janela)
        self.menu.add_cascade(label='Arquivo', menu=menu_arquivo)
        menu_arquivo.add_command(label='Novo', command=self.novo_arquivo)
        menu_arquivo.add_command(label='Abrir', command=self.abrir_arquivo)
        menu_arquivo.add_command(label='Salvar', command=self.salvar_arquivo)

    def desenhar(self, evento):
        x, y = evento.x, evento.y
        raio = 2
        self.desenho.ellipse([x-raio, y-raio, x+raio, y+raio], fill='black')
        self.atualizar_area_desenho()
        self.modificado = True

    def atualizar_area_desenho(self):
        self.imagem_tk = ImageTk.PhotoImage(self.imagem)
        self.area_desenho.itemconfig(self.id_imagem, image=self.imagem_tk)

    def novo_arquivo(self):
        if self.modificado and messagebox.askyesno("Salvar?", "Deseja salvar?"):
            self.salvar_arquivo()
        self.imagem = Image.new('RGB', (900, 600), 'white')
        self.desenho = ImageDraw.Draw(self.imagem)
        self.atualizar_area_desenho()
        self.modificado = False

    def abrir_arquivo(self):
        caminho_arquivo = filedialog.askopenfilename(filetypes=[('PNG Files', '*.png')])
        if caminho_arquivo:
            self.imagem = Image.open(caminho_arquivo)
            self.desenho = ImageDraw.Draw(self.imagem)
            self.atualizar_area_desenho()

    def salvar_arquivo(self):
        caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[('PNG Files', '*.png')])
        if caminho_arquivo:
            self.imagem.save(caminho_arquivo)
            self.modificado = False

if __name__ == "__main__":
    janela = tk.Tk()
    janela.resizable(False, False)
    app = EditorSimplesDeImagem(janela)
    janela.mainloop()