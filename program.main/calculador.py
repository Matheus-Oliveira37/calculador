from time import sleep
from rich import print
from rich.panel import Panel
import pacotes.funcoes



#programa principal

print('[bold red]CRIADO POR MATHEUS O. AMORIM       VERSÃO 3.1[/]')
panel = Panel("BEM VINDO AO CALCULATOR 2000", title="[bold green]CALCULATOR 2000[/]", border_style="bold green", width=50)
print(panel)

sleep(1)

#escolha uma opção entre forro, laje, informações ou sair do programa
escolha = 0
while escolha != 4:

    print(pacotes.funcoes.menu('Menu'))

    escolha = int(input())
    if escolha == 1:
        print("[bold blue]VOCÊ ESCOLHEU FORRO[/]")
        print(pacotes.funcoes.EscolhaForro('FORRO'))
        escolha2 = int(input(''))
        if escolha2 == 1:
            tambarra = float(input('QUAL O TAMANHO DA BARRA: '))
            tamparede = float(input('QUAL A LARGURA: '))
            print(pacotes.funcoes.CalcularForrom(tambarra, tamparede))
            sleep(1.2)
            resposta = input('[bold red]QUER DIVIDIR AS BARRAS? S/N:[/] ').upper()
            if resposta == 'S':
                dividir = float(input("[yellow]QUER DIVIDIR POR QUANTO:[/]"))
                divisao = qbarra / dividir
                totaldividio = total / dividir
                sleep(1.2)
                print(f"SERIAM [green]{divisao:.2f}[/] BARRAS DANDO [/]{totaldividio:.2f}M²[/]")
                sleep(1.2)
            else:
                print('')
        elif escolha2 == 2:
            barra = float(input("TAMANHO DA BARRA: "))
            quantidade = int(input("QUANTIDADE DE BARRAS: "))
            soma = (barra * 0.2) * quantidade
            sleep(1.2)
            print(f"SERIAM [green]{quantidade}[/] BARRAS DANDO [green]{soma:.2f}M²[/]")
            sleep(1.2)
        escolha3 = input(f"[bold yellow]]QUER CALCULAR RODA FORRO/MEIA CANA TAMBÉM? S/N:[/]").upper()
        if escolha3 == 'S':
            parede1 = float(input('TAMANHO DA PRIMEIRA PAREDE: '))
            parede2 = float(input('TAMANHO DA SEGUNDA PAREDE: '))
            parede3 = float(input('TAMANHO DA TERCEIRA PAREDE: '))
            parede4 = float(input('TAMANHO DA QUARTA PAREDE: '))
            soma = ((parede1 + parede2 + parede3 + parede4) / 6).__ceil__()
            sleep(1.2)
            print(f"SERIAM [green]{soma}[/]] BARRAS")
            sleep(1.2)
        elif escolha3 == 'N':
            print('')
            sleep(1)
        print(f"[bold yellow]CALCULO CONCLUIDO[/]")
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
