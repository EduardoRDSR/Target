def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

# Entrada de string
string = input("Digite uma string: ")

# Exibir a string invertida
print("String invertida:", inverter_string(string))