import csv
from ast import literal_eval

# to call this file, use : py analisador_sintatico.py


file_path = 'tabela_sintatica.csv'

# Ler a tabela do arquivo CSV
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    tabela = [row for row in csv_reader]

# Converter os elementos da tabela de volta para a estrutura desejada
for i, row in enumerate(tabela):
    for j, cell in enumerate(row):
        try:
            tabela[i][j] = literal_eval(cell)
        except (ValueError, SyntaxError):
            pass

terminais = ['def', 'ident', 'int', 'float', 'string', 'int_constant', 'float_constant', 'string_constant', 'break', 'print', 'read', 'return', 'if', 'else', 'for', 'new', 'null', '(', ')', '{', '}', ';', '=', '<', '>', '<=', '>=', '==', '!=', '[', ']', '*', '+', '-', '/', '%', ',', '$']

file_path_tokens = 'lista_tokens.csv'

# Ler a lista de tokens do arquivo CSV
with open(file_path_tokens, 'r') as file:
    lista = [line.strip() for line in file]

lista.append('$')

pilha = ['$', 'PROGRAM']

pointer = 0

variavel = pilha[-1]

while variavel != '$':
    simbolo = lista[pointer]

    # Se o topo da pilha for igual a entrada desempilha e consome a entrada
    if variavel == simbolo:
        pilha.pop()
        pointer += 1
        variavel = pilha[-1]
    
    # Se o topo da pilha for igual EPSILON desempilha
    elif variavel == 'EPSILON':
        pilha.pop()
        variavel = pilha[-1]

    # Se o topo da pilha é terminal e não corresponde a entrada aponta erro
    elif variavel in terminais:
        raise Exception(f'O simbolo encontrado na entrada é {simbolo} porém, a variavel no topo da pilha é {variavel} logo, não existe {variavel} -+> (uma ou mais transições) {simbolo}') 
    
    # Encontra na tabela a produção correspondente para a entrada a partir do topo da pilha
    else:
        coluna = tabela[0].index(simbolo)
        linha = 0
        for linhas in tabela:
            if linhas[0] == variavel:
                linha = tabela.index(linhas)
                break

        # Se não houver produção para essa combinação de topo da pilha e entrada aponta erro
        if tabela[linha][coluna] == []:
            raise Exception(f'O simbolo encontrado na entrada é {simbolo} porém, a variavel no topo da pilha é {variavel} logo, não existe {variavel} -+> (uma ou mais transições) {simbolo}') 
        
        # Exibe a produção, desempilha a cabeça e empilha a cauda da produção
        else:
            aux = tabela[linha][coluna].copy()
            print(variavel, ' -> ', ' '.join(aux))
            pilha.pop()
            aux.reverse()
            pilha += aux
            variavel = pilha[-1]

# Se não der Erros então Sucesso!
print('Sucesso!')

