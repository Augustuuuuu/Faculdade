# -*- coding: utf-8 -*-
# Script Corrigido para Decodificar o Emoji CTF

# ATENÇÃO: Esta é a string original e verificada do desafio.
# O erro no script anterior foi usar uma string corrompida.
ctf_string = ""

decoded_flag = ""

# Percorre cada caractere na string
for char in ctf_string:
    # Pega o número do código Unicode do caractere
    codepoint = ord(char)

    # Verifica se o caractere está no intervalo dos dados escondidos
    if 0xE0100 <= codepoint <= 0xE01EF:
        # Isola o último byte do código, que corresponde ao caractere ASCII
        ascii_value = codepoint & 0xFF
        
        # Converte o valor ASCII para um caractere e adiciona à flag
        decoded_flag += chr(ascii_value)

# Imprime a flag final e correta
print(decoded_flag)