# 5. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
from livros import Livro

# 6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
livro3 = Livro('titulo3', 'autor3', 2024)
livro4 = Livro('titulo4', 'autor4', 2023)

Livro.emprestar_livro(livro4)

Livro.listar_livros()


# 7) No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
ano_especifico = 2023
livros_disponiveis = Livro.verificar_disponibilidade(ano_especifico)
print(f"\nLivros disponíveis em {ano_especifico}:")
for livro in livros_disponiveis:
    print(livro)
