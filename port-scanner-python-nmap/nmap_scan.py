import nmap
from colorama import Fore, Style, init
init(autoreset=True) 
import time


#intial nmap portScanner()
scanner = nmap.PortScanner()
scanner.scan("scanme.nmap.org", "22,80,443")
print(f"scanning ...")

while True:
#loop for hostname and state of every host scanned
    for host in scanner.all_hosts():
        print(f"{Fore.CYAN}Host: {host} ({scanner[host].hostname()})")
        print(f"{Fore.YELLOW}State: {scanner[host].state()}")
    
#loop for protocols in host and output protocols
    for proto in scanner[host].all_protocols():
        print(f"{Fore.MAGENTA}Protocol: {proto}")
    

#loop for ports and print state of every port of protocol of host => port number selected with .keys()
    ports = scanner[host][proto].keys()
    for port in ports:
        state =scanner[host][proto][port]['state']
        
        if state == "open":
            color = Fore.GREEN
        elif state == "closed":
            color = Fore.RED
        else:
            state == "filtred"
            color = Fore.YELLOW
        print(f"Port : is {color}{state}")
    print("new scan in 5 second..")
        
    time.sleep(5)
            

        

    
    

