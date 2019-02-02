
import socket
from base64 import b64decode

from hl7apy import core, parser, UnsupportedVersion

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        client = conn.recv(800000).decode()

        #while (l):
        #    f.write(l)
        #    l = sc.recv(1024)
        if not client:
            # if data is not received break
            break
        print("from connected user: " + client)

        server = input(' -> ')
        if server == "PROCESS":
            print("Procesando HL7...")
            try:
                m = parser.parse_message(client)
            except UnsupportedVersion:
                m = parser.parse_message(client.replace("n", "r"))
            f = open("sendfile.hl7", "w")
            f.write(m.value)
            f.close()
            f1 = open("marainternet.jpg", "w")
            f1.write(m.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_5.value)
            f1.close()
            server = input(' -> ')

        conn.send(server.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
