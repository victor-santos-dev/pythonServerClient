import socket
import sys

class MainServer():

    server_host = 'localhost'
    server_port = 8080

    def __init__(self):

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            


    def start_connection(self):
        
        self.server.bind((self.server_host,self.server_port))
        self.server.listen(1)

        while True:

            print('Waiting client connect')
            connection , client_address = self.server.accept()
            try:
                print('connection from', client_address)

                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(16)
                    print('received {!r}'.format(data))
                    if data:
                        print('sending data back to the client')
                        connection.sendall(data)
                    else:
                        print('no data from', client_address)
                        break

            finally:
                # Clean up the connection
                connection.close()

if __name__ == '__main__':

    server = MainServer()
    server.start_connection()

