import os
import time

# Função para limpar a tela
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Arte ASCII e menu
art = """
 __   ___  __   __        __        __   __   __  
|  \ |__  |__) |__) |  | |__)  /\  |  \ /  \ |__) 
|__/ |___ |  \ |  \ \__/ |__) /~~\ |__/ \__/ |  \ 
                                                  
 __   ___                                         
|  \ |__                                          
|__/ |___                                         
                                                  
   __                                             
| |__)                                            
| |                                               
                                                  
 __                                               
|__) \ / .                                        
|__)  |  .                                        
                                                  
 ___       __   __   ___  __                      
|__  |\ | |  \ /__` |__  /  `                     
|___ | \| |__/ .__/ |___ \__,                     
"""

menu = """
______________________________________________
{art}
| - [ 1 ] Derrubar Ip Net
----------------------------------
| - [ 2 ] Derrubar Ip Site
----------------------------------
| - [ 3 ] Rastrear Ip
----------------------------------
| - [ 4 ] Info Ip
---------------------------------
| - [ 5 ] ddos Ip Net
---------------------------------
| - [ 6 ] Sair do Script
---------------------------------
| - [ 7 ] Instalar Dependências
______________________________________________

------------|
| - [ # ] => 
-------------|
"""

# Loop principal do programa
while True:
    opcao = input("Digite uma opção: ")
    
    # Verifica se a opção é sair
    if opcao == "sair":
        break
    
    # Verifica se a opção é válida
    if opcao in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        # Limpa a tela e exibe a arte ASCII e o menu novamente
        clear_screen()
        print(art + menu)

        # Verifica se o usuário escolheu a opção de sair
        if opcao == "6":
            # Sai do loop
            break
        elif opcao == "7":
            # Instala as dependências
            os.system("pkg update && pkg upgrade")
            os.system("pkg install pip")
            os.system("pip install ngrok")
            os.system("pkg install pip2")
            input("Dependências instaladas. Pressione Enter para continuar.")
            clear_screen()
            print(art + menu)
        elif opcao == "8":
            # Limpa a tela e exibe a arte ASCII e a mensagem de atualização
            clear_screen()
            print(art)
            print("Procurando atualizações...")
            
# Loop giratório enquanto procura atualizações
while True:
    print("/", end="", flush=True)
    time.sleep(0.1)
    print("\b", end="", flush=True)

    # TODO: Inserir código para verificar atualizações no GitHub e atualizar o script
    # Aqui apenas simulamos uma verificação de atualização
    if input("Deseja atualizar o script? (s/n) ") == "s":
        os.system("git pull origin main")
        print("Script atualizado com sucesso. Reinicie o programa.")
        time.sleep(2)
        break

# Limpa a tela e exibe a arte ASCII e o menu novamente
clear_screen()
print(art + menu)
