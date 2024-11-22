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
        Durante o cadastro, os números de títulos de eleitores e os números eleitorais dos candidatos registrados são organizados em listas no seguinte formato:
            
            Eleitores:
                Nome: Geralt of Rivia | RG: 293476135 | CPF: 15669112814
                Título: 1371 | Seção: 25 | Zona: 15
                
                Nome: Johnny Silverhand | RG: 234685517 | CPF: 96991827843
                Título: 7734 | Seção: 25 | Zona: 15
                
                Nome: Demetrian Titus | RG: 507079097 | CPF: 32426914823
                Título: 36540 | Seção: 25 | Zona: 15
                
                Nome: Vincent | RG: 480085213 | CPF: 56128033890
                Título: 2377 | Seção: 25 | Zona: 15
                
                Nome: Ciri of Cintra | RG: 713824935 | CPF: 50934480277
                Título: 53568 | Seção: 25 | Zona: 15
                
                Nome: Viktor Vektor | RG: 340833100 | CPF: 86356417212
                Título: 76604 | Seção: 25 | Zona: 15
                
                Nome: Jackie Welles | RG: 317045267 | CPF: 40092013940
                Título: 76985 | Seção: 25 | Zona: 15
                
                Mome: Roboute Guilliman | RG: 334862005 | CPF: 33092615058
                Título: 50688 | Seção: 25 | Zona: 15
                
                Nome: Abaddon the Despoiler | RG: 602774243 | CPF: 61769897605
                Título: 42909 | Seção: 25 | Zona: 15
                
                Nome: Triss Merigold | RG: 230970655 | CPF: 58101744851
                Título: 5678 | Seção: 25 | Zona: 15

            Candidatos:
                Nome: PHILLIP STRENGER | RG: 227766854 | CPF: 46107238832
                Número Eleitoral: 66
                
                Nome: EMPEROR OF MANKIND | RG: 350402371 | CPF: 82718024887
                Número Eleitoral: 42
                
                Nome: ADAM SMASHER | RG: 346587955 | CPF: 32304664890
                Número Eleitoral: 77
                
                Nome: KHORNE | RG: 192749249 | CPF: 43826577841
                Número Eleitoral: 98
                
                Nome: TZEENTCH | RG: 260327773 | CPF: 37054504844
                Número Eleitoral: 54 
                
                Nome: NURGLE | RG: 319073956 | CPF: 59096095804
                Número Eleitoral: 50
                
                Nome: SLAANESH | RG: 198476085 | CPF: 15631800810
                Número Eleitoral: 24
                
                Nome: HORUS | RG: 403838678 | CPF: 36776209880
                Número Eleitoral: 52

    Interface Gráfica:
        Uso de classes para criar telas interativas que exibem informações e recebem inputs do usuário durante o processo de votação.

    Menu Principal:
        Oferece opções para gerenciar eleitores, candidatos e acessar o modo de simulação da urna.
