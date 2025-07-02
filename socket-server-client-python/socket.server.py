
import socket
host = "0.0.0.0"
port = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print("Server is listening")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()
            if not data:
                print("client disconnected")
                break
            
            print(f"Client: {data}")
            server_input = input("enter message: ")
            conn.sendall(server_input.encode())
            
            if server_input.lower() == "exit":
                print("Server shutting down...")
                break
    
            

print("Sever Closed")