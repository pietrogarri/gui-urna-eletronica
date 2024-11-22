class Pessoa:
    __nome : str
    __RG : str
    __CPF : str

    def __init__(self, nome, rg, cpf):
        self.__nome = nome
        self.__RG = rg
        self.__CPF = cpf

    def get_nome(self):
        return self.__nome

    def __str__(self):
        info = f'Nome: {self.__nome} | RG: {self.__RG} | CPF: {self.__CPF}\n'
        return info

    def __repr__(self):
        return f"Pessoa(nome='{self.__nome}', RG='{self.__RG}', CPF='{self.__CPF}')"

class Eleitor(Pessoa):
    __titulo : int
    secao : int
    zona : int

    def __init__(self, nome, rg, cpf, titulo, secao, zona):
        super().__init__(nome, rg, cpf)
        self.__titulo = titulo
        self.secao = secao
        self.zona = zona

    def __str__(self):
        info = super().__str__()
        info += f'Titulo: {self.__titulo} | Seção: {self.secao} | Zona: {self.zona}'
        return info

    def __repr__(self):
        return f"Eleitor({super().__repr__()}, titulo='{self.__titulo}', secao='{self.secao}', zona='{self.zona}')"

    def get_titulo(self):
        return self.__titulo

class Candidato(Pessoa):
    __numero : int

    def __init__(self, nome, rg, cpf, numero):
        super().__init__(nome, rg, cpf)
        self.__numero = numero

    def __str__(self):
        info = super().__str__()
        info += f'Numero: {self.__numero}\n'
        return info

    def __repr__(self):
        return f"Candidato({super().__repr__()}, numero='{self.__numero})'"

    def get_numero(self):
        return self.__numero