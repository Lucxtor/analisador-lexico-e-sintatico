import sys
import csv

# to call this file, use : py analisador_lexico.py arquivo1.lcc

alfabet = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}


acceptedChars = alfabet.union(numbers)


lista_de_palavras_reservadas = {'def', 'call', 'int', 'float', 'string', 'break', 'print', 'read', 'return', 'if', 'else', 'for', 'new', 'null'}


lista_de_simbolos = {'(', ')', '{', '}', ';', '<', '>', '=', '!', '[', ']', '*', '+', '-', '/', '%', ','}


lista_de_tokens = []


tabela_de_simbolos = []


haveError = False

# Essa função identifica ident, palavras reservadas e contribui para a montagem da lista de tokens e da lista de simbolos
def analisador_ident(charlist, init, linha):
    if (charlist[init] not in alfabet):
        return False, init


    token = charlist[init]


    pointer = init + 1
    while(charlist[pointer] in acceptedChars):
        token += charlist[pointer]
        pointer+=1
    if token in lista_de_palavras_reservadas:
        lista_de_tokens.append(token)
    else:
        lista_de_tokens.append('ident')
        inList = False
        for linhaMatriz in tabela_de_simbolos:
            if token == linhaMatriz[0]:
                inList = True
                linhaMatriz.append(linha)
                break
        if not inList:
            tabela_de_simbolos.append([token, linha])
    end = pointer
    return True, end

# Essa função identifica números inteiro ou de ponto flutuante com apenas 1 (um) . (ponto) 
def analisador_number_constant(charlist, init):
    pointer = init
    if (charlist[pointer] in ['+', '-']):
        pointer += 1

    if (charlist[pointer] not in numbers):
        return False, init

    pointer += 1
    while(charlist[pointer] in numbers ):
        pointer+=1
    if charlist[pointer] == '.':
        pointer+=1
        if charlist[pointer] not in numbers:
            return False, init
        while(charlist[pointer] in numbers ):
            pointer+=1
        lista_de_tokens.append('float_constant')
    else:
        lista_de_tokens.append('int_constant')

    end = pointer
    return True, end

# Essa função identifica string_constants em uma unica linha
def analisador_string_constant(charlist, init):
    if (charlist[init] != '"'):
        return False, init
    
    pointer = init + 1
    while(charlist[pointer] != '"' and charlist[pointer] != '\n'):
        pointer += 1
        
    if charlist[pointer] == '"':
        lista_de_tokens.append('string_constant')
        end = pointer + 1
        return True, end
    return False, init

# Utiliza os analisadores acima para realizar a análise léxica completa do código lido
def analisador(charlist):
    linha = 1
    pointer = 0
    isError = False
    while(1):
        try:
            char = charlist[pointer]
        except:
            return False

        isIdent, pointer = analisador_ident(charlist, pointer, linha)

        if not isIdent:
            isNumber, pointer = analisador_number_constant(charlist, pointer)
            if not isNumber:
                isString, pointer = analisador_string_constant(charlist, pointer)
                if not isString:
                    isSimbol = (charlist[pointer] in lista_de_simbolos)
                    if isSimbol:
                        if charlist[pointer] in ['<', '>', '=', '!']:
                            if charlist[pointer+1] == '=':
                                token = charlist[pointer] + charlist[pointer+1]
                                lista_de_tokens.append(token)
                                pointer += 2
                            else:
                                lista_de_tokens.append(charlist[pointer])
                                pointer += 1    
                        else:
                            lista_de_tokens.append(charlist[pointer])
                            pointer += 1
                    elif charlist[pointer] == ' ':
                        pointer+=1
                    elif char == '\n':
                        linha+=1
                        pointer+=1
                    else:
                        isError = True
        if isError:
            print('Erro Léxico na linha '+ str(linha))
            return True
        
file_path = sys.argv[1]

try:
    with open(file_path, 'r') as file:
            codigo = file.read()
            if codigo:
                haveError = analisador(codigo + " ")

                if not haveError:
                    print()
                    print(lista_de_tokens)
                    print()
                    print(tabela_de_simbolos)
    
    file_path_tokens = 'lista_tokens.csv'
    
    with open(file_path_tokens, 'w') as file:
        for token in lista_de_tokens:
            file.write(token + '\n')
            

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
