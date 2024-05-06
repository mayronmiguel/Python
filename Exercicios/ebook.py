class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        self.livros = []
    def __str__(self):
        return f"Livro: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao}"
    
    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis

livro1 = Livro("Aprendendo Python", "John Doe", 2022)
livro2 = Livro("Data Science Fundamentals", "Jane Smith", 2020)

print(livro1)
print(livro2)

livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)
print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")

Livro.livros = [livro1, livro2, livro3]  # Adicionando os livros à lista de livros

resultado = Livro.verificar_disponibilidade(2020)

for livro in resultado:
    print(f"disponiveis: {livro}")
