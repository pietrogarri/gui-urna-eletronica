import pickle
from common import *
from urna import UrnaApp

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'

def menu():
    print("1-Novo Eleitor")
    print("2-Atualizar Eleitor")
    print("3-Inserir Candidato")
    print("4-Listar Candidatos")
    print("5-Testar Urna")
    print("6-Sair")
    op = int(input("Digite a opcao [1 a 6]? "))
    while op not in range(1, 7):
        op = int(input("Digite a opcao [1 a 6]? "))
    return op

def inserir_eleitor(eleitores):
    titulo = int(input("Digite o Títlulo: "))

    if titulo in eleitores:
        raise Exception("Titulo já existente!")

    nome = input("Digite o nome: ")
    rg = input("Digite o rg: ")
    cpf = input("Digite o cpf: ")
    secao = int(input("Digite a secao: "))
    zona = int(input("Digite a zona: "))

    eleitor = Eleitor(nome, rg, cpf, titulo, secao, zona)
    eleitores[eleitor.get_titulo()] = eleitor

    with open(FILE_ELEITORES, 'wb') as arquivo:
        pickle.dump(eleitores, arquivo)

    print('Eleitor gravado com sucesso!')
    print(eleitor)

def atualizar_eleitor(eleitores):
    titulo = int(input('Digite o titulo do eleitor: '))

    if titulo in eleitores:
        eleitor = eleitores[titulo]
        print(eleitor)
        secao = int(input("Digite a nova secao: "))
        zona = int(input("Digite a nova zona: "))
        eleitor.secao = secao
        eleitor.zona = zona

        with open(FILE_ELEITORES, 'wb') as arquivo:
            pickle.dump(eleitores, arquivo)

        print('Atualizados dados do eleitor!')
        print(eleitor)
    else:
        raise Exception('Titulo inexistente')

def inserir_candidato(candidatos):
    numero = int(input("Digite o número do candidato: "))

    if numero in candidatos:
        raise Exception("Candidato já existente!")

    nome = input("Digite o nome: ")
    rg = input("Digite o rg: ")
    cpf = input("Digite o cpf: ")

    candidato = Candidato(nome, rg, cpf, numero)
    candidatos[candidato.get_numero()] = candidato

    with open(FILE_CANDIDATOS, 'wb') as arquivo:
        pickle.dump(candidatos, arquivo)

    print('Candidato gravado com sucesso!')
    print(candidato)

def listar_candidatos(candidatos):
    for candidato in candidatos.values():
        print(candidato)

if __name__ == "__main__":
    eleitores = {} # Dicionário a chave será = titulo
    try:
        print("Carregando arquivo de eleitores ...")

        with open(FILE_ELEITORES, 'rb') as arquivo:
            eleitores = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum eleitor carregado!")

    candidatos = {}  # Dicionário a chave será = titulo
    try:
        print("Carregando arquivo de candidatos ...")

        with open(FILE_CANDIDATOS, 'rb') as arquivo:
            candidatos = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum candidato carregado!")

    opcao = 1
    while opcao in range(1,8):
        try:
            opcao = menu()

            if opcao == 1:
                inserir_eleitor(eleitores)
            elif opcao == 2:
                atualizar_eleitor(eleitores)
            elif opcao == 3:
                inserir_candidato(candidatos)
            elif opcao == 4:
                listar_candidatos(candidatos)
            elif opcao == 5:
                app = UrnaApp(eleitores, candidatos)
                app.mainloop()
            elif opcao == 6:
                print("Saindo!")
                break
        except Exception as e:
            print(e)