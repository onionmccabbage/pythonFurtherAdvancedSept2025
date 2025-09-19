# client for our microservice
import socket

def client():
    '''simple socket client to consume microservices'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    setup_t = ('localhost', 9876) 
    client.connect(setup_t) # we connect to the server
    # next we can send abyte stream to te server
    client.send(b'Hello from client')


if __name__ == '__main__':
    client()