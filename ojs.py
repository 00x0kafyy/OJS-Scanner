import requests, concurrent.futures
from urllib.parse import urljoin
from colorama import Fore, init
import os, pyfiglet, time

init(autoreset=True)

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    ascii_banner = pyfiglet.figlet_format("OJS Scanner")
    print(Fore.GREEN + ascii_banner)
    print(Fore.LIGHTBLACK_EX + "  Scanner Directory Open Journal Systems | by @yourdre4m7")
    print(Fore.LIGHTBLACK_EX + "=" * 65)

def load_file(path):
    with open(path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def save_result(filename, url):
    with open(filename, 'a') as f:
        f.write(url + "\n")

def scan_path(target, paths, protocol):
    for path in paths:
        full_url = f"{protocol}://{target}{path}"
        try:
            r = requests.get(full_url, timeout=10)
            if r.status_code == 200:
                if "Index of" in r.text:
                    print(Fore.GREEN + f"[+] OPEN DIR : {full_url}")
                    save_result("open_dir.txt", full_url)
                else:
                    print(Fore.BLUE + f"[+] 200 OK     : {full_url}")
                    save_result("valid_path.txt", full_url)
            elif r.status_code == 403:
                print(Fore.YELLOW + f"[!] 403 Forbidden : {full_url}")
                save_result("forbidden.txt", full_url)
            elif r.status_code == 404:
                pass  # silent
            else:
                print(Fore.MAGENTA + f"[?] {r.status_code} Unknown : {full_url}")
        except requests.RequestException:
            print(Fore.RED + f"[x] ERROR       : {full_url}")

def run_scan():
    banner()
    list_file = input(Fore.LIGHTBLACK_EX + "Target List File     >>> ").strip()
    path_file = input(Fore.LIGHTBLACK_EX + "Path List File       >>> ").strip()
    proto_input = input(Fore.LIGHTBLACK_EX + "Use HTTPS? (y/n)     >>> ").lower().strip()
    protocol = "https" if proto_input == "y" else "http"

    try:
        targets = load_file(list_file)
        paths = load_file(path_file)
    except Exception as e:
        print(Fore.RED + f"[ERROR] Failed to load files: {e}")
        return

    print(Fore.CYAN + f"\n[+] Starting scan for {len(targets)} targets with {len(paths)} paths using {protocol.upper()}...\n")
    start = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        for target in targets:
            executor.submit(scan_path, target, paths, protocol)

    elapsed = time.time() - start
    print(Fore.GREEN + f"\n[✓] Scan completed in {elapsed:.2f} seconds.\n")

if __name__ == "__main__":
    run_scan()
