from colorama import Fore, init
import os
import time


init(autoreset=True)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def new_title(title):
    os.system(f'title {title}' if os.name == 'nt' else f'echo -n -e "\033]0;{title}\007"')


ascii_art = f"""
{Fore.LIGHTCYAN_EX}
             
             ██ ▄█▀ ██▓ ██▓       ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
             ██▄█▒ ▓██▒▓██▒       ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
             ▓███▄░ ▒██▒▒██░       ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
             ▓██ █▄ ░██░▒██░       ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
             ▒██▒ █▄░██░░██████▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
             ▒ ▒▒ ▓▒░▓  ░ ▒░▓  ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
             ░ ░▒ ▒░ ▒ ░░ ░ ▒  ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
             ░ ░░ ░  ▒ ░  ░ ░        ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
             ░  ░    ░      ░  ░                ░ ░      ░ ░      ░  ░      ░  
                                                                  

{Fore.RESET}
"""

color = Fore.LIGHTCYAN_EX

def formater():
    print("Token Formatter selected")
    time.sleep(1)

def Token_checker():
    print("Token Checker selected")
    time.sleep(1)

def sort_tokens():
    print("Token Sorter selected")
    time.sleep(1)

def main():
    new_title("ki1L MultiTool │ Page 1")
    clear()
    print(ascii_art) 
    print(f"""
                    {color}<<{Fore.RESET}1{color}>> [{Fore.RESET}Token Formatter{color}]        {color}<<{Fore.RESET}8{color}>>  [{Fore.RESET}Proxy Scraper{color}]         {color}<<{Fore.RESET}15{color}>>  [{Fore.RESET}Token Mail Verifier{color}]
                    {color}<<{Fore.RESET}2{color}>> [{Fore.RESET}Token Checker{color}]         {color}<<{Fore.RESET}9{color}>>  [{Fore.RESET}Proxy Checker{color}]         {color}<<{Fore.RESET}16{color}>>  [{Fore.RESET}Token Pass Changer{color}]
                    {color}<<{Fore.RESET}3{color}>> [{Fore.RESET}Token Sorter{color}]          {color}<<{Fore.RESET}10{color}>> [{Fore.RESET}Webhook Tool{color}]          {color}<<{Fore.RESET}17{color}>>  [{Fore.RESET}Token Onliner{color}]
                    {color}<<{Fore.RESET}4{color}>> [{Fore.RESET}Token Spammer{color}]         {color}<<{Fore.RESET}11{color}>> [{Fore.RESET}Faker Tool{color}]            {color}<<{Fore.RESET}18{color}>>  [{Fore.RESET}Token Status Rotator{color}]
                    {color}<<{Fore.RESET}5{color}>> [{Fore.RESET}Token Guild Checker{color}]   {color}<<{Fore.RESET}12{color}>> [{Fore.RESET}Obfuscator{color}]            {color}<<{Fore.RESET}19{color}>>  [{Fore.RESET}Token Nuker{color}]
                    {color}<<{Fore.RESET}6{color}>> [{Fore.RESET}Token Guild Leaver{color}]    {color}<<{Fore.RESET}13{color}>> [{Fore.RESET}Clear Output Folder{color}]   {color}<<{Fore.RESET}20{color}>>  [{Fore.RESET}Token Editor{color}]
                    {color}<<{Fore.RESET}7{color}>> [{Fore.RESET}Remove Duplicates{color}]     {color}<<{Fore.RESET}14{color}>> [{Fore.RESET}Clear Input Folder{color}]    {color}<<{Fore.RESET}21{color}>>  [{Fore.RESET}Nitro Gift Checker{color}]
    """)
    choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice: ")
    functions = {
        "1": formater,
        "2": Token_checker,
        "3": sort_tokens,
        
    }
    function = functions.get(choice)
    if function:
        function()
    else:
        print("Invalid choice")
        time.sleep(1)
    main()


os.system("mode con cols=135 lines=24")
main()
