# verifica se ano é ou não bissexto

# apresentação
print('\n\t\t\t -- Verifique se ano é ou não bissexto -- \n')

# processamento
def bissexto(ano):

    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return True

    else:
        return False

# saída
entrada = int(input("Digite o ano: "))

if bissexto(entrada):

    print(f"O ano {entrada} é bissexto.")

else:
    print(f"O ano {entrada} não é bissexto.")