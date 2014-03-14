#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import system

# Iniciando no if else e if elif else


def main():

    # Limpar a tela com a função clear da biblioteca os
    system("clear")

    # Pedo ao usuário que digite um número
    numero = int(raw_input("Insira um número: "))

	# Exemplo básico de if else
    if numero < 0:
    	print "Número menor que 0"    	    	

    else:
		print "Número maior que 0"

    if numero > 0 and numero < 50:
		print "Número maior que 0 e menor que 50"


# ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- #

    # Pula uma linha
    print "\n"

    # Pedo ao usuário que digite um número
    numero = int(raw_input("Insira um número: "))

    # Exemplo básico de if else de outros if elses
    if numero > 0:
        print "Número maior que 0"
        if numero > 0 and numero < 50:
        	print "Número maior que 0 e menor que 50"
    else:
        print "Número menor que 0"

# ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- ## ---- #

    # Pula uma linha
    print "\n"

    # Pedo ao usuário que digite um número
    numero = int(raw_input("Insira um número: "))

    # Exemplo básico de if elif
    if numero < 0:
    	print "Número menor que 0"    	    	

    elif numero > 0:
		print "Número maior que 0"

    elif numero > 0 and numero < 50:
		print "Número maior que 0 e menor que 50"


if "__main__" == __name__:
    main()
