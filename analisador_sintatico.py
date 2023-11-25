import csv
from ast import literal_eval

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

terminais = []

file_path_tokens = 'lista_tokens.csv'

# Ler a lista de tokens do arquivo CSV
with open(file_path_tokens, 'r') as file:
    lista = [line.strip() for line in file]

print(lista)
#lista = ['id', '+', 'id']
#lista = ['def', 'ident', '(', 'int', 'ident', ')', '{', 'int', 'ident', ';', 'ident', '=', 'ident', '+', 'ident', ';', 'return', 'ident', ';', '}']

lista.reverse()

lista.append('$')

pilha = ['$', 'E']

pointer = 0

variavel = pilha[-1]

while variavel != '$':
    simbolo = lista[pointer]

    if variavel == simbolo:
        pilha.pop()
        pointer += 1
        variavel = pilha[-1]
    elif variavel == 'EPSILON':
        pilha.pop()
        variavel = pilha[-1]
    elif variavel in terminais:
        raise Exception(f'O simbolo encontrado na entrada é {simbolo} porém, a variavel no topo da pilha é {variavel} logo, não existe {variavel} =*> (uma ou mais transições) {simbolo}') 
    else:
        coluna = tabela[0].index(simbolo)
        linha = 0
        for linhas in tabela:
            if linhas[0] == variavel:
                linha = tabela.index(linhas)
                break
        if tabela[linha][coluna] == []:
            raise Exception(f'O simbolo encontrado na entrada é {simbolo} porém, a variavel no topo da pilha é {variavel} logo, não existe {variavel} =*> (uma ou mais transições) {simbolo}') 
        else:
            aux = tabela[linha][coluna].copy()
            print(variavel, ' -> ', ''.join(aux))
            pilha.pop()
            aux.reverse()
            pilha += aux
            variavel = pilha[-1]

print('Sucesso!')



#while lista[len(lista) - 1] != '$':
 #   print(lista[len(lista) - 1])
  #  lista.pop()
    
