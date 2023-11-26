# Analisador Léxico e Sintático para Análise LL(1)

Repositório do Analisador Léxico e Sintático em Python para análise de código fonte, identificação de tokens e análise de gramática.

Este repositório contém três arquivos para análise léxica e sintática de uma linguagem:

1. **analizador_lexico.py**

   - **Descrição:** Este script em Python realiza análise léxica no código-fonte de entrada e gera uma lista de tokens juntamente com uma tabela de símbolos. Relata erros léxicos em linha, se houver.
   - **Uso:** Execute este script primeiro passando como flag o arquivo lcc contendo o código a ser análisado léxica e sintáticamente.
   - **Exemplo:**
     ```bash
     python analizador_lexico.py arquivo1.lcc 
     ```
   - **Saída:**
     - `lista_tokens`: Lista de tokens.
     - `tabela_simbolos`: Tabela de símbolos.
     - `lista_tokens.csv`: Lista de tokens em formato csv para análise sintática.

2. **monta_tabela.py**

   - **Descrição:** Este script em Python constrói a tabela de reconhecimento sintático LL(1) para a gramática.
   - **Uso:** Execute este script após executar `analizador_lexico.py`.
   - **Exemplo:**
     ```bash
     python monta_tabela.py
     ```
   - **Saída:**
     - `tabela_sintatica`: Tabela de reconhecimento LL(1).
     - `tabela_sintatica.csv`: Tabela de reconhecimento LL(1) em formato csv para análise sintática.

3. **analisador_sintatico.py**

   - **Descrição:** Este script em Python realiza análise sintática usando a lista de tokens e a tabela de reconhecimento criadas anteriormente. Exibe as produções e uma mensagem de sucesso se não houver erros sintáticos.
   - **Uso:** Execute este script por último, após executar tanto `analizador_lexico.py` quanto `monta_tabela.py`.
   - **Exemplo:**
     ```bash
     python analisador_sintatico.py
     ```
   - **Dependências:**
     - Requer `lista_tokens.csv` gerado por `analizador_lexico.py`.
     - Requer `tabela_sintatica.csv` gerado por `monta_tabela.py`.
    
   - **Saída:**
     - `Produções para a lista de tokens baseadas na tabela de reconhecimento`

**Observação:** Certifique-se de executar os scripts na ordem especificada para evitar erros. O script `analisador_sintatico.py` depende dos arquivos de saída gerados pelos scripts anteriores.
