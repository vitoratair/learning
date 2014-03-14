#!/usr/bin/env python
# -*- coding: utf-8 -*-


#	Input no terminal com concatenação de string


def main():

	# Pula uma linha
    print "\n"

    # Pedo ao usuário que digite algo, o conteúdo será armazenado na variável varInput
    varInput = raw_input("Entre com seu nome: ")

    # Pula uma linha
    print "\n"

    # Exibe o conteúdo armazenado na variável varInput concatenando com outras strings
    print "Seja vem vindo ao python <<< " + varInput + " >>>"


if "__main__" == __name__:
    main()
