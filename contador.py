# Programa para contar, separar e mostrar total de palavras em um arquivo texto fornecido pelo usuario
caminho_arquivo = input("Digite o caminho do arquivo: ")

with open(caminho_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()

palavras = conteudo.split()

print(f"O arquivo possui {len(palavras)} palavras")

for palavra in palavras:
    print(f"A palavra {palavra} aparece {palavras.count(palavra)} vezes")
