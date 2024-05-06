class Pessoa:
    def __init__(self, nome='', idade=0, profissão=''): 
       self.nome = nome
       self.idade = idade
       self.profissão = profissão

    def __str__(self):
        return f'{self.nome},{self.idade} anos, {self.profissão}'

    @property
    def saudacao(self):
        if self.profissão:
               return f'Olá, sou {self.nome}! Trabalho como {self.profissão}.'
        else: 
            return f'Olá, sou {self.nome}!'

    def aniversario(self):
        self.idade += 1     

# Criando 3 instâncias da classe Pessoa
pessoa1 = Pessoa(nome='Alice', idade=25, profissão='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissão='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

# Imprimindo informações iniciais
print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.aniversario()
pessoa3.aniversario()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)
