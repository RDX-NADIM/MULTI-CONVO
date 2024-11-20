import requests
import time
import os
from colorama import init, Fore, Style

init(autoreset=True)


def approval():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def raj_logo():
    logo = r"""
\033[1;36m$$$$$$$\   $$$$$$\     $$$$$\ 
\033[1;36m$$  __$$\ $$  __$$\    \__$$ |
\033[1;34m$$ |  $$ |$$ /  $$ |      $$ |
\033[1;34m$$$$$$$  |$$$$$$$$ |      $$ |
\033[1;36m$$  __$$< $$  __$$ |$$\   $$ |
\033[1;32m$$ |  $$ |$$ |  $$ |$$ |  $$ |
\033[1;33m$$ |  $$ |$$ |  $$ |\$$$$$$  |
\033[1;33m\__|  \__|\__|  \__| \______/ 
"""
    print(Fore.MAGENTA + Style.BRIGHT + logo)


def fetch_profile_name(access_token):
    """Fetch the profile name using the token"""
    try:
        response = requests.get("https://graph.facebook.com/me", params={"access_token": access_token})
        response.raise_for_status()
        return response.json().get("name", "Unknown")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[x] Failed to fetch profile name for token. Error: {e}")
        return "Unknown"


def fetch_target_name(target_id, access_token):
    """Fetch the target profile name using the target ID and token"""
    try:
        response = requests.get(f"https://graph.facebook.com/{target_id}", params={"access_token": access_token})
        response.raise_for_status()
        return response.json().get("name", "Unknown Target")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[x] Failed to fetch target name. Error: {e}")
        return "Unknown Target"


def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = [token.strip() for token in file.readlines()]

    # Fetch the profile name for each token
    token_profiles = {token: fetch_profile_name(token) for token in tokens}

    # Fetch the target profile name
    target_profile_name = fetch_target_name(target_id, tokens[0])  # Using the first token for the target fetch

    headers = {
        "User-Agent": "Mozilla/5.0",
    }

    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            access_token = tokens[token_index]
            sender_name = token_profiles.get(access_token, "Unknown Sender")
            full_message = f"{haters_name} {message.strip()}"

            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}
            try:
                response = requests.post(url, json=parameters, headers=headers)
                response.raise_for_status()
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                print(Fore.GREEN + f"\n┌────────────────────────────────────────────────────────────────────┐")
                print(Fore.CYAN + f"[✔] {Fore.YELLOW}Message {message_index + 1} Successfully Sent!")
                print(Fore.CYAN + f"[👤] Sender: {Fore.MAGENTA}{sender_name}")
                print(Fore.CYAN + f"[📩] Target: {Fore.MAGENTA}{target_profile_name} ({target_id})")
                print(Fore.CYAN + f"[📨] Message: {Fore.LIGHTGREEN_EX}{full_message}")
                print(Fore.CYAN + f"[⏰] Time: {Fore.LIGHTBLUE_EX}{current_time}")
                print(Fore.GREEN + f"└────────────────────────────────────────────────────────────────────┘\n")
                print(Fore.YELLOW + "\033[1;32m<<========❌✨🌐 OWNER RAJ 😏⚔️⚜️🫢 THAKUR ✨❌✨🌐😈🛠️✨======>>")
                print("\n" + ("─" * 80) + "\n")
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"\n[x] FAILED to send message {message_index + 1}. Error: {e}")
            time.sleep(speed)
        print(Fore.CYAN + "\n[+] All messages sent. Restarting the process...\n")


def main():
    approval()
    raj_logo()
    print(Fore.MAGENTA + " \033[1;37m 🕊️❣️<<•BROKEN💫NADIM•>>🕊️❣️ NAM TO YAD HOGA")
    tokens_file = input(Fore.GREEN + "[+] ENTER-THE-TOKENS-FILE=>> ").strip()
    target_id = input(Fore.YELLOW + "[+] ENTER-THE-TARGET-ID=>> ").strip()
    messages_file = input(Fore.YELLOW + "[+] ENTER-----GALI-FILE=>> ").strip()
    haters_name = input(Fore.YELLOW + "[+] ENTER-HATER-NAME=>> ").strip()
    speed = float(input(Fore.GREEN + "[+] ENTER THE SPEED (IN SECONDS) BETWEEN MESSAGES=>> ").strip())

    send_messages(tokens_file, target_id, messages_file, haters_name, speed)


if __name__ == "__main__":
    main()
