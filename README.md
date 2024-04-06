Descrição:

Este programa permite ao usuário armazenar e manipular informações em três pastas distintas, armazenadas em um banco de dados SQLite. Cada pasta é representada por uma tabela no banco de dados.
Requisitos:

    Python 3.x
    Biblioteca sqlite3 (normalmente já incluída na instalação padrão do Python)

Como Usar:

    Execute o programa em um ambiente Python.
    O programa exibirá um menu com as seguintes opções:
        [1] Visualizar e adicionar dados na Pasta 1
        [2] Visualizar e adicionar dados na Pasta 2
        [3] Visualizar e adicionar dados na Pasta 3
        [4] Apagar dados de uma pasta específica
        [5] Limpar uma pasta específica
        [6] Sair do programa
    Escolha a opção desejada digitando o número correspondente.
    Para inserir dados em uma pasta, selecione a pasta desejada e siga as instruções.
    Para apagar dados de uma pasta, selecione a opção correspondente e siga as instruções para selecionar a pasta e o item a ser removido.
    Para limpar uma pasta, selecione a opção correspondente e escolha a pasta a ser limpa.
    O programa irá armazenar todas as informações em um arquivo chamado "banco_de_dados.txt" ao finalizar a execução.

Observações:

    Certifique-se de não fechar o programa abruptamente, pois isso pode resultar em perda de dados não salvos.
    Todos os dados são armazenados permanentemente no banco de dados SQLite, garantindo a persistência dos dados entre diferentes execuções do programa.
