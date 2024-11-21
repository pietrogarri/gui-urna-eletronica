# GUI de Urna Eletrônica
Aluno: Pietro Motta Garri

Este projeto implementa um sistema de urna eletrônica para gerenciar e registrar informações relacionadas a eleitores e candidatos em um processo de votação. Ele combina a interface gráfica com funcionalidades de gerenciamento de dados, utilizando persistência em arquivos para armazenar e recuperar informações.

Funcionalidades Principais:

    Cadastro e Gerenciamento de Eleitores:
        Adição de eleitores com informações como nome, RG, CPF, título, seção e zona eleitoral.
        Atualização de dados existentes (seção e zona).
        Persistência dos dados em arquivo usando a biblioteca pickle.

    Cadastro e Gerenciamento de Candidatos:
        Adição de candidatos com informações como nome, RG, CPF e número eleitoral.
        Listagem dos candidatos registrados.

    Simulação de Votação:
        Integração com uma interface gráfica (Urna_App) para testar a funcionalidade da urna eletrônica, como simulação de votação e exibição de candidatos.

    Persistência de Dados:
        Eleitores e candidatos são armazenados em arquivos separados (eleitores.pkl e candidatos.pkl), garantindo que os dados sejam preservados entre execuções.

    Interface Gráfica:
        Uso de classes para criar telas interativas que exibem informações e recebem inputs do usuário durante o processo de votação.

    Menu Principal:
        Oferece opções para gerenciar eleitores, candidatos e acessar o modo de simulação da urna.
