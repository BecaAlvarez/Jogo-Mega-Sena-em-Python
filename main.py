from funcoes import *

print('-'*30)
print('JOGA NA MEGA SENA' )
print('-'*30)

while True:
    Jogo()
    while True:
        print('[Digite "S" para sim ou "N" para não]')
        resp = str(input("Deseja jogar novamente? "))
        if resp not in 'SsNn':
            print('VALOR INVÁLIDO!!!')
            continue
        else:
            break
    if resp in 'Ss':
        continue
    else:
        break

print("Fim do programa")
