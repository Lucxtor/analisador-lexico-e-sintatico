import csv

# P2 Compiladores (INE5622) 2023.2 
# Grupo - Thundercats - Alunos:
# Bruno Garbatzki Madeira Cunha (19202601)
# Luis Felipe Fabiane (21106213)
# Lívia Silva Marques (18200638)

# to call this file, use : py monta_tabela.py

gramatica = [
    ["PROGRAM", [["STATEMENT"], ["FUNCLIST"], ["EPSILON"]]],
    ["FUNCLIST", [["FUNCDEF", "FUNCLIST2"]]],
    ["FUNCLIST2", [["EPSILON"], ["FUNCLIST"]]],
    ["FUNCDEF", [["def", "ident", "(", "PARAMLIST", ")", "{", "STATELIST", "}"]]],
    ["PARAMLIST", [["int", "ident", "PARAMLIST2"], ["float", "ident", "PARAMLIST2"], ["string", "ident", "PARAMLIST2"], ["EPSILON"]]],
    ["PARAMLIST2", [[",", "PARAMLIST"], ["EPSILON"]]],
    ["STATEMENT", [["VARDECL", ";"], ["ATRIBSTAT", ";"], ["PRINTSTAT", ";"], ["READSTAT", ";"], ["RETURNSTAT", ";"], ["IFSTAT"], ["FORSTAT"], ["{", "STATELIST", "}"], ["break", ";"], [";"]]],
    ["VARDECL", [["int", "ident", "VARDECL'"], ["float", "ident", "VARDECL'"], ["string", "ident", "VARDECL'"]]],
    ["VARDECL'", [["EPSILON"], ["[", "int_constant", "]", "VARDECL'"]]],
    ["ATRIBSTAT", [["LVALUE", "=", "ATRIBSTAT2"]]],
    ["ATRIBSTAT2", [["EXPRESSION"], ["NEW"], ["FUNCCALL"]]],
    ["FUNCCALL", [["call", "ident", "(", "PARAMLISTCALL", ")"]]],
    ["PARAMLISTCALL", [["ident", "PARAMLISTCALL2"], ["EPSILON"]]],
    ["PARAMLISTCALL2", [[",", "PARAMLISTCALL"], ["EPSILON"]]],
    ["PRINTSTAT", [["print", "EXPRESSION"]]],
    ["READSTAT", [["read", "LVALUE"]]],
    ["RETURNSTAT", [["return"]]],
    ["IFSTAT", [["if", "(", "EXPRESSION", ")", "{", "STATEMENT", "}", "IFSTAT2"]]],
    ["IFSTAT2", [["else", "STATEMENT"], ["EPSILON"]]],
    ["FORSTAT", [["for", "(", "ATRIBSTAT", ";", "EXPRESSION", ";", "ATRIBSTAT", ")", "STATEMENT"]]],
    ["STATELIST", [["STATEMENT", "STATELIST2"]]],
    ["STATELIST2", [["STATELIST"], ["EPSILON"]]],
    ["NEW", [["new", "ALLOCEXPRESSION"]]],
    ["ALLOCEXPRESSION", [["int", "ALLOCEXPRESSION2"], ["float", "ALLOCEXPRESSION2"], ["string", "ALLOCEXPRESSION2"]]],
    ["ALLOCEXPRESSION2", [["[", "NUMEXPRESSION", "]", "ALLOCEXPRESSION3"]]],
    ["ALLOCEXPRESSION3", [["ALLOCEXPRESSION2"], ["EPSILON"]]],
    ["EXPRESSION", [["NUMEXPRESSION", "EXPRESSION'"]]],
    ["EXPRESSION'", [["<", "NUMEXPRESSION"], [">", "NUMEXPRESSION"], ["<=", "NUMEXPRESSION"], [">=", "NUMEXPRESSION"], ["==", "NUMEXPRESSION"], ["!=", "NUMEXPRESSION"], ["EPSILON"]]],
    ["NUMEXPRESSION", [["TERM", "NUMEXPRESSION'"]]],
    ["NUMEXPRESSION'", [["+", "TERM", "NUMEXPRESSION'"], ["-", "TERM", "NUMEXPRESSION'"], ["EPSILON"]]],
    ["TERM", [["UNARYEXPR", "TERM'"]]],
    ["TERM'", [["*", "UNARYEXPR", "TERM'"], ["/", "UNARYEXPR", "TERM'"], ["%", "UNARYEXPR", "TERM'"], ["EPSILON"]]],
    ["UNARYEXPR", [["+", "FACTOR"], ["-", "FACTOR"], ["FACTOR"]]],
    ["FACTOR", [["int_constant"], ["float_constant"], ["string_constant"], ["null"], ["LVALUE"], ["(", "NUMEXPRESSION", ")"]]],
    ["LVALUE", [["ident", "LVALUE'"]]],
    ["LVALUE'", [["[", "NUMEXPRESSION", "]", "LVALUE'"], ["EPSILON"]]],
]

lista_firsts = [
    [['STATEMENT'], ['{', 'break', ';', 'int', 'float', 'string', 'print', 'return', 'for', 'ident', 'if', 'read']],
    [['FUNCLIST'], ['def']],
    [['EPSILON'], ['EPSILON']],
    [['FUNCDEF', "FUNCLIST2"], ['def']],
    [['def', 'ident', '(', 'PARAMLIST', ')', '{', 'STATELIST', '}'], ['def']],
    [['int', 'ident', "PARAMLIST2"], ['int']],
    [['float', 'ident', "PARAMLIST2"], ['float']],
    [['string', 'ident', "PARAMLIST2"], ['string']],
    [[',', 'PARAMLIST'], [',']],
    [['VARDECL', ';'], ['int', 'float', 'string']],
    [['ATRIBSTAT', ';'], ['ident']],
    [['PRINTSTAT', ';'], ['print']],
    [['READSTAT', ';'], ['read']],
    [['RETURNSTAT', ';'], ['return']],
    [['IFSTAT'], ['if']],
    [['FORSTAT'], ['for']],
    [['{', 'STATELIST', '}'], ['{']],
    [['break', ';'], ['break']],
    [[';'], [';']],
    [['int', 'ident', 'VARDECL\''], ['int']],
    [['float', 'ident', 'VARDECL\''], ['float']],
    [['string', 'ident', 'VARDECL\''], ['string']],
    [['[', 'int_constant', ']', 'VARDECL\''], ['[']],
    [['LVALUE', '=', "ATRIBSTAT2"], ['ident']],
    [['EXPRESSION'], ['+', '-', 'int_constant', 'float_constant', 'string_constant', 'null', '(', 'ident']],
    [['NEW'], ['new']],
    [['new', 'ALLOCEXPRESSION'], ['new']],
    [['FUNCCALL'], ['call']],
    [['call', 'ident', '(', 'PARAMLISTCALL', ')'], ['call']],
    [['ident', "PARAMLISTCALL2"], ['ident']],
    [[',', 'PARAMLISTCALL'], [',']],
    [['print', 'EXPRESSION'], ['print']],
    [['read', 'LVALUE'], ['read']],
    [['return'], ['return']],
    [['if', '(', 'EXPRESSION', ')', '{', 'STATEMENT', '}', "IFSTAT2"], ['if']],
    [['else', 'STATEMENT'], ['else']],
    [['for', '(', 'ATRIBSTAT', ';', 'EXPRESSION', ';', 'ATRIBSTAT', ')', 'STATEMENT'], ['for']],
    [['STATEMENT', "STATELIST2"], ['{', 'break', ';', 'int', 'float', 'string', 'print', 'return', 'for', 'ident', 'if', 'read']],
    [['STATELIST'], ['{', 'break', ';', 'int', 'float', 'string', 'print', 'return', 'for', 'ident', 'if', 'read']],
    [['int', 'ALLOCEXPRESSION\''], ['int']],
    [['float', 'ALLOCEXPRESSION\''], ['float']],
    [['string', 'ALLOCEXPRESSION\''], ['string']],
    [['[', 'NUMEXPRESSION', ']', "ALLOCEXPRESSION3"], ['[']],
    [["ALLOCEXPRESSION2"], ['[']],
    [['NUMEXPRESSION', "EXPRESSION'"], ['+', '-', 'int_constant', 'float_constant', 'string_constant', 'null', '(', 'ident']],
    [['<', 'NUMEXPRESSION'], ['<']],
    [['>', 'NUMEXPRESSION'], ['>']],
    [['<=', 'NUMEXPRESSION'], ['<=']],
    [['>=', 'NUMEXPRESSION'], ['>=']],
    [['==', 'NUMEXPRESSION'], ['==']],
    [['!=', 'NUMEXPRESSION'], ['!=']],
    [['TERM', "NUMEXPRESSION'"], ['+', '-', 'int_constant', 'float_constant', 'string_constant', 'null', '(', 'ident']],
    [['+', 'TERM', "NUMEXPRESSION'"], ['+']],
    [['-', 'TERM', "NUMEXPRESSION'"], ['-']],
    [['UNARYEXPR', 'TERM\''], ['+', '-', 'int_constant', 'float_constant', 'string_constant', 'null', '(', 'ident']],
    [['*', 'UNARYEXPR', 'TERM\''], ['*']],
    [['/', 'UNARYEXPR', 'TERM\''], ['/']],
    [['%', 'UNARYEXPR', 'TERM\''], ['%']],
    [['+', 'FACTOR'], ['+']],
    [['-', 'FACTOR'], ['-']],
    [['FACTOR'], ['int_constant', 'float_constant', 'string_constant', 'null', 'ident', '(']],
    [['int_constant'], ['int_constant']],
    [['float_constant'], ['float_constant']],
    [['string_constant'], ['string_constant']],
    [['null'], ['null']],
    [['LVALUE'], ['ident']],
    [['(', 'NUMEXPRESSION', ')'], ['(']],
    [['ident', "LVALUE'"], ['ident']],
    [['[', 'NUMEXPRESSION', ']', "LVALUE'"], ['[']],
]


lista_follows = [
    ["PROGRAM", ['$']],
    ["FUNCLIST", ['$']],
    ["FUNCLIST2", ['$', '{']],
    ["FUNCDEF", ['def', '$']],
    ["PARAMLIST", [')']],
    ["PARAMLIST2", [')']],
    ["STATEMENT", ['{', 'break', ';', 'int', 'float', 'string', 'print', 'return', 'for', 'ident', 'if', 'read', 'else', '}', '$']],
    ["VARDECL", [';']],
    ["VARDECL'", [';']],
    ["ATRIBSTAT", [';', ')']],
    ["ATRIBSTAT2", [';', ')']],
    ["FUNCCALL", [';', ')']],
    ["PARAMLISTCALL", [')']],
    ["PARAMLISTCALL2", [')']],
    ["PRINTSTAT", [';']],
    ["READSTAT", [';']],
    ["RETURNSTAT", [';']],
    ["IFSTAT", ['{', 'break', ';', 'int', 'float', 'string', 'print', 'return', 'for', 'ident', 'if', 'read', '}', '$']],
    ["IFSTAT2", ['{', 'break', ';', 'int', 'float', 'string', 'print', 'return', 'for', 'ident', 'if', 'read', '}', '$']],
    ["FORSTAT", ['{', 'break', ';', 'int', 'float', 'string', 'print', 'return', 'for', 'ident', 'if', 'read', '}', '$']],
    ["STATELIST", ['}']],
    ["STATELIST2", ['}']],
    ["NEW", [';', ')']],
    ["ALLOCEXPRESSION", [';', ')']],
    ["ALLOCEXPRESSION2", [';', ')']],
    ["ALLOCEXPRESSION3", [';', ')']],
    ["EXPRESSION", [';', ')']],
    ["EXPRESSION'", [';', ')']],
    ["NUMEXPRESSION", [']', ')', ';', '<', '>', '<=', '>=', '==', '!=']],
    ["NUMEXPRESSION'", [']', ')', ';', '<', '>', '<=', '>=', '==', '!=']],
    ["TERM", ['+', '-', ']', ')', ';', '<', '>', '<=', '>=', '==', '!=']],
    ["TERM'", ['+', '-', ']', ')', ';', '<', '>', '<=', '>=', '==', '!=']],
    ["UNARYEXPR", ['*', '/', '%', '+', '-', ']', ')', ';', '<', '>', '<=', '>=', '==', '!=']],
    ["FACTOR", ['*', '/', '%', '+', '-', ']', ')', ';', '<', '>', '<=', '>=', '==', '!=']],
    ["LVALUE", ['=', '*', '/', '%', '+', '-', ']', ')', ';', '<', '>', '<=', '>=', '==', '!=']],
    ["LVALUE'", ['=', '*', '/', '%', '+', '-', ']', ')', ';', '<', '>', '<=', '>=', '==', '!=']],
]

# gramatica = [['E', [["T", "E'"]]],
#              ["E'", [["+", "T", "E'"], ['EPSILON']]],
#              ['T', [["F", "T'"]]],
#              ["T'", [["*", "F", "T'"], ['EPSILON']]],
#              ['F', [["(", "E", ")"], ['id']]]
#             ]

# lista_firsts = [[['EPSILON'], ['EPSILON']],
#                 [["T", "E'"], ['(', 'id']], 
#                 [["+", "T", "E'"], ['+']], 
#                 [["F", "T'"], ['(', 'id']], 
#                 [["*", "F", "T'"], ['*']],
#                 [["(", "E", ")"], ['(']],
#                 [['id'], ['id']]]

# lista_follows = [['E', ["$", ")"]],
#                  ["E'", ["$", ")"]],
#                  ['T', ["+", "$", ")"]],
#                  ["T'", ["+", "$", ")"]],
#                  ['F', ["*", "+", "$", ")"]]
#                 ]


# Monta a tabela sintatica vazia apenas com os tokens finais e não finais
tabela_sintatica = [['', 'def', 'ident', 'call', 'int', 'float', 'string', 'int_constant', 'float_constant', 'string_constant', 'break', 'print', 'read', 'return', 'if', 'else', 'for', 'new', 'null', '(', ')', '{', '}', ';', '=', '<', '>', '<=', '>=', '==', '!=', '[', ']', '*', '+', '-', '/', '%', ',', '$']]
linha_tabela = [[] for _ in range(len(tabela_sintatica[0]))]

for var in gramatica:
    linha_tabela[0] = var[0]
    tabela_sintatica.append(linha_tabela.copy())
    

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
                if(tabela_sintatica[linha][coluna] != []):
                    print(tabela_sintatica[linha][coluna])
                    raise Exception("ambigua")
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
                    if(tabela_sintatica[linha][coluna] != []):
                        print(tabela_sintatica[linha][coluna])
                        raise Exception("ambigua")
                    tabela_sintatica[linha][coluna] = producao

        
for linhas in tabela_sintatica:
    print(linhas)
    print()

file_path = 'tabela_sintatica.csv'

with open(file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(tabela_sintatica)

print(f"Matriz salva em {file_path}")