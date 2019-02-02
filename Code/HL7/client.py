import socket

from Code.HL7.HL7encoder import generarHL7_ORU_R01, generarHL7_ORU_R02


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    #Aquí almacenamos un mensaje:
    client = input(" -> ")  # take input
    messagetype = ""


    while client != 'bye':

        if messagetype == "HL7":
            client_socket.send(client.to_mllp().encode('UTF-8'))  # send message
        else:
            client_socket.send(client.encode())  # send message

        server = client_socket.recv(800000).decode()

        print('Received from server: ' + server)  # show in terminal
        messagetype = ""
        client = input(" -> ")  # again take input
        if client == 'ORU_R02':
            client = generarHL7_ORU_R02()
            messagetype = "HL7"

        elif client == 'ORU_R01':
            client = generarHL7_ORU_R01()
            messagetype = "HL7"

    client_socket.close()  # close the connection
if __name__ == '__main__':
    client_program()
