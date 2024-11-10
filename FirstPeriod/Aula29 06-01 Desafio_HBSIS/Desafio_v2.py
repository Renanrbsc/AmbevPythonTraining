
Fortwo=[]
Embarcado=[]
Terminal=['Piloto','Oficial 1','Oficial 2','Chefe de Serviço','Comissária 1','Comissária 2','Policial','Prisioneiro']

def viagens(Terminal):
    if 'Policial' in Terminal[1] and 'Prisioneiro' in Terminal[2]:
        Fortwo.insert(1, Terminal.pop(2))
        Fortwo.insert(0, Terminal.pop(1)) 
        atualizar_terminal(Terminal)
        print(f'Fortwo: {Fortwo[0]} e {Fortwo[1]}\nTerminal:{Terminal}\nFortwo Retorno: {Fortwo[0]}')
        input('...')
        Embarcado.append(Fortwo.pop(1))
        atualizar_embarcado(Embarcado)
        Embarcado.append(Fortwo.pop(0))
        atualizar_embarcado(Embarcado)
        Terminal.insert(1, Embarcado.pop(2))
        atualizar_terminal(Terminal)
        print(f'\nEmbarcado: {Embarcado}\nTerminal:{Terminal}')
        input('...')
    else:
        Fortwo.append(Terminal.pop(0))
        Fortwo.append(Terminal.pop(0))
        atualizar_terminal(Terminal)
        if 'Chefe de Servico' in Fortwo[1]:
            Fortwo.insert(0, Fortwo.pop(1))
        print(f'Fortwo: {Fortwo[0]} e {Fortwo[1]}\nTerminal:{Terminal}\nFortwo Retorno: {Fortwo[0]}')
        input('...')
        Embarcado.append(Fortwo.pop(1))
        atualizar_embarcado(Embarcado)
        Terminal.insert(0, Fortwo.pop(0))
        if len(Terminal) == 1:
            Embarcado.append(Terminal.pop(0))
            atualizar_embarcado(Embarcado)
        atualizar_terminal(Terminal)
        print(f'Embarcado: {Embarcado}\nTerminal:{Terminal}')
        input('...')

def atualizar_terminal(Terminal):
    arq = open('TrabalhosPython\Aula29 06-01\Terminal.txt','w')
    arq.write(''.join(Terminal)+'\n')

def atualizar_embarcado(Embarcado):
    arq = open('TrabalhosPython\Aula29 06-01\Embarcado.txt','w')
    arq.write(''.join(Embarcado)+'\n')


print(f'Terminal: {Terminal}\n')

for i in range(1,8):
    print(f'--------Viagem {i}--------')
    viagens(Terminal)

