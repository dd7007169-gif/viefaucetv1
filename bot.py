import requests
import time
from colorama import Fore, Style, init
from cfg import coockie, user_agent, bear

init(autoreset=True)

def banner():
    print(f"{Fore.YELLOW}==================================")
    print(f"{Fore.GREEN}   BOT VIEFAUCET AKTIF - PAK JOHN")
    print(f"{Fore.YELLOW}==================================")

def claim():
    url = "https://viefaucet.com/api/faucet"
    headers = {
        "Host": "viefaucet.com",
        "authorization": bear,
        "user-agent": user_agent,
        "cookie": coockie
    }
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            print(f"{Fore.CYAN}[{time.strftime('%H:%M:%S')}] {Fore.GREEN}Claim Berhasil! Saldo Bertambah.")
        elif r.status_code == 429:
            print(f"{Fore.YELLOW}[!] Harap Tunggu, Sedang Cooldown...")
        else:
            print(f"{Fore.RED}[!] Error: Cek kembali Cookie/Token di cfg.py")
    except:
        print(f"{Fore.RED}[!] Koneksi Terputus...")

banner()
while True:
    claim()
    # Tunggu 1 menit sebelum claim lagi
    time.sleep(61)
