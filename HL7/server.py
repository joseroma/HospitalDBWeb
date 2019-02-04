import socket
import base64
from hl7apy import parser, UnsupportedVersion
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


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
            f = open("recivedData/message.hl7", "w")
            f.write(m.value)
            f.close()

            if m.msh.msh_3.value == "img":
                file_like = m.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_5.value
                f1 = open("recivedData/hl7image.jpg", "wb")
                f1.write(base64.b64decode(str.encode(file_like)))
                f1.close()
            elif m.msh.msh_3.value == "text":
                f1 = open("recivedData/hl7owl.owl", "w")
                f1.write(m.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_5.value)
                f1.close()
            else:
                print("No se pudo procesar. El archivo enviado por HL7 no corresponde con img o text.")

            server = input(' -> ')

        conn.send(server.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
