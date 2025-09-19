def writeBytes(n):
    '''persist the bytes 'n' to a byte file'''
    with open('my_bytes', 'ab') as fout: # 'ab' will append to a byte file
        if type(n)==bytes:
            fout.write(n)
            # we may choose to add a termination character
            fout.write('\n'.encode())
        else:
            fout.write(n.encode())