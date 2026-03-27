from time import sleep
from rich import print
from rich.panel import Panel
import pacotes.funcoes



#titulo do programa e mensagem de boas vindas
print('[bold red]CRIADO POR MATHEUS O. AMORIM       VERSÃO 3.1[/]')
panel = Panel("[bold white on green]        BEM VINDO AO CALCULATOR 2000         ", title="[bold green]CALCULATOR 2000[/]", border_style="bold green", width=50)
print(panel)

sleep(1)

#escolha uma opção entre forro, laje, informações ou sair do programa
escolha = 0
while escolha != 4:

    print(pacotes.funcoes.menu('Menu'))

#escolha do menu
    escolha = int(input())

#escolha nº1: Forro pvc
    if escolha == 1:
        print("[bold blue]VOCÊ ESCOLHEU FORRO[/]")
        print(pacotes.funcoes.EscolhaForro('FORRO')) 
        escolha2 = int(input(''))
        if escolha2 == 1: #forro calculado por m²
            while True:
                try:
                    tambarra = float(input('QUAL O TAMANHO DA BARRA: '))
                    tamparede = float(input('QUAL A LARGURA: '))
                    sleep(1.2)
                except (TypeError, ValueError):
                    print('[bold red]ERRO: ENTRADA INVÁLIDA. POR FAVOR, INSIRA NÚMEROS VÁLIDOS.[/]')
                
                except ZeroDivisionError:
                    print('[bold red]ERRO: A LARGURA NÃO PODE SER ZERO[/]')
                
                else:
                    print(pacotes.funcoes.CalcularForrom(tambarra, tamparede)) #função para calcular o forro por m²
                    sleep(1.2)
                    break

        elif escolha2 == 2: #forro calculado por barra
            while True:
                try:
                     tambarra = float(input('QUAL O TAMANHO DA BARRA: '))
                     if tambarra == 0:
                        print('[bold red]ERRO: O TAMANHO DA BARRA NÃO PODE SER ZERO[/]')
                        continue
                     tamparede = float(input('QUAL A LARGURA: '))
                     if tamparede == 0:
                        print('[bold red]ERRO: A LARGURA NÃO PODE SER ZERO[/]')
                        continue
                     sleep(1.2)
                except (TypeError, ValueError):
                    print('[bold red]ERRO: ENTRADA INVÁLIDA. POR FAVOR, INSIRA NÚMEROS VÁLIDOS.[/]')
                
                except ZeroDivisionError:
                    print('[bold red]ERRO: A LARGURA NÃO PODE SER ZERO[/]')
                
                else:
                     print(pacotes.funcoes.CalcularForrom(tambarra, tamparede)) #função para calcular o forro por barra
                     sleep(1.2)
                     break
            
        elif escolha == 3:
            break
        else:
            print('[bold red]OPÇÃO INVÁLIDA[/]')
            sleep(1.2)
            continue

#escolha nº2: Laje
    elif escolha == 2:
        print(f'[bold cyan]VOCÊ ESCOLHEU LAJE[/]')
        print(pacotes.funcoes.EscolhaLaje('LAJE'))
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