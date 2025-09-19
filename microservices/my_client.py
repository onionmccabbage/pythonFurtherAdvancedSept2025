# client for our microservice
import socket

def client():
    '''simple socket client to consume microservices'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    setup_t = ('localhost', 9876) 
    client.connect(setup_t) # we connect to the server
    # next we can send a byte stream to the server
    client.send(b'some interesting data')
    # we may reasonably expect aa response from the server
    received = client.recv(1024)
    print(f'Client received {received}')
    client.close() # always a good idea to tidy up


if __name__ == '__main__':
    client()