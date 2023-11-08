
terminais = []

tabela =   [['', 'id', '+', '*', '(', ')', '$'], 
            ['E', ["T", "E'"], [], [], ["T", "E'"], [], []], 
            ["E'", [], ["+","T","E'"], [], [], ['EPSILON'], ['EPSILON']], 
            ['T', ["F","T'"], [], [], ["F","T'"], [], []], 
            ["T'", [], ['EPSILON'], ["*", "F","T'"],[], ['EPSILON'], ['EPSILON']],
            ['F', ['id'], [], [], ['(', 'E', ')'], [], []]]

lista = ['id', '+', '+', 'id']
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
        raise Exception('erro') 
    else:
        coluna = tabela[0].index(simbolo)
        linha = 0
        for linhas in tabela:
            if linhas[0] == variavel:
                linha = tabela.index(linhas)
                break
        if tabela[linha][coluna] == []:
            raise Exception('erro')
        else:
            aux = tabela[linha][coluna].copy()
            pilha.pop()
            aux.reverse()
            pilha += aux
            variavel = pilha[-1]

print('Sucesso!')



#while lista[len(lista) - 1] != '$':
 #   print(lista[len(lista) - 1])
  #  lista.pop()
    
