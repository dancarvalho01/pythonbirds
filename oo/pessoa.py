class Pessoa:
    def __init__(self,*filhos, nome=None, idade=35):
        self.idade = idade
        self. nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    danilo = Pessoa(nome='Danilo')
    joão = Pessoa(danilo, nome='João')
    print(Pessoa.cumprimentar(joão))
    print(id(joão))
    print(joão.cumprimentar())
    print(joão.nome)
    print(joão.idade)
    for filho in joão.filhos:
        print(filho.nome)
    joão.sobrenome = 'Ramalho'
    del joão.filhos
    print(joão.__dict__)
    print(danilo.__dict__)

