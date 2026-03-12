# calculador
Programa que calcula forros e lajes automaticamente, destinado à depósitos de material de construção 

from time import sleep
from colorama import init, Fore, Style


init()


estilo = {
    'negrito' : Style.BRIGHT,
    'reset' : Style.RESET_ALL,
}

cores = {
    'verde' : Fore.GREEN,
    'azul' : Fore.BLUE,
    'amarelo' : Fore.YELLOW,
    'roxo' : Fore.MAGENTA,
    'vermelho' : Fore.RED,
    'limpa' : Fore.RESET,
}


titulo = 'BEM VINDO AO CALCULATOR 2000'
print(f'{estilo['negrito']}{cores['vermelho']}CRIADO POR MATHEUS O. AMORIM       VERSÃO 2.1{cores['limpa']}{estilo['reset']}')
print('-' * 50)
print(f'{estilo['negrito']}{cores['verde']}{titulo.center(50)}{cores['limpa']}{estilo['reset']}'.center(40))
print('-' * 50)
sleep(1)


escolha = 0

while escolha != 4:
    print(f'{estilo['negrito']}{cores['roxo']}ESCOLHA UMA OPÇÃO [ESCREVA O NÚMERO DA OPÇÃO]:{cores['limpa']}{estilo['reset']} ')
    print(f'''{estilo['negrito']}{cores['roxo']}
 [ 1 ] FORRO
 [ 2 ] LAJE
 [ 3 ] INFORMAÇÕES
 [ 4 ] SAIR{cores['limpa']}{estilo['reset']}''')


    escolha = int(input())
    if escolha == 1:
        print(f'{estilo['negrito']}{cores['azul']}VOCÊ ESCOLHEU FORRO{cores['limpa']}{estilo['reset']}')
        print(f'''{estilo['negrito']}{cores['roxo']}
[ 1 ] FORRO CALCULADO POR M²
[ 2 ] FORRO CALCULADO POR BARRA{cores['limpa']}{estilo['reset']}''')
        escolha2 = int(input(''))
        if escolha2 == 1:
            tambarra = float(input('QUAL O TAMANHO DA BARRA: '))
            mbarra = tambarra * 0.2
            tamparede = float(input('QUAL A LARGURA: '))
            qbarra = (tamparede / 0.2).__ceil__()
            total = qbarra * mbarra
            sleep(1.2)
            print(f'SERIAM {cores['verde']}{qbarra}{cores['limpa']} BARRAS DANDO {cores['verde']}{total:.2f}M²{cores['limpa']}')
            sleep(1.2)
            resposta = input(f'{estilo['negrito']}{cores['amarelo']}QUER DIVIDIR AS BARRAS? S/N:{cores['limpa']}{estilo['reset']} ').upper()
            if resposta == 'S':
                dividir = float(input(f'{estilo['negrito']}{cores['amarelo']}QUER DIVIDIR POR QUANTO:{cores['limpa']} '))
                divisao = qbarra / dividir
                totaldividio = total / dividir
                sleep(1.2)
                print(f'SERIAM {cores['verde']}{divisao:.2f}{cores['limpa']} BARRAS DANDO {cores['verde']}{totaldividio:.2f}M²{cores['limpa']}')
                sleep(1.2)
            else:
                print('')
        elif escolha2 == 2:
            barra = float(input('TAMANHO DA BARRA: '))
            quantidade = int(input('QUANTIDADE DE BARRAS: '))
            soma = (barra * 0.2) * quantidade
            sleep(1.2)
            print(f'SERIAM {cores['verde']}{quantidade}{cores['limpa']} BARRAS DANDO {cores['verde']}{soma:.2f}M²{cores['limpa']}')
            sleep(1.2)
        escolha3 = input(f'{estilo['negrito']}{cores['amarelo']}QUER CALCULAR RODA FORRO/MEIA CANA TAMBÉM? S/N:{cores['limpa']}{estilo['reset']} ').upper()
        if escolha3 == 'S':
            parede1 = float(input('TAMANHO DA PRIMEIRA PAREDE: '))
            parede2 = float(input('TAMANHO DA SEGUNDA PAREDE: '))
            parede3 = float(input('TAMANHO DA TERCEIRA PAREDE: '))
            parede4 = float(input('TAMANHO DA QUARTA PAREDE: '))
            soma = ((parede1 + parede2 + parede3 + parede4) / 6).__ceil__()
            sleep(1.2)
            print(f'SERIAM {cores['verde']}{soma}{cores['limpa']} BARRAS')
            sleep(1.2)
        elif escolha3 == 'N':
            print('')
            sleep(1)
        print(f'{estilo['negrito']}{cores['amarelo']}CALCULO CONCLUIDO{cores['limpa']}{estilo['reset']}')
        sleep(3)

    elif escolha == 2:
        print(f'{estilo['negrito']}{cores['azul']}VOCÊ ESCOLHEU LAJE{cores['limpa']}{estilo['reset']}')
        print(f'''{estilo['negrito']}{cores['roxo']}
[ 1 ] LAJE CALCULADO POR M²
[ 2 ] CALCULAR QUANTIDADE DE LAJOTAS{cores['limpa']}{estilo['reset']}''')
        escolha2 = int(input(''))
        if escolha2 == 1:
            largura = float(input('QUAL A LARGURA: '))
            qviga = (largura / 0.42).__ceil__()
            tamviga = float(input('QUAL O TAMANHO DA VIGA: '))
            total = (qviga * tamviga) / 2.38
            sleep(1.2)
            print(f'SERIAM {cores['verde']}{qviga:.2f}{cores['limpa']} VIGAS DANDO {cores['verde']}{total:.2f}M²{cores['limpa']}')
            sleep(1.2)
            print(f'{estilo['negrito']}{cores['amarelo']}CALCULO CONCLUIDO{cores['limpa']}{estilo['reset']}')
            sleep(3)
        elif escolha2 == 2:
            m2 = float(input('QUAL A METRAGEM QUADRADA?: '))
            lajota = m2 * 11.4
            isopor = m2 * 2.28
            sleep(1.2)
            print(f'SERIAM {cores['verde']}{lajota.__ceil__()}{cores['limpa']} LAJOTAS DE CERAMICA{cores['limpa']}')
            sleep(1.2)
            print(f'SERIAM {cores['verde']}{isopor.__ceil__()}{cores['limpa']} LAJOTAS DE ISOPOR{cores['limpa']}')
            sleep(1.2)
            print(f'{estilo['negrito']}{cores['amarelo']}CALCULO CONCLUIDO{cores['limpa']}{estilo['reset']}')
            sleep(3)

    elif escolha == 3:
        print(f'{estilo['negrito']}{cores['azul']}VOCÊ ESCOLHEU INFORMAÇÕES{cores['limpa']}{estilo['reset']}')
        print('NÃO É NECESSÁRIO USAR O MOUSE, USE APENAS O TECLADO')
        sleep(1.5)
        print('TENTE NÃO DIGITAR COISAS FORA DO QUE ESTÁ PEDINDO NA TELA, DEPENDENDO DO QUE FOR PODE FECHAR O PROGRAMA')
        sleep(1.5)
        print('USE O PONTO " . " PARA NÚMEROS QUEBRADOS, A VIRGULA NÃO FUNCIONA PARA ISSO')
        sleep(1.5)
        print('QUALQUER DUVIDA ENTRAR EM CONTATO COM O NOSSO WHATSAPP DE SUPORTE')
        sleep(1.5)
        print(f'{estilo['negrito']}{cores['amarelo']}OBRIGADO!{cores['limpa']}{estilo['reset']}\n')
        sleep(3)

    elif escolha == 4:
        print(f'{estilo['negrito']}{cores['amarelo']}ENCERRANDO PROGRAMA{cores['limpa']}{estilo['reset']}')
        print(f'{cores['verde']}.{cores['limpa']}')
        sleep(0.5)
        print(f'{cores['amarelo']}.{cores['limpa']}')
        sleep(0.5)
        print(f'{cores['vermelho']}.{cores['limpa']}')
        sleep(0.5)
        print(f'{cores['vermelho']}ENCERRADO COM SUCESSO.{cores['limpa']}')
        sleep(2)

    else:
        print(f'{estilo['negrito']}{cores['vermelho']}OPÇÃO INVÁLIDA{cores['limpa']}{estilo['reset']}')
        sleep(1.5)
