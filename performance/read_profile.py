import pstats

def main():
    '''open a profile report and show the contents'''
    p=pstats.Stats('performance/prof_out') # root-relative address
    p.print_stats() # explore other options

if __name__ == '__main__':
    main()