#Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter_string(texto):
    """
    Inverte os caracteres de uma string.

    Args:
        texto: A string a ser invertida.

    Returns:
        A string invertida.
    """

    string_invertida = ""
    for i in range(len(texto) - 1, -1, -1):
        string_invertida += texto[i]
    return string_invertida


# String a ser invertida 
texto_original = "Target" 

# Invertendo a string
texto_invertido = inverter_string(texto_original)

# Exibindo o resultado
print(f"String original: {texto_original}")
print(f"String invertida: {texto_invertido}")