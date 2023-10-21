alfabet = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
number = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}


acceptedChars = alfabet.union(number)


lista_de_palavras_reservadas = {'def', 'int', 'float', 'string', 'break', 'print', 'read', 'return', 'if', 'else', 'for', 'new', 'null'}


lista_de_simbolos = {'(', ')', '{', '}', ';', '<', '>', '=', '!', '[', ']', '*', '+', '-', '/', '%'}


lista_de_tokens = []


tabela_de_simbolos = []






codigo = '''def func1 ( int A , int B )
{
    int SM [2];
    SM [0] = A + B ;
    SM [1] = B * C ;
    return ;
}


def principal ()
{
    int C ;
    int D ;
    int R ;
    C = 4;
    D = 5;
    R = func1 (C , D );
    return ;
}'''




def analisador_ident(charlist, init, linha):
    if (charlist[init] not in alfabet):
        return False, init


    ident = charlist[init]


    pointer = init + 1
    while(charlist[pointer] in acceptedChars):
        ident += charlist[pointer]
        pointer+=1
    if ident in lista_de_palavras_reservadas:
        lista_de_tokens.append(ident)
    else:
        lista_de_tokens.append('ident')
        inList = False
        for linhaMatriz in tabela_de_simbolos:
            if ident == linhaMatriz[0]:
                inList = True
                linhaMatriz.append(linha)
                break
        if not inList:
            tabela_de_simbolos.append([ident, linha])
    end = pointer
    return True, end








def analisador(charlist):
    linha = 1
    pointer = 0
    while(1):
        try:
            char = charlist[pointer]
        except:
            break




        isIdent, pointer = analisador_ident(charlist, pointer, linha)
        if(isIdent):
            print('IDENT ', end='')
        elif (char == ' ' or char == '\n'):
            print(char, end='')
            if char == '\n':
                linha+=1
            pointer+=1
        else:
            lista_de_tokens.append(char)
            print('OUTRO ', end=' ')
            pointer+=1




analisador(codigo)
print()
print(lista_de_tokens)
print()
print(tabela_de_simbolos)
















# file_path = 'arquivo.lcc'




# try:
#     with open(file_path, 'r') as file:
#         while True:
#             char = file.read()
#             if not char:
#                 break
           
#             analisador_ident(char, 0)
# except FileNotFoundError:
#     print(f"File '{file_path}' not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")


