from rich.panel import Panel

#funções para os menus
def menu(msg):
    msg = Panel(
        "[magenta]ESCOLHA UMA OPÇÃO [ESCREVA O NÚMERO DA OPÇÃO] \n"
        "[ 1 ] FORRO\n"
        "[ 2 ] LAJE\n"
        "[ 3 ] INFORMAÇÕES\n"
        "[ 4 ] SAIR[/]",
        title="[bold magenta]Menu[/]", border_style="bold magenta", width=50
        )
    return msg

def EscolhaForro(msg):
    msg = Panel(
        "[magenta]ESCOLHA UMA OPÇÃO [ESCREVA O NÚMERO DA OPÇÃO] \n"
        "[ 1 ] FORRO CALCULADO POR M²\n"
        "[ 2 ] FORRO CALCULADO POR BARRA[/]",
        title="[bold magenta]FORRO[/]", border_style="bold magenta", width=50
        )
    return msg

def CalcularForrom(barra, parede):
    mbarra = barra * 0.2
    qbarra = (parede / 0.2).__ceil__()
    total = qbarra * mbarra
    return f"SERIAM [green]{qbarra}[/] BARRAS DANDO [green]{total}M²[/]"