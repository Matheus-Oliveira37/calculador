from rich.panel import Panel
from rich import print
from time import sleep
import math

#funções para os menus
def menu(msg):
    msg = Panel(
        "[magenta]ESCOLHA UMA OPÇÃO [ESCREVA O NÚMERO DA OPÇÃO] \n"
        "[ 1 ] FORRO\n"
        "[ 2 ] LAJE\n"
        "[ 3 ] INFORMAÇÕES\n"
        "[ 4 ] SAIR[/]",
        title="[bold magenta]Menu[/]",
        border_style="bold magenta",
        width=50)
        
    return msg

def EscolhaForro(msg):
    msg = Panel(
        "[blue]ESCOLHA UMA OPÇÃO [ESCREVA O NÚMERO DA OPÇÃO] \n"
        "[ 1 ] FORRO CALCULADO POR M²\n"
        "[ 2 ] FORRO CALCULADO POR BARRA\n"
        "[ 3 ] VOLTAR AO MENU[/]",
        title="[bold blue]FORRO[/]", border_style="bold blue", width=50
        )
    return msg

def EscolhaLaje(msg):
    msg = Panel(
        "[cyan]ESCOLHA UMA OPÇÃO [ESCREVA O NÚMERO DA OPÇÃO] \n"
        "[ 1 ] LAJE CALCULADO POR M²\n"
        "[ 2 ] CALCULAR QUANTIDADE DE LAJOTAS\n"
        "[ 3 ] VOLTAR AO MENU[/]",
        title="[bold cyan]LAJE[/]", border_style="bold cyan", width=50
        )
    return msg

def CalcularForrom(barra, parede):
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
    
def CalcularForroBarra(barra, parede):
    mbarra = barra * 0.2
    qbarra = (parede / 0.2).__ceil__()
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
            soma = ((parede1 + parede2 + parede3 + parede4) / 6).__ceil__()
            sleep(1.2)
            print(f"SERIAM [green]{soma}[/] BARRAS")
            sleep(1.2)
    elif escolha3 == 'N':
            sleep(1)
    else:
        print('[bold red]OPÇÃO INVÁLIDA[/]')
    print("[bold yellow]CALCULO CONCLUIDO![/]")
    sleep(3)

print(EscolhaForro('FORRO'))
print(EscolhaLaje('LAJE'))