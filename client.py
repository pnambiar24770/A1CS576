import socket

def client(server_host='127.0.0.1', server_port=65432): #client function
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #socket object
        s.connect((server_host, server_port)) #connect to server
        try: 
            while True: 
                message = input("Enter a message to encode (type 'exit' to quit): ") #ask user to enter msg
                if message == 'exit': #check if the input message is 'exit'
                    break #exit
                s.sendall(message.encode()) #encode the message
                data = s.recv(256) #receive the encoded message
                print(f"Received encoded message: {data.decode()}") #print the msg
        except KeyboardInterrupt: #handle KeyboardInterrupt exception
            print("\nClient is shutting down.") #shut down message

if __name__ == "__main__": #run script directly
    client()  
