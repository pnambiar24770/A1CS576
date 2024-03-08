import socket  

#function to encode a message by shifting each character by 1
def encode_message(message):
    return ''.join(chr((ord(char) + 1) % 256) for char in message)

#function to run the server
def server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #create socket object 
        s.bind((host, port)) #bind the socket to host and port
        s.listen() #server is listening
        print(f"Server listening on {host}:{port}") #debug msg
        try:
            while True: #keep server on
                conn, addr = s.accept() #accept a new connection
                with conn:  
                    print(f"Connected by {addr}") #debug msg with connection
                    while True:  
                        data = conn.recv(256) #receive data
                        if not data: #check if no data is received
                            break #exit if no data is received
                        #encode the received message and send it back to the client
                        encoded_message = encode_message(data.decode())
                        conn.sendall(encoded_message.encode())
        except KeyboardInterrupt: #handle KeyboardInterrupt exception to shut server down
            print("Server is shutting down.") #print a message indicating server shutdown

if __name__ == "__main__": #run script directly
    server()  
