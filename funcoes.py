from random import randint


def Jogo():
    while True:
        v = tratamento()
        if v:
            jogo = list()
            lista = list()
            print(f'-=-=-= SORTEANDO OS JOGOS -=-=-=')
            tot = 1
            print(f'Os números sorteados foram: ')
            while tot <= v:
                cont = 0
                while True:
                    num = randint(1, 60)
                    if num not in jogo:
                        jogo.append(num)
                        cont += 1
                    if cont >= 6:
                        break
                jogo.sort()
                lista.append(jogo[:])
                jogo.clear()
                tot += 1
            for i, l in enumerate(lista):
                print(f'Jogo {i + 1}: {l}')
        else:
            continue
        print('-'*32)
        break


def tratamento():
    try:
        v = int(input("Quantos jogos vc quer que eu sorteie? "))
    except(ValueError, TypeError):
        print('VALOR INVÁLIDO!!!')
        return False
    else:
        return v

