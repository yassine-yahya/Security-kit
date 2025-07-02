import paramiko
import socket
from colorama import Fore, Style, init

init(autoreset=True)

def sshConnect(hostname, username,password):
#set credentials for target
    

#create ssh client
    ssh = paramiko.SSHClient()

    #set missing hosts keys
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
    #connect ssh
        print(f"{Fore.YELLOW}Connecting to Hostname:  {hostname}  ...")
        ssh.connect(hostname, username=username, password=password, timeout=5)
        
       
        stdin, stdout, stderr = ssh.exec_command("whoami")
        print(f"{Fore.GREEN}✅ [+]  Connected to {hostname} {Style.RESET_ALL}")
        print("Running command:")
        print(f"{Fore.CYAN}> whoami:")
        print(stdout.read().decode())
        ssh.close()
    
        

    #handle exception and error
    except paramiko.AuthenticationException as e:
        print(f"Authentication error: {e}")
    except paramiko.SSHException as e:
        print(f"SSH error: {e}")
        
    except socket.timeout:
        print(f"{Fore.RED} connection Timeout, SSH Blocking")
        
    except paramiko.ssh_exception.NoValidConnectionsError:
        print(f"{Fore.RED} [-] Unable to connect to {hostname}. SSH might be disabled or the port is closed.")
        
        

hostname = input("Hostname : ")
username = input("Username : ")
password = input("Password : ")




sshConnect(hostname, username,password)