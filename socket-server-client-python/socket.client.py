import socket

host = "127.0.0.1"
port = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
   
    while True:
        user_input = input("enter message: ")
        s.sendall(user_input.encode())
        
        if user_input == "exit":
            print("client closing connection..")
            break

            
        data = s.recv(1024).decode()
        print(f"server: {data}")
print("client closed.")
