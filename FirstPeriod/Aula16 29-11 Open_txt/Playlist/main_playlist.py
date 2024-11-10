# Aula 16 - 29-11-19
#???????

#cadastro de playlist
# lendo musica,artista e albuns

from def_playlist import *

musica = input('Digite uma musica: ')
album = input('Digite o nome do album: ')
artista = input('Digite o nome do artista: ')

faixa = criar_faixa(musica,album,artista)
salvar_faixa(faixa)
lista = ler_playlist()

c=0
for i in lista:
    print(f"{c} - Musica: {i['musica']} - Album: {i['album']} - Artista: {i['artista']}")
    c = c + 1