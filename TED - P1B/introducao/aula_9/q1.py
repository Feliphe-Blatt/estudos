def conta_vogais(texto:str) -> int:
    
    quantidade = 0
    vogais = "aeiouAEIOU"

    for letra in texto:

        if letra in vogais:
            quantidade += 1

    return quantidade

frase = "Esta e uma frase de teste"

print(f'\n A frase informada possui: {conta_vogais(frase)} vogais!\n')