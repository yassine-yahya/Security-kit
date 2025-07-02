import socket
import threading
from colorama import Fore, Style, init

# Initialize colorama for Windows support
init()

# Global counter for total ports scanned
port_count = 0
lock = threading.Lock()  # Prevent race conditions

def port_scanner(ip, port):
    global port_count  
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((ip, port))
        s.close()
        
        if result == 0:
            print(Fore.GREEN + f"[+] Port {port} is OPEN" + Style.RESET_ALL)
        
    
    except Exception as e:
        print(Fore.YELLOW + f"[!] Error scanning port {port}: {e}" + Style.RESET_ALL)
        with open("results.json", "w") as f:
            json.dump(results, f)

    # Update total ports scanned safely using the lock
    with lock:
        port_count += 1

# Function for fast scanning with threading
def start_scan(ip, ports):
    threads = []
    for port in ports:
        thread = threading.Thread(target=port_scanner, args=(ip, port))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# User input
target_ip = input(Fore.CYAN + "Enter IP Address > " + Style.RESET_ALL)
port_range = range(400, 1025)

print(Fore.MAGENTA + f"\nScanning target {target_ip}...\n" + Style.RESET_ALL)

start_scan(target_ip, port_range)

# Display total ports scanned
print(Fore.BLUE + f"\nTotal ports scanned: {port_count}" + Style.RESET_ALL)
