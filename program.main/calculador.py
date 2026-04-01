from time import sleep
from rich import print
from rich.panel import Panel
import pacotes.funcoes

# titulo do programa e mensagem de boas vindas
print('[bold red]CRIADO POR MATHEUS O. AMORIM       VERSÃO 4.2[/]')
panel = Panel("[bold white on green]        BEM VINDO AO CALCULATOR 2000         ",
              title="[bold green]CALCULATOR 2000[/]", border_style="bold green", width=50)
print(panel)

sleep(1)

# escolha uma opção entre forro, laje, informações ou sair do programa
escolha = 0
while escolha != 5:
    try:

        print(pacotes.funcoes.menu())

        # escolha do menu
        escolha = int(input())

        # escolha nº1: Forro pvc
        if escolha == 1:
            print("[bold blue]VOCÊ ESCOLHEU FORRO[/]")
            print(pacotes.funcoes.escolhaforro())
            escolha2 = int(input(''))
            if escolha2 == 1:  # forro calculado por m²
                while True:
                    try:
                        tambarra = float(input('QUAL O TAMANHO DA BARRA: '))
                        if tambarra == 0:
                            print('[bold red]ERRO: O TAMANHO DA BARRA NÃO PODE SER ZERO[/]')
                            continue
                        tamparede = float(input('QUAL A LARGURA: '))
                        if tamparede == 0:
                            print('[bold red]ERRO: O TAMANHO DA BARRA NÃO PODE SER ZERO[/]')
                            continue
                        sleep(1.2)
                    except (TypeError, ValueError):
                        print('[bold red]ERRO: ENTRADA INVÁLIDA. POR FAVOR, INSIRA NÚMEROS VÁLIDOS.[/]')

                    except ZeroDivisionError:
                        print('[bold red]ERRO: A LARGURA NÃO PODE SER ZERO[/]')

                    else:
                        print(
                            pacotes.funcoes.calcularforrom2(tambarra, tamparede))  # função para calcular o forro por m²
                        sleep(1.2)
                        break

            elif escolha2 == 2:  # forro calculado por barra
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
                        print(pacotes.funcoes.calcularforrom2(tambarra, tamparede))  # função para calcular o forro por barra
                        sleep(1.2)
                        break
            elif escolha2 == 3:
                print('[bold blue]VOLTANDO AO MENU...[/]')
                sleep(0.5)

            else:
                print('[bold red]OPÇÃO INVÁLIDA[/]')
                sleep(1.0)


        # escolha nº2: Laje
        elif escolha == 2: #opção de laje
            print(f'[bold cyan]VOCÊ ESCOLHEU LAJE[/]')
            print(pacotes.funcoes.escolhalaje())
            escolha2 = int(input(''))
            if escolha2 == 1: #opção de calcular a laje por m²
                while True:
                    try:
                        largura = float(input('QUAL A LARGURA: '))
                        if largura == 0:
                            print('[bold red]ERRO: A LARGURA NÃO PODE SER ZERO[/]')
                            continue
                        tamviga = float(input('QUAL O TAMANHO DA VIGA: '))
                        if tamviga == 0:
                            print('[bold red]ERRO: O TAMANHO DA VIGA NÃO PODE SER ZERO[/]')
                            continue
                        sleep(1.2)
                    except (TypeError, ValueError):
                        print('[bold red]ERRO: ENTRADA INVÁLIDA. POR FAVOR, INSIRA NÚMEROS VÁLIDOS.[/]')

                    except ZeroDivisionError:
                        print('[bold red]ERRO: A LARGURA NÃO PODE SER ZERO[/]')

                    else:
                        print(pacotes.funcoes.calcularlajem2(largura, tamviga))  # função para calcular a laje por m²
                        sleep(1.2)
                        break

            elif escolha2 == 2: #opção de calcular a quantidade de lajotas por m²
                while True:
                    try:
                        m2 = float(input('QUAL A METRAGEM QUADRADA?: '))
                        if m2 == 0:
                            print('[bold red]ERRO: A LARGURA NÃO PODE SER ZERO[/]')
                            continue
                        sleep(1.2)
                    except (TypeError, ValueError):
                        print('[bold red]ERRO: ENTRADA INVÁLIDA. POR FAVOR, INSIRA NÚMEROS VÁLIDOS.[/]')
                    else:
                        print(pacotes.funcoes.calcularlajelajotas(m2))  # função para calcular a quantidade de lajotas
                        sleep(1.2)
                        break

            elif escolha2 == 3:
                print('[bold cyan]VOLTANDO AO MENU...[/]')
                sleep(0.5)

            else:
                print('[bold red]OPÇÃO INVÁLIDA[/]')
                sleep(1.0)


        elif escolha == 3: #opção de tijolos/bloco
            print(f"[color(208)]VOCê ESCOLHEU TIJOLOS[/]")
            print(pacotes.funcoes.escolhatijolo())
            escolha2 = int(input(''))
            if escolha2 == 1: #opção de tijolo baiano
                while True:
                    print(pacotes.funcoes.escolhabaiano())
                    escolha3 = int(input(''))

                    if escolha3 == 1: #opção de calcular parede com tijolo baiano
                            try:
                                comprimento = float(input('QUAL O COMPRIMENTO DA PAREDE: '))
                                if comprimento == 0:
                                    print('[bold red]ERRO: O COMPRIMENTO NÃO PODE SER ZERO[/]')
                                    continue
                                altura = float(input('QUAL A ALTURA DA PAREDE: '))
                                if altura == 0:
                                    print('[bold red]ERRO: A ALTURA NÃO PODE SER ZERO[/]')
                                    continue
                                sleep(1.2)
                            except (TypeError, ValueError):
                                print('[bold red]ERRO: ENTRADA INVÁLIDA. POR FAVOR, INSIRA NÚMEROS VÁLIDOS.[/]')
                                continue

                            except ZeroDivisionError:
                                print('[bold red]ERRO: O COMPRIMENTO E A ALTURA NÃO PODEM SER ZERO[/]')

                            else:
                                print(pacotes.funcoes.calculartijolobaiano(comprimento, altura))  # função para calcular tijolo baiano
                                sleep(1.2)
                                break

                    elif escolha3 == 2: #opção de calcular a quantidade de tijolos baianos por m²
                            try:
                                m2 = float(input('QUAL A METRAGEM QUADRADA?: '))
                                if m2 == 0:
                                    print('[bold red]ERRO: A METRAGEM QUADRADA NÃO PODE SER ZERO[/]')
                                    continue
                                sleep(1.2)
                            except (TypeError, ValueError):
                                    print('[bold red]ERRO: ENTRADA INVÁLIDA. POR FAVOR, INSIRA NÚMEROS VÁLIDOS.[/]')
                            else:
                                print(pacotes.funcoes.calculartijolobaianom2(m2))  # função para calcular a quantidade de tijolos baianos por m²
                                sleep(1.2)
                                break
                    elif escolha3 == 3:
                        print('[color(208)]VOLTANDO AO MENU...[/]')
                        sleep(0.5)
                        break
                    else:
                        print('[bold red]OPÇÃO INVÁLIDA[/]')
                        sleep(1.0)        
                            
            elif escolha2 == 2: #opção de tijolo baianinho
                while True:
                    print(pacotes.funcoes.escolhabaianinho())
                    escolha3 = int(input(''))
                    if escolha3 == 1: #opção de calcular parede com tijolo baianinho
                        try:
                            comprimento = float(input('QUAL O COMPRIMENTO DA PAREDE: '))
                            if comprimento == 0:
                                print('[bold red]ERRO: O COMPRIMENTO NÃO PODE SER ZERO[/]')
                                continue
                            altura = float(input('QUAL A ALTURA DA PAREDE: '))
                            if altura == 0:
                                print('[bold red]ERRO: A ALTURA NÃO PODE SER ZERO[/]')
                                continue
                            sleep(1.2)
                        except (TypeError, ValueError):
                            print('[bold red]ERRO: ENTRADA INVÁLIDA. POR FAVOR, INSIRA NÚMEROS VÁLIDOS.[/]')

                        except ZeroDivisionError:
                            print('[bold red]ERRO: O COMPRIMENTO E A ALTURA NÃO PODEM SER ZERO[/]')

                        else:
                            print(pacotes.funcoes.calculartijolobaianinho(comprimento, altura))  # função para calcular tijolo baianinho
                            sleep(1.2)
                            break
                    elif escolha3 == 2: #opção de calcular a quantidade de tijolos baianinhos por m²
                        try:
                            m2 = float(input('QUAL A METRAGEM QUADRADA?: '))
                            if m2 == 0:
                                print('[bold red]ERRO: A METRAGEM QUADRADA NÃO PODE SER ZERO[/]')
                                continue
                            sleep(1.2)
                        except (TypeError, ValueError):
                            print('[bold red]ERRO: ENTRADA INVÁLIDA. POR FAVOR, INSIRA NÚMEROS VÁLIDOS.[/]')
                        else:
                            print(pacotes.funcoes.calculartijolobaianinhom2(m2))  # função para calcular a quantidade de tijolos baianinhos por m²
                            sleep(1.2)
                            break
                    elif escolha3 == 3:
                        print('[color(208)]VOLTANDO AO MENU...[/]')
                        sleep(0.5)
                        break
                    else:
                        print('[bold red]OPÇÃO INVÁLIDA[/]')
                        sleep(1.0)

            elif escolha2 == 3: #opção de tijolo mineirão
                while True:
                    print(pacotes.funcoes.escolhamineirao())
                    escolha3 = int(input(''))
                    if escolha3 == 1: #opção de calcular parede com tijolo mineirão
                        try:
                            comprimento = float(input('QUAL O COMPRIMENTO DA PAREDE: '))
                            if comprimento == 0:
                                print('[bold red]ERRO: O COMPRIMENTO NÃO PODE SER ZERO[/]')
                                continue
                            altura = float(input('QUAL A ALTURA DA PAREDE: '))
                            if altura == 0:
                                print('[bold red]ERRO: A ALTURA NÃO PODE SER ZERO[/]')
                                continue
                            sleep(1.2)
                        except (TypeError, ValueError):
                            print('[bold red]ERRO: ENTRADA INVÁLIDA. POR FAVOR, INSIRA NÚMEROS VÁLIDOS.[/]')

                        except ZeroDivisionError:
                            print('[bold red]ERRO: O COMPRIMENTO E A ALTURA NÃO PODEM SER ZERO[/]')

                        else:
                            print(pacotes.funcoes.calculartijolomineirao(comprimento, altura))  # função para calcular tijolo mineirão
                            sleep(1.2)
                            break
                    elif escolha3 == 2: #opção de calcular a quantidade de tijolos mineirão por m²
                        try:
                            m2 = float(input('QUAL A METRAGEM QUADRADA?: '))
                            if m2 == 0:
                                print('[bold red]ERRO: A METRAGEM QUADRADA NÃO PODE SER ZERO[/]')
                                continue
                            sleep(1.2)
                        except (TypeError, ValueError):
                            print('[bold red]ERRO: ENTRADA INVÁLIDA. POR FAVOR, INSIRA NÚMEROS VÁLIDOS.[/]')
                        else:
                            print(pacotes.funcoes.calculartijolomineiraom2(m2))  # função para calcular a quantidade de tijolos mineirão por m²
                            sleep(1.2)
                            break
                    elif escolha3 == 3:
                        print('[color(208)]VOLTANDO AO MENU...[/]')
                        sleep(0.5)
                        break
                    else:
                        print('[bold red]OPÇÃO INVÁLIDA[/]')
                        sleep(1.0)

            elif escolha2 == 4: #opção de bloco de concreto
                while True:
                    print(pacotes.funcoes.escolhabloco())
                    escolha3 = int(input(''))
                    if escolha3 == 1: #opção de calcular parede com bloco de concreto
                        try:
                            comprimento = float(input('QUAL O COMPRIMENTO DA PAREDE: '))
                            if comprimento == 0:
                                print('[bold red]ERRO: O COMPRIMENTO NÃO PODE SER ZERO[/]')
                                continue
                            altura = float(input('QUAL A ALTURA DA PAREDE: '))
                            if altura == 0:
                                print('[bold red]ERRO: A ALTURA NÃO PODE SER ZERO[/]')
                                continue
                            sleep(1.2)
                        except (TypeError, ValueError):
                            print('[bold red]ERRO: ENTRADA INVÁLIDA. POR FAVOR, INSIRA NÚMEROS VÁLIDOS.[/]')

                        except ZeroDivisionError:
                            print('[bold red]ERRO: O COMPRIMENTO E A ALTURA NÃO PODEM SER ZERO[/]')

                        else:
                            print(pacotes.funcoes.calcularbloco(comprimento, altura))  # função para calcular bloco
                            sleep(1.2)
                            break
                    elif escolha3 == 2: #opção de calcular a quantidade de blocos por m²
                        try:
                            m2 = float(input('QUAL A METRAGEM QUADRADA?: '))
                            if m2 == 0:
                                print('[bold red]ERRO: A METRAGEM QUADRADA NÃO PODE SER ZERO[/]')
                                continue
                            sleep(1.2)
                        except (TypeError, ValueError):
                            print('[bold red]ERRO: ENTRADA INVÁLIDA. POR FAVOR, INSIRA NÚMEROS VÁLIDOS.[/]')
                        else:
                            print(pacotes.funcoes.calcularblocom2(m2))  # função para calcular a quantidade de blocos por m²
                            sleep(1.2)
                            break
                    elif escolha3 == 3:
                        print('[color(208)]VOLTANDO AO MENU...[/]')
                        sleep(0.5)
                        break
                    else:
                        print('[bold red]OPÇÃO INVÁLIDA[/]')
                        sleep(1.0)

            elif escolha2 == 5:
                print('[color(208)]VOLTANDO AO MENU...[/]')
                sleep(0.5)

            else:
                print('[bold red]OPÇÃO INVÁLIDA[/]')
                sleep(1.0)


        elif escolha == 4: #opção de informações sobre o programa
            print(f'[bold green]VOCÊ ESCOLHEU INFORMAÇÕES[/]')
            print(pacotes.funcoes.informacoes())
            sleep(3)
            

        elif escolha == 5:
            print(f'[bold yellow]ENCERRANDO PROGRAMA[/]')
            print(f'[bold green].[/]')
            sleep(0.5)
            print(f'[bold yellow].[/]')
            sleep(0.5)
            print(f'[bold red].[/]')
            sleep(0.5)
            print(f'[bold bright_red italic]ENCERRADO COM SUCESSO.[/]')
            sleep(2)
            break

        else:
            print(f'[bold red]OPÇÃO INVÁLIDA[/]')
            sleep(1.5)

    except ValueError:
        print('[bold red]ERRO: DIGITE UM NÚMERO VÁLIDO[/]')
        sleep(1.5)

