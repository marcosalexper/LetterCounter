frase = 'Python é uma linguagem versátil e fácil de aprender' 

i = 0
qtd_apareceu_mais_vezes = 0
letra_que_mais_apareceu = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quantas_vezes_apareceu = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < quantas_vezes_apareceu:
        qtd_apareceu_mais_vezes = quantas_vezes_apareceu
        letra_que_mais_apareceu = letra_atual


    i += 1

print(f'A letra "{letra_que_mais_apareceu}" apareceu {qtd_apareceu_mais_vezes} vezes.')