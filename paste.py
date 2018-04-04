import clipboard

def printcopy():
    informacia = clipboard.paste()
    print(informacia)

def setpaste():
    paste = input()
    clipboard.copy(paste)


print('printcopy or setpaste')
blbost = input()
if blbost == 'printcopy':
    printcopy()
elif blbost == 'setpaste':
    setpaste()


    '''
    staracopy = clipboard.paste()
    while True:
        novacopy = clipboard.paste()
        if novacopy == staracopy:
            pass
        else:
            staracopy = novacopy
            client.sendall(novacopy.encode())
        time.sleep(5)'''