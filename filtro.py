arquivo = open('C:\\Users\\876338\\Desktop\\words\\palavras_c5.txt', 'r', encoding="utf-8")

with open('C:\\Users\\876338\\Desktop\\words\\palavras_c5.txt', 'r', encoding="utf-8") as f:
        palavras = [line.rstrip() for line in f]

conjunto = 'o'

for palavra in palavras:
    if (conjunto in palavra[1]) and (conjunto in palavra[4]) and ('u' in palavra[2]) and ('r' in palavra) and (not'a' in palavra) and (not'p' in palavra) and (not'd' in palavra) and (not'l' in palavra) and (not't' in palavra):
        print(palavra)