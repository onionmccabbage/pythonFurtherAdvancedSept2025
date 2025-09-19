def writeBytes(n):
    '''persist the bytes 'n' to a byte file'''
    with open('my_bytes', 'ab') as fout: # 'ab' will append to a byte file
        if type(n)==bytes:
            fout.write(n)
        else:
            fout.write(n.encode())