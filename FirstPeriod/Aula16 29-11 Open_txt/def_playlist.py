def criar_faixa(mus, alb, art):
    faixa = {'musica':mus,'album':alb,'artista':art}
    return faixa

def salvar_faixa(faixa):
    arquivo = open('Aula16 29-11/cadastro_playlist.txt','a')
    arquivo.write(f"{faixa['musica']};{faixa['album']};{faixa['artista']}\n")
    arquivo.close()

def ler_playlist():
    playlist = []
    arquivo = open('Aula16 29-11/cadastro_playlist.txt','r')
    for i in arquivo:
        i = i.strip()
        i_linha = i.split(';')
        faixa = criar_faixa(i_linha[0],i_linha[1],i_linha[2])
        playlist.append(faixa)
    arquivo.close()
    return playlist

        