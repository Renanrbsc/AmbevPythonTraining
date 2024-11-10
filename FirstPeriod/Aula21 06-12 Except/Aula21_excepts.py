try:
    arquivo = open('')
except OSError:
    print('Ocorreu um erro!')
else:
    print('Nao houve erro! Continuando...')
finally:
    print('Finanlizando processo!')
    if 'close' in dir(arquivo):
        arquivo.close()

