# 1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = int(ano_publicacao)
        self._disponivel = True
        Livro.livros.append(self)

# 2. Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        return f'{self.titulo} | {self.autor} | {self.ano_publicacao} | {self.disponivel}'
    
# 3. Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    @classmethod
    def listar_livros(cls):
        print(f'{"Título".ljust(25)} | {"Autor".ljust(25)} | {"Ano de publicação".ljust(25)} | {"Disponibilidade"}')
        for livro in cls.livros:
            print(f'{livro.titulo.ljust(25)} | {livro.autor.ljust(25)} | {str(livro.ano_publicacao).ljust(25)} | {livro.disponivel}')

    @property
    def disponivel(self):
        return '☐' if self._disponivel else '☒'

    def emprestar_livro(self):
        self._disponivel = False

# 4. Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        
        for livro in Livro.livros:
            if livro.ano_publicacao == ano and livro._disponivel:
                livros_disponiveis.append(livro)
        
        return livros_disponiveis
    
#imprimindo duas instâncias conforme exercício 2
livro1 = Livro('titulo1', 'autor1', 2024)
livro2 = Livro('titulo2', 'autor2', 2023)
print(livro1)
print(livro2)

#Chamando o metodo emprestar_livro e imprimindo livro para ver se está disponível conforme exercício 4
Livro.emprestar_livro(livro1)
Livro.listar_livros()
