import csv

lista_de_palavras_reservadas = {'def', 'int', 'float', 'string', 'break', 'print', 'read', 'return', 'if', 'else', 'for', 'new', 'null'}

lista_de_simbolos = {'(', ')', '{', '}', ';', '<', '>', '=', '!', '[', ']', '*', '+', '-', '/', '%', ','}

lista_de_terminais = ['id', '+', '*', '(', ')', '$']

gramatica = [['E', [["T", "E'"]]],
             ["E'", [["+", "T", "E'"], ['EPSILON']]],
             ['T', [["F", "T'"]]],
             ["T'", [["*", "F", "T'"], ['EPSILON']]],
             ['F', [["(", "E", ")"], ['id']]]
            ]

lista_firsts = [[['EPSILON'], ['EPSILON']],
                [["T", "E'"], ['(', 'id']], 
                [["+", "T", "E'"], ['+']], 
                [["F", "T'"], ['(', 'id']], 
                [["*", "F", "T'"], ['*']],
                [["(", "E", ")"], ['(']],
                [['id'], ['id']]]

lista_follows = [['E', ["$", ")"]],
                 ["E'", ["$", ")"]],
                 ['T', ["+", "$", ")"]],
                 ["T'", ["+", "$", ")"]],
                 ['F', ["*", "+", "$", ")"]]
                ]

tabela_sintatica = [['',    'id',   '+',    '*',    '(',    ')',    '$'],
                    ['E',   [],     [],     [],     [],     [],     [],],
                    ["E'",  [],     [],     [],     [],     [],     [],],
                    ['T',   [],     [],     [],     [],     [],     [],],
                    ["T'",  [],     [],     [],     [],     [],     [],],
                    ['F',   [],     [],     [],     [],     [],     [],]
                   ]

for producoes in gramatica:
    for producao in producoes[1]:

        # Obtem a linha da tabela sintatica para a variavel a esquerda da produção
        linha = 0
        for linhas in tabela_sintatica:
            if linhas[0] == producoes[0]:
                linha = tabela_sintatica.index(linhas)
                break

        # Obtem os simbolos de Firts da produção
        simbolos = []
        for firsts in lista_firsts:
            if (producao == firsts[0]):
                simbolos = firsts[1]
                break

        # Obtem as colunas e insere as produções na tabela
        coluna = 0
        for simbolo in simbolos:
            if simbolo != 'EPSILON':
                coluna = tabela_sintatica[0].index(simbolo)
                tabela_sintatica[linha][coluna] = producao
            else:
                # Em caso de epsilon Obtem a lista de Follows da variavel
                simbolos_follow = []
                for follows in lista_follows:
                    if producoes[0] == follows[0]:
                        simbolos_follow = follows[1]
                        break
                # Obtem a coluna dos simbolos follow e insere a produção na tabela
                for simbolo_follow in simbolos_follow:
                    coluna = tabela_sintatica[0].index(simbolo_follow)
                    tabela_sintatica[linha][coluna] = producao

        
for linhas in tabela_sintatica:
    print(linhas)
    print()

file_path = 'tabela_sintatica.csv'

with open(file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(tabela_sintatica)

print(f"Matriz salva em {file_path}")