from rich.panel import Panel
from rich import print
from time import sleep
import math


# funções para os menus
def menu():
    """MENU PRINCIPAL DO PROGRAMA COM AS OPÇÕES DE FORRO, LAJE, INFORMAÇÕES E SAIR
    USE O TECLADO PARA DIGITAR O NÚMERO DA OPÇÃO DESEJADA"""
    msg = Panel(
        "[magenta]ESCOLHA UMA OPÇÃO [ESCREVA O NÚMERO DA OPÇÃO] \n"
        "[ 1 ] FORRO\n"
        "[ 2 ] LAJE\n"
        "[ 3 ] TIJOLOS\n"
        "[ 4 ] INFORMAÇÕES\n"
        "[ 5 ] SAIR[/]",
        title="[bold magenta]Menu[/]",
        border_style="bold magenta",
        width=50)

    return msg


def escolhaforro():
    """MENU DE OPÇÕES PARA O FORRO, COM AS OPÇÕES DE CALCULAR POR M²,
    CALCULAR POR BARRA E VOLTAR AO MENU PRINCIPAL
    USE O TECLADO PARA DIGITAR O NÚMERO DA OPÇÃO DESEJADA"""
    msg = Panel(
        "[blue]ESCOLHA UMA OPÇÃO [ESCREVA O NÚMERO DA OPÇÃO] \n"
        "[ 1 ] FORRO CALCULADO POR M²\n"
        "[ 2 ] FORRO CALCULADO POR BARRA\n"
        "[ 3 ] VOLTAR AO MENU[/]",
        title="[bold blue]FORRO[/]", border_style="bold blue", width=50
    )
    return msg


def escolhalaje():
    """MENU DE OPÇÕES PARA A LAJE, COM AS OPÇÕES DE CALCULAR POR M²,
    CALCULAR QUANTIDADE DE LAJOTAS E VOLTAR AO MENU PRINCIPAL
    USE O TECLADO PARA DIGITAR O NÚMERO DA OPÇÃO DESEJADA"""
    msg = Panel(
        "[cyan]ESCOLHA UMA OPÇÃO [ESCREVA O NÚMERO DA OPÇÃO] \n"
        "[ 1 ] LAJE CALCULADO POR M²\n"
        "[ 2 ] CALCULAR QUANTIDADE DE LAJOTAS\n"
        "[ 3 ] VOLTAR AO MENU[/]",
        title="[bold cyan]LAJE[/]", border_style="bold cyan", width=50
    )
    return msg

def escolhatijolo():
    """MENU DE OPÇÕES PARA O TIJOLO, COM AS OPÇÕES DE CALCULAR TIJOLO BAIANO,
    CALCULAR TIJOLO BAIANINHO, CALCULAR TIJOLO MINEIRÃO, CALCULAR BLOCO E VOLTAR AO MENU PRINCIPAL
    USE O TECLADO PARA DIGITAR O NÚMERO DA OPÇÃO DESEJADA"""
    msg = Panel(
        "[color(208)]ESCOLHA UMA OPÇÃO [ESCREVA O NÚMERO DA OPÇÃO] \n"
        "[ 1 ] CALCULAR TIJOLO BAIANO\n"
        "[ 2 ] CALCULAR TIJOLO BAIANINHO\n"
        "[ 3 ] CALCULAR TIJOLO MINEIRÃO\n"
        "[ 4 ] CALCULAR BLOCO\n"
        "[ 5 ] VOLTAR AO MENU[/]",
        title="[bold color(208)]TIJOLO[/]", border_style="bold color(208)", width=50
    )
    return msg


def calcularforrom2(barra, parede):
    """FUNÇÃO PARA CALCULAR O FORRO POR M²,
    RECEBENDO O TAMANHO DA BARRA E O TAMANHO DA PAREDE COMO PARÂMETROS
    TAMBÉM TENDO A OPÇÃO DE DIVIDIR AS BARRAS E CALCULAR RODA FORRO/MEIA CANA"""
    mbarra = barra * 0.2
    qbarra = math.ceil(parede / 0.2)
    total = qbarra * mbarra
    sleep(1.2)
    print(f"SERIAM [green]{qbarra}[/] BARRAS DANDO [green]{total:.2f}M²[/]")
    sleep(1.2)
    while True:
        try:
            print("[bold yellow]QUER DIVIDIR AS BARRAS? S/N:[/] ")
            resposta = input().upper()

            if resposta == 'S':
                print('[bold yellow]QUER DIVIDIR POR QUANTO: [/]')
                dividir = float(input())
                if dividir == 0:
                    print('[bold red]ERRO: NÃO PODE DIVIDIR POR ZERO[/]')
                    continue
                divisao = qbarra / dividir
                totaldividio = total / dividir
                sleep(1.2)
                print(f'SERIAM [green]{divisao:.2f}[/] BARRAS DANDO [green]{totaldividio:.2f}M²[/]')
                sleep(1.2)
                break

            elif resposta == 'N':
                sleep(1)
                print("[bold yellow]...[/]")
                break

            else:
                print('[bold red]OPÇÃO INVÁLIDA[/]')

        except ValueError:
            print('[bold red]ERRO: DIGITE UM NÚMERO VÁLIDO[/]')

    while True:
        try:
            print("[bold yellow]QUER CALCULAR RODA FORRO/MEIA CANA TAMBÉM? S/N:[/] ")
            escolha3 = input().upper()
            if escolha3 == 'S':
                parede1 = float(input('TAMANHO DA PRIMEIRA PAREDE: '))
                if parede1 == 0:
                    print('[bold red]ERRO: O TAMANHO DA PAREDE NÃO PODE SER ZERO[/]')
                    continue
                parede2 = float(input('TAMANHO DA SEGUNDA PAREDE: '))
                if parede2 == 0:
                    print('[bold red]ERRO: O TAMANHO DA PAREDE NÃO PODE SER ZERO[/]')
                    continue
                parede3 = float(input('TAMANHO DA TERCEIRA PAREDE: '))
                if parede3 == 0:
                    print('[bold red]ERRO: O TAMANHO DA PAREDE NÃO PODE SER ZERO[/]')
                    continue
                parede4 = float(input('TAMANHO DA QUARTA PAREDE: '))
                if parede4 == 0:
                    print('[bold red]ERRO: O TAMANHO DA PAREDE NÃO PODE SER ZERO[/]')
                    continue
                soma = math.ceil((parede1 + parede2 + parede3 + parede4) / 6)
                sleep(1.2)
                print(f"SERIAM [green]{soma}[/] BARRAS")
                sleep(1.2)
                break

            elif escolha3 == 'N':
                sleep(1)
                print("[bold yellow]...[/]")
                break

            else:
                print('[bold red]OPÇÃO INVÁLIDA[/]')

        except ValueError:
            print('[bold red]ERRO: DIGITE UM NÚMERO VÁLIDO[/]')
    print("[bold yellow]CALCULO CONCLUIDO![/]")
    sleep(3)


def calcularforrobarra(barra, parede):
    """FUNÇÃO PARA CALCULAR O FORRO POR BARRA,
    RECEBENDO O TAMANHO DA BARRA E O TAMANHO DA PAREDE COMO PARÂMETROS
    TAMBÉM TENDO A OPÇÃO DE CALCULAR RODA FORRO/MEIA CANA"""
    mbarra = barra * 0.2
    qbarra = math.ceil(parede / 0.2)
    total = qbarra * mbarra
    sleep(1.2)
    print(f"SERIAM [green]{qbarra}[/] BARRAS DANDO [green]{total:.2f}M²[/]")
    sleep(1.2)
    print(f"[bold yellow]QUER CALCULAR RODA FORRO/MEIA CANA TAMBÉM? S/N:[/]")
    escolha3 = input().upper()
    if escolha3 == 'S':
        parede1 = float(input('TAMANHO DA PRIMEIRA PAREDE: '))
        parede2 = float(input('TAMANHO DA SEGUNDA PAREDE: '))
        parede3 = float(input('TAMANHO DA TERCEIRA PAREDE: '))
        parede4 = float(input('TAMANHO DA QUARTA PAREDE: '))
        soma = math.ceil((parede1 + parede2 + parede3 + parede4) / 6)
        sleep(1.2)
        print(f"SERIAM [green]{soma}[/] BARRAS")
        sleep(1.2)
    elif escolha3 == 'N':
        sleep(1)
    else:
        print('[bold red]OPÇÃO INVÁLIDA[/]')
    print("[bold yellow]CALCULO CONCLUIDO![/]")
    sleep(3)


def calcularlajem2(largura, tamviga):
    """FUNÇÃO PARA CALCULAR A LAJE POR M²,
    RECEBENDO A LARGURA E O TAMANHO DA VIGA COMO PARÂMETROS"""
    qviga = (largura / 0.42).__ceil__()
    total = (qviga * tamviga) / 2.38
    sleep(1.2)
    print(f'SERIAM [green]{qviga:.2f}[/] VIGAS DANDO [green]{total:.2f}M²[/]')
    sleep(1.2)
    print(f'[bold yellow]CALCULO CONCLUIDO[/]')
    sleep(3)


def calcularlajelajotas(m2):
    """FUNÇÃO PARA CALCULAR A QUANTIDADE DE LAJOTAS NECESSÁRIAS PARA COBRIR A LAJE,
    RECEBENDO A METRAGEM QUADRADA COMO PARÂMETRO"""
    lajota = m2 * 11.4
    isopor = m2 * 2.28
    sleep(1.2)
    print(f'SERIAM [green]{math.ceil(lajota)}[/] LAJOTAS DE CERAMICA')
    sleep(1.2)
    print(f'SERIAM [green]{math.ceil(isopor)}[/] LAJOTAS DE ISOPOR')
    sleep(1.2)
    print(f'[bold yellow]CALCULO CONCLUIDO[/]')
    sleep(3)

def calculartijolobaiano(comprimento, altura):
    """FUNÇÃO PARA CALCULAR A QUANTIDADE DE TIJOLOS BAIANOS NECESSÁRIOS PARA COBRIR UMA PAREDE,
    RECEBENDO O COMPRIMENTO E ALTURA COMO PARÂMETRO"""
    total_comprimento = comprimento / 0.24
    total_altura = altura / 0.14
    total = math.ceil(total_comprimento) * math.ceil(total_altura)
    sleep(1.2)
    print(f'SERIAM [green]{total}[/] TIJOLOS BAIANOS NECESSÁRIOS PARA COBRIR A PAREDE')
    sleep(1.2)
    print(f'[bold yellow]CALCULO CONCLUIDO[/]')
    sleep(3)

def calculartijolobaianom2(m2):
    """FUNÇÃO PARA CALCULAR A QUANTIDADE DE TIJOLOS BAIANOS NECESSÁRIOS PARA COBRIR UMA PAREDE,
    RECEBENDO A METRAGEM QUADRADA COMO PARÂMETRO"""
    total = m2 * 25
    sleep(1.2)
    print(f'SERIAM [green]{math.ceil(total)}[/] TIJOLOS BAIANOS NECESSÁRIOS PARA COBRIR A PAREDE')
    sleep(1.2)
    print(f'[bold yellow]CALCULO CONCLUIDO[/]')
    sleep(3)

def calculartijolobaianinho(comprimento, altura):
    """FUNÇÃO PARA CALCULAR A QUANTIDADE DE TIJOLOS BAIANINHOS NECESSÁRIOS PARA COBRIR UMA PAREDE,
    RECEBENDO O COMPRIMENTO E ALTURA COMO PARÂMETRO"""
    total_comprimento = comprimento / 0.19
    total_altura = altura / 0.19
    total = math.ceil(total_comprimento) * math.ceil(total_altura)
    sleep(1.2)
    print(f'SERIAM [green]{total}[/] TIJOLOS BAIANINHOS NECESSÁRIOS PARA COBRIR A PAREDE')
    sleep(1.2)
    print(f'[bold yellow]CALCULO CONCLUIDO[/]')
    sleep(3)

def calculartijolobaianinhom2(m2):
    """FUNÇÃO PARA CALCULAR A QUANTIDADE DE TIJOLOS BAIANINHOS NECESSÁRIOS PARA COBRIR UMA PAREDE,
    RECEBENDO A METRAGEM QUADRADA COMO PARÂMETRO"""
    total = m2 * 25
    sleep(1.2)
    print(f'SERIAM [green]{math.ceil(total)}[/] TIJOLOS BAIANINHOS NECESSÁRIOS PARA COBRIR A PAREDE')
    sleep(1.2)
    print(f'[bold yellow]CALCULO CONCLUIDO[/]')
    sleep(3)

def calculartijolomineirao(comprimento, altura):
    """FUNÇÃO PARA CALCULAR A QUANTIDADE DE TIJOLOS MINEIRÃO NECESSÁRIOS PARA COBRIR UMA PAREDE,
    RECEBENDO O COMPRIMENTO E ALTURA COMO PARÂMETRO"""
    total_comprimento = comprimento / 0.29
    total_altura = altura / 0.19
    total = math.ceil(total_comprimento) * math.ceil(total_altura)
    sleep(1.2)
    print(f'SERIAM [green]{total}[/] TIJOLOS MINEIRÃO NECESSÁRIOS PARA COBRIR A PAREDE')
    sleep(1.2)
    print(f'[bold yellow]CALCULO CONCLUIDO[/]')
    sleep(3)

def calculartijolomineiraom2(m2):
    """FUNÇÃO PARA CALCULAR A QUANTIDADE DE TIJOLOS MINEIRÃO NECESSÁRIOS PARA COBRIR UMA PAREDE,
    RECEBENDO A METRAGEM QUADRADA COMO PARÂMETRO"""
    total = m2 * 20
    sleep(1.2)
    print(f'SERIAM [green]{math.ceil(total)}[/] TIJOLOS MINEIRÃO NECESSÁRIOS PARA COBRIR A PAREDE')
    sleep(1.2)
    print(f'[bold yellow]CALCULO CONCLUIDO[/]')
    sleep(3)

def calcularbloco(comprimento, altura):
    """FUNÇÃO PARA CALCULAR A QUANTIDADE DE BLOCOS NECESSÁRIOS PARA COBRIR UMA PAREDE,
    RECEBENDO O COMPRIMENTO E ALTURA COMO PARÂMETRO"""
    total_comprimento = comprimento / 0.39
    total_altura = altura / 0.19
    total = math.ceil(total_comprimento) * math.ceil(total_altura)
    sleep(1.2)
    print(f'SERIAM [green]{total}[/] BLOCOS NECESSÁRIOS PARA COBRIR A PAREDE')
    sleep(1.2)
    print(f'[bold yellow]CALCULO CONCLUIDO[/]')
    sleep(3)

def calcularblocom2(m2):
    """FUNÇÃO PARA CALCULAR A QUANTIDADE DE BLOCOS NECESSÁRIOS PARA COBRIR UMA PAREDE,
    RECEBENDO A METRAGEM QUADRADA COMO PARÂMETRO"""
    total = m2 * 14
    sleep(1.2)
    print(f'SERIAM [green]{math.ceil(total)}[/] BLOCOS NECESSÁRIOS PARA COBRIR A PAREDE')
    sleep(1.2)
    print(f'[bold yellow]CALCULO CONCLUIDO[/]')
    sleep(3)

def informacoes():
    msg = Panel(
        "[cyan]INFORMAÇÕES SOBRE O PROGRAMA: \n"
        "ESTE PROGRAMA FOI DESENVOLVIDO PARA AUXILIAR NA HORA DE CALCULAR FORROS E LAJES, \n"
        "OFERECENDO OPÇÕES DE CÁLCULO POR M² OU POR BARRA, ALÉM DE INFORMAÇÕES SOBRE A QUANTIDADE DE LAJOTAS NECESSÁRIAS. \n"
        "O PROGRAMA É FÁCIL DE USAR E FOI PROJETADO PARA SER ACESSÍVEL A TODOS, INDEPENDENTEMENTE DO NÍVEL DE EXPERIÊNCIA EM CONSTRUÇÃO. \n"
        "USE O PONTO '.' AO INVÉS DA VÍRGULA PARA DIGITAR NÚMEROS QUEBRADOS. \n"
        "ESPERO QUE ESTE PROGRAMA SEJA ÚTIL PARA VOCÊS![/]",
        title="[bold white on green]INFORMAÇÕES[/]", border_style="bold green", width=70)
    return msg

