#1 - Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo.
#    Inicie o atributo ativo como False por padrão.

class ContaBancaria():
    contas_bancarias = []
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contas_bancarias.append(self)

#2 - Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self):
        return f'{self._titular} | {self._saldo} | {self._ativo}'
#3 - Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    @classmethod
    def ativar_conta(cls):
        for conta in cls.contas_bancarias:
            conta._ativo = not conta._ativo
    
    @property
    def titular(self):
        return self._titular

conta1 = ContaBancaria('Jordan', 1000000)
conta1.ativar_conta()

print(conta1)
#4 - Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

#5 - Crie uma instância da classe e imprima o valor da propriedade titular.
conta2 = ContaBancaria('Lara', 1000000)
print(conta2._titular)

#6 - Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBanco():
    clientes = []
    
    def __init__(self, nome, agencia, conta, cidade, abertura):
        self._nome = nome
        self._agencia = agencia
        self._conta = conta
        self._cidade = cidade
        self._abertura = abertura
        ClienteBanco.clientes.append(self)

    @classmethod
    def saudacao(cls):
        for cliente in cls.clientes:
            print('Olá', cliente._nome, 'seja bem vindo')


cliente1 = ClienteBanco('Jose', '2222', '21542', 'Londrina', '20/04/2024')
cliente2 = ClienteBanco('Maria', '2222', '32421', 'Londrina', '30/03/2023')
cliente3 = ClienteBanco('Joao', '2222', '54523', 'Londrina', '01/01/2022')

#7 - Crie um método de classe para a conta ClienteBanco.
ClienteBanco.saudacao()


    