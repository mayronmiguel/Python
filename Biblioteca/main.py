# 8. Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.

from livros import Livro

livro5 = Livro('titulo5', 'autor5', 2023)
livro6 = Livro('titulo6', 'autor6', 2024)

print(livro5)
print(livro6)
