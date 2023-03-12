from termcolor import colored
import os

# Arte ASCII
art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣴⣶⠶⠶⠖⠚⠛⠛⠛⠛⠒⠶⠶⣶⣶⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⡾⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡾⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⠋⠀⠀⠀⠀⢀⣠⣴⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠴⣒⡽⠟⣩⠏⢩⠉⢏⠙⠯⣑⠲⠦⣄⡀⠀⠀⠀⠀⠀⠀⠙⢶⣤⡀⠀⠀⠀⠀⠈⢿⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⡟⠁⠀⠀⣠⢄⣶⣿⠟⠁⠀⠀⠀⠀⢀⣴⠞⠋⠀⣠⠞⠁⠀⣰⠋⠀⣼⠀⠀⢧⡀⠈⠙⢦⡀⠉⠓⠦⣀⡀⠀⠀⠀⠀⠹⣿⣷⣤⢤⡀⠀⠀⠹⣷⡀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⠟⠀⠀⣴⡟⢠⣿⡿⢋⡄⠀⠀⠀⣠⠞⠃⠤⢄⣀⠞⠁⠀⠀⢰⡏⠀⠀⠿⠀⠀⠘⣧⠀⠀⠀⠙⣆⣀⠤⠄⠛⢦⡀⠀⠀⠐⡜⢿⣿⣆⢻⣦⡀⠀⠘⣿⡄⠀⠀⠀
⠀⠀⢀⣾⠏⠀⡠⣸⣿⠇⡾⢋⣴⡟⠀⠀⢠⠞⠃⠀⠀⠀⢠⠟⠙⠒⠒⠤⡞⠀⣤⣤⠶⣤⣤⡀⠘⠀⠐⠒⠊⠙⣧⠀⠀⠀⠀⠙⣄⠀⠀⠹⣶⣝⠻⡄⣿⣷⢠⡀⠘⣿⡄⠀⠀
⠀⠀⣼⠟⠀⣼⠁⣿⡟⣠⣾⣿⠟⠁⠀⡴⠋⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⡇⠀⢻⣿⢶⢸⣿⡇⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠈⢳⡀⠀⠙⢿⣷⣄⢸⣿⡇⣷⡀⠘⣿⡄⠀
⠀⣸⡿⠀⢸⣿⠀⣿⣽⡿⢋⡵⠀⢀⡾⠁⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠹⡄⠀⠸⣏⠿⣷⣿⠃⣿⣷⠀⢹⣧⠀
⠀⣿⠇⠀⣼⣿⡇⣼⢋⣴⡿⠁⠀⡼⠀⠉⠒⠶⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡀⠤⠴⠂⠈⠀⢹⡀⠀⢹⣷⣌⢻⡄⣿⣿⠀⠀⢿⡄
⢸⡟⠀⣴⢹⣿⡇⣱⣿⡿⠁⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢴⣿⡷⠤⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⣻⣿⣷⡀⣿⣿⠀⠀⢸⡇
⢸⡇⠀⣿⠘⣿⣿⣿⠏⣰⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⢻⠙⢿⣧⣿⡇⢠⡇⠀⣿
⣾⠁⠸⣿⡄⠹⡿⠃⣴⡟⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣯⣿⣭⣥⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⣧⠈⢻⡿⠀⣾⡇⠀⣿
⣿⠀⠀⣿⣷⡀⠇⣼⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⡇⠀⢨⣿⣇⠀⠀⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⠀⠸⣿⣷⡈⠇⣼⣿⠇⠀⣿
⢿⡄⢀⢻⣿⣷⢸⣿⡟⢀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⢠⣶⣶⣾⣿⣿⣿⣿⡿⠀⠀⠉⣿⡈⠀⠀⢹⣿⣿⣿⣿⣿⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢠⠸⣿⡇⣰⣿⡿⠀⠀⣿
⢸⡇⢸⡄⠻⣿⣼⣿⠁⣸⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⢰⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⣼⡀⢿⡇⣿⡟⢁⡇⠀⣿
⢸⣧⠀⣿⣄⠘⢿⡟⢠⣿⡇⠀⠹⡆⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⢸⣿⡇⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⢀⡿⠀⢀⣿⡇⢸⣿⠟⢠⣾⠇⢸⡇
⠀⣿⡄⠙⣿⣷⣌⠓⢸⣿⡗⢄⠀⢱⡀⣀⣤⠴⠖⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⢸⣿⡇⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠓⠶⢤⣄⣀⣼⠁⢠⣾⣿⣧⠸⢁⣶⣿⠟⠀⣾⠃
⠀⢹⣷⠀⠈⢿⣿⣷⡸⣿⡇⠘⣦⡀⢣⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣸⠃⣰⡏⢸⣿⡏⣴⣿⣿⠋⠀⣸⡿⠀
⠀⠀⢻⣦⠘⣦⠙⠿⣷⣿⣿⠀⣿⣧⠀⠳⡄⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢀⡼⠁⣰⣿⠁⢸⣟⣼⡿⠛⣁⠇⢠⣿⠃⠀
⠀⠀⠈⢿⣆⠘⢿⣦⣈⠙⠿⣇⢸⣿⣧⢀⠈⠂⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠠⠋⢀⣠⣿⡿⢠⠿⠛⢁⣠⣶⠏⢠⣿⠃⠀⠀
⠀⠀⠀⠈⢿⣆⠈⠻⣿⣷⣶⣬⡀⢻⣿⡎⢳⣄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣠⡶⢋⣿⣿⢁⣡⣴⣶⣿⠿⠃⢠⣾⠋⠀⠀⠀
⠀⠀⠀⠀⠈⢻⣧⡀⠈⢙⠿⣿⣿⣷⣿⣷⡄⢿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢁⣼⣿⣵⣿⣿⠿⢟⠁⠀⣰⣿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣷⣄⠈⢳⣤⣈⣉⠉⠙⠛⠆⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠱⠞⠛⠉⣉⣁⣠⡴⠃⢀⣴⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣶⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣷⣾⣿⣿⣿⣿⣿⠿⠟⠋⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣦⣄⠀⠰⣬⣉⣉⣉⣉⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⣉⣉⣉⣉⣩⠴⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣤⡈⠙⠛⠿⠿⢿⠿⠿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⠿⠿⠿⠿⠟⠛⠁⣠⣶⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣷⣦⣀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⢀⣠⣶⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢶⣤⣄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣤⣴⠾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠟⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

_____ _   _ ____    ____  _____ ____
 | ____| \ | |  _ \  / ___|| ____/ ___|
 |  _| |  \| | | | | \___ \|  _|| |  
 | |___| |\  | |_| |  ___) | |__| |___ 
 |_____|_| \_|____/  |____/|_____\____|

"""

# Função para limpar a tela
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para imprimir o menu
def print_menu():
    print('\033[31m' + art + '\033[0m')
    print('METODOS AND HACKING\n')
    print('[ 1 ] Puxar Dados')
    print('[ 2 ] Desbanir')
    print('[ 3 ] Banir\n')

# Menu para a opção 1
def menu_puxar_dados():
    print('\nPUXAR DADOS\n')
    print('[ 1 ] Puxar Ip')
    print('[ 2 ] Puxar CPF')
    print('[ 3 ] Puxar Dados Bancários')
    print('[ 4 ] Puxar Localização')
    print('[ 5 ] Puxar Placa')
    print('[ 6 ] Voltar')
    print('[ 7 ] Sair')

# Menu para a opção 2
def menu_desbanir():
    print('\nDESBANIR\n')
    print('[ 1 ] Desbanir Perma')
    print('[ 2 ] Desbanir Normal')
    print('[ 3 ] Desbanir Analise')
    print('[ 4 ] Voltar')
    print('[ 5 ] Sair')

# Menu para a opção 3
def menu_banir():
    print('\nBANIR\n')
    print('[ 1 ] Banir Perma')
    print('[ 2 ] Banir Temporario')
    print('[ 3 ] Desativar Number')
    print('[ 4 ] Voltar')
    print('[ 5 ] Sair')

# Loop principal do programa
while True:
    clear()
    print_menu()
    opcao = input('(-) [$] -> ')