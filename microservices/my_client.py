# client for our microservice
import socket
import sys

# mini-challenge
# within the client, see if any additional sys.argv were sent
# if so, use them as the message to send to the server


def client():
    '''simple socket client to consume microservices'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    setup_t = ('localhost', 9876) 
    try:
        client.connect(setup_t) # we connect to the server
        # next we can send a byte stream to the server
        if len(sys.argv) >1:
             msg = ', '.join(sys.argv[1:])
        else:
             msg = 'default message'
        client.send(msg.encode())
        # we may reasonably expect aa response from the server
        received = client.recv(1024)
        print(f'Client received {received}')
        client.close() # always a good idea to tidy up
    # A good idea to handle different tyopes of exception
    except ConnectionAbortedError as err: # start with specific exceptions
         pass
    except ConnectionRefusedError as err:
         pass
    except ConnectionError as err:
         pass
    except Exception as err:
            print(f'Problem: {err}')


if __name__ == '__main__':
    client()