# get ref csv

def get_csv(data):
    import csv
    global codon
    global a_acid
    codon=[]
    a_acid=[]
    with open(data) as csv_file:#this will open the txt doc and store the 2nd row elements.sice first row is just heading
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:#for column row. it just passes
            if line_count == 0:
                line_count += 1
            else:
                codon.append(row[0])
                a_acid.append(row[1])

                

                
def optimize(input):
    x = int(len(input) / 3)
    for i in range(x):
        x = i + 1
        if (input[i * 3:(x * 3)] not in codon):
            return "DISCONNECT"


    change=input[0:3]
    message = input[0:3]
    acid = ''
    for i in range(len(codon)):
        if (codon[i] == message):
            acid = a_acid[i]
    for i in range(len(a_acid)):
        if (a_acid[i]==acid and codon[i] != message):
            message = codon[i]
            message = message[::-1]
            break
    return input.replace(change,message)





# server

import socket
import threading

port = int(input("ENTER PORT NUMBER: "))

HEADER = 64
PORT  =  port
SERVER = socket.gethostbyname(socket.gethostname()) #or ""
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected")
    
    connected = True
    while  connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                conn.close()
            else:
                get_csv("codon-aminoacid.csv")
                msg = optimize(msg)
                if msg == "DISCONNECT":
                    conn.send("CODON NOT CONTAINED IN FILE".encode(FORMAT))
                    conn.close()
                else:
                    conn.send(f"Client: {msg}".encode(FORMAT))
                
            
            print(f"[{addr}] {msg}")
            #conn.send("\nMsg received".encode(FORMAT))
            
    #conn.close()
    

        
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting....")
start()
