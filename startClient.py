# check length of the RNA String
def check_len(message):
    if len(message)%3 != 0:
        message = "DISCONNECT"
        print("INVALID RNA LENGTH")
        return message
    else:
        return message

    
# check each nucleotide in RNA String
def check_item(message):
    if message != "DISCONNECT":
        for i in message:
            if i not in ("G","A","C","T"):
                message = "DISCONNECT"
                print("INVALID RNA")
                break
        return message
    else:
        return message
    
    
# Request START RNA message
def start_rna():
    global msg
    msg = "empty"
    begin = "START RNA"
    while True:
            print("ENTER <START RNA> TO BEGIN")
            msg = input("Client: ").upper()
            if msg == begin:
                break
            else:
                print("INCORRECT INPUT, ENTER <START RNA> TO BEGIN")







# Ensure proper message is sent
port = int(input("ENTER THE SAME PORT NUMBER AS THE SERVER: "))
begin = "START RNA"
message = ""





def get_message():
    print("PRESS <ENTER> IN ABSENCE OF A FILE") # get the file or input RNA
    filename = input("ENTER FILENAME: ")
    global message


    if filename:
        with open (filename,"r") as file:
            message = file.readline # read first line of the file
    else:
        print("'Y' to enter RNA \n'N' to exit")
        while True:
            answer = input("Enter (Y/N): ")
            if answer.upper() == 'Y':
                start_rna()
                print("Enter RNA")
                message = input("Client: ").upper() # Ensure uppercase is used for RNA string input
                message = check_len(message)
                message = check_item(message)
                break
            elif answer.upper() == 'N':
                message = "DISCONNECT"
                break
            else:
                print("INCORRECT ENTRY\n'Y' to enter RNA \n'N' to exit")



import socket
HEADER = 64
PORT  =  port
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

    


while True:
    if message != "DISCONNECT":
        get_message()
        send(message)
    else:
        send(message)
        input("<ENTER> TO EXIT")
        break
#get_message()
#send(message)
#input("<ENTER> TO EXIT")