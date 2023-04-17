def generator(params = {}):
    if 'special' in params:
        print('special chars')
    if 'upperlower' in params:
        print('upperlower letters')
    if 'number' in params:
        print('numbers')
    return 'generated'