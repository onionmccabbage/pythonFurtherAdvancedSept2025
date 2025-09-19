# a simple microservice
import socket
import threading

# every time we receive from a client, persist this to a byte file
# do this on separate threads
from file_writer import writeBytes


def server():
    '''a simple microservice socket server'''
    # these are common sensible defaults
    server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    # choose a suitable IP address and port
    setup_t = ('localhost', 9876) # localhost maps to 127.0.0.1
    server.bind(setup_t) # here our server is provided with an IP address and port
    # begin listening for clients
    server.listen(4) # this server can handle up to 4 clients at a time
    print(f'Server is listening on {setup_t[0]}:{setup_t[1]}')
    # we need our server to run continuously
    while True: # this will run on the main thread until we terminate the while loop
        # we can handle any client requests
        try:
            (client, addr) = server.accept()
            # print(addr) # the address details of the client
            # the client may send a lot of data. 
            # By convention we examine just the first few bytes
            buffer = client.recv(1024) # receive up to the first 1024 bytes from the client
            # NB our buffer contains bytes (not a plain string)
            buf_str = buffer.decode()
            print(f'Server received {buf_str}') # what do we get...
            # invoke a thread and write the buffer to a byte file
            t = threading.Thread(target=writeBytes, args=(buffer,))
            t.start()
            # no join() so we don't block the main thread
            # provide a mechanism for our server to stop cleanly
            if buffer == b'quit': # b'...' makes a byte string out of text
                break # the while loop will end here
            else:
                # simple echo back what the client sent, forced to upper case
                response = buffer.upper()
                client.send(response)
        except Exception as err:
            print(f'Problem: {err}')


if __name__ == '__main__':
    server()