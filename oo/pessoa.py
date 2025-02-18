class Pessoa:
    olhos = 2
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
    joão.olhos = 1
    del joão.olhos
    print(danilo.__dict__)
    print(joão.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(joão.olhos)
    print(danilo.olhos)
    print(id(Pessoa.olhos), id(joão.olhos), id(danilo.olhos))