# Installation
1. Extract all files from the zip file
2. Ensure all files are placed in the same directory folder
3. Place the "codon-aminoacid.csv" file in the same same directory aswell
4. Run the server.py and provide a port number as requested
5. Run the client.py and provide the same port number as provided in the server.py startup
    * Follow the instruction requested from the operation to get the desirable output

# Content
1. server.py
2. client.py
3. info
4. Rules
5. codon-aminoacid.csv

## server.py
#### Operations
1. This creates a server on a host computer by binding a port number supplied by the server operator to an IP address
2. It listens and accepts connection from different clients
3. It receives encoded message from different clients
    * These messages are RNA strings
4. These messages are decoded and:
    * If a valid RNA string is provided, it is optimized, then encoded and sent back to the client where it is later decoded
    * If an invalid RNA string is provide, the client is disconnected from the server
5. The client can also manually disconnect from the server

### Funcions
#### get_csv(data)
1. This imports the python csv library and takes a csv file (data) as an argument
2. It takes the codon columns and stores all its items in a list
3. It takes all items in the amino acid column and stores it in seperate list

#### optimize(input)
1. It takes in an input RNA supplied by the client and breaks it up into a group of 3
2. It checks if each group is contines in a reference codon list created from the [get_csv(data)] function
    * Returns "DISCONNECT" (an error) if its not contained in the reference list.
    * It gets the amino acid of codon if it is contained in the reference list
3. Replaces original codon with a new codon that can be mapped to the same amino acid of the original codon

#### start()
1. This listens to connection from any client attempting to connect to the server
2. Keeps the server open to multiple connection from clients and calls the [handle_client(conn,addr)] function on all incomming client connections

#### handle_client(conn, addr)
1. This contains the all operations that should be performed on the message sent from the client
2. It calls other operational function and applies them to message from any client provided there is an established connection


## client.py
### Operations
1. This establishes a connection with the server on the same port provided by the client user
2. The connection is created by connecting the client IP address to the server port
3. The client is provided with the option to supply a file where the RNA can be read from
    * If the file is provided, the first line of the file is stored as the message to be sent to the server
    * If the file is not provided, the user can either exit the connection or provide the RNA string to be sent to the server
4. The length of the message to be sent is checked and the appropriate result is generated
5. The characters in the message is also checked to ensure they are the appropriate characters
6. The message is then sent to the client
7. All errors generated while collecting the message changes the message content to "DISCONNECT" which disconnects the client from the server when sent. 

### Functions
#### check_len(message)
1. This takes in the message the client intends to send to the server as an argument
    * Message is a string of RNA
2. This checks the length of the message and ensures that it is a multiple of 3
    * i.e., the modulus of the sum of the nucleotide must be zero(0)
        * If it is "0", it returns the inputed RNA string as an output
        * If it is not "0", it changes the RNA string to "DISCONNECT"
            * Clients will disconnect from the server if it sends a "DISCONNECT" message
            
#### check_item(message)
1. This takes the RNA string input provided by the client and checks if each character is either a "G", "A", "T" or "C"
2. Provided a single nucleotide is none of the restricted character, the entire message changes to "DISCONNECT"

#### send(msg)
1. This is usedd to send and receive messages from the client
2. WHat ever message is to be sent is encoded and the length of the message is also encoded and padded to a given length
3. The length is then sent followed by the message and the client receives a reply which is then decoded

## info
This gives the complete information about the code, functions and describes their operations
