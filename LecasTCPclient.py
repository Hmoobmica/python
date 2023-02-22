import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # IP and port server listens to.  
    server.bind((IP, PORT))
        #max amount of backlogs = 5
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}') 
   
    while True:
        # When a client connects we get the client socket in the client variable and the remote connection details in the address variable
       client, address = server.accept()
       print(f'[*] Accepted connection from {address[0]}:{address[1]}')
       client_handler = threading.Thread(target=handle_client, args=(client,))
       client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
 main()
