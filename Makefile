# Makefile for Lexical and Syntactic Analyzer
# Desenvolvido com python na versão 3.11.4

PYTHON = py

all: analizador_lexico monta_tabela analisador_sintatico

analizador_lexico:
	$(PYTHON) analizador_lexico.py

monta_tabela: analizador_lexico
	$(PYTHON) monta_tabela.py

analisador_sintatico: analizador_lexico monta_tabela
	$(PYTHON) analisador_sintatico.py

.PHONY: all analizador_lexico monta_tabela analisador_sintatico
