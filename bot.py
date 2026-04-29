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
    # Header ditingkatkan agar lebih mirip browser asli (Mises)
    headers = {
        "Host": "viefaucet.com",
        "Connection": "keep-alive",
        "accept": "application/json, text/plain, */*",
        "authorization": bear,
        "user-agent": user_agent,
        "cookie": coockie,
        "origin": "https://viefaucet.com",
        "referer": "https://viefaucet.com/faucet",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    try:
        # Menggunakan session agar koneksi lebih stabil
        r = requests.get(url, headers=headers, timeout=15)
        
        if r.status_code == 200:
            print(f"{Fore.CYAN}[{time.strftime('%H:%M:%S')}] {Fore.GREEN}Claim Berhasil! Saldo Bertambah.")
        elif r.status_code == 429:
            print(f"{Fore.YELLOW}[!] Harap Tunggu, Sedang Cooldown...")
        elif r.status_code == 503 or r.status_code == 403:
            print(f"{Fore.RED}[!] Error {r.status_code}: Terdeteksi Cloudflare/Blokir IP.")
        else:
            # Menampilkan status code asli supaya kita tahu penyakitnya apa
            print(f"{Fore.RED}[!] Error {r.status_code}: Cek kembali Cookie/Token di cfg.py")
            
    except Exception as e:
        print(f"{Fore.RED}[!] Koneksi Terputus... {str(e)}")

banner()
while True:
    claim()
    # Tunggu 61 detik (sesuai permintaan Anda, jangan dikurang)
    time.sleep(61)
