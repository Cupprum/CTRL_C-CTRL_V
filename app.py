import threading
from threading import Thread
import time
import socket
import signal
import clipboard
from tkinter import *
from tkinter.ttk import *


def prijmaclient(client):
    while True:
        a = client.recv(4096)
        a = a.decode('utf-8')
        pokus = str(a)
        pokus = pokus.lstrip('b')
        pokus = pokus.strip("'")
        print('\n')
        print(pokus)
        clipboard.copy(pokus)
        time.sleep(5)

def posielaclient(client):
    staracopy = clipboard.paste()
    while True:
        novacopy = clipboard.paste()
        if novacopy == staracopy:
            pass
        else:
            staracopy = novacopy
            client.sendall(novacopy.encode('utf-8'))
        time.sleep(5)

def startserver():
    try:
        ip = entry_ip.get()
        port = entry_port.get()
        server = socket.socket()
        host = str(ip)
        port = int(port)
        server.bind((host, port))
    except:
        host = '192.168.1.111'
        port = 8787
        server.bind((host, port))
        print('except')
    server.listen()
    client, addr = server.accept()
    print('Got connection from', addr)        
    Thread(target = prijmaclient, args=[client]).start()
    Thread(target = posielaclient, args=[client]).start()

def prijmaserver(server):
    while True:
        a = server.recv(4096)
        a = a.decode('utf-8')
        pokus = str(a)
        pokus = pokus.lstrip('b')
        pokus = pokus.strip("'")
        print('\n')
        print(pokus)
        clipboard.copy(pokus)
        time.sleep(5)

def posielaserver(server):
    staracopy = clipboard.paste()
    while True:
        novacopy = clipboard.paste()
        if novacopy == staracopy:
            pass
        else:
            staracopy = novacopy
            server.sendall(novacopy.encode('utf-8'))
        time.sleep(5)

def connecttoserver():
    server = socket.socket()
    try:
        ip = entry_ip.get()
        port = entry_port.get()
        server = socket.socket()
        host = str(ip)
        port = int(port)
        server.connect((host, port))
    except:
        host = '192.168.1.111'
        port = 8787
        server.connect((host, port))
        print('except')
    Thread(target = prijmaserver, args=[server]).start()
    Thread(target = posielaserver, args=[server]).start()

if __name__ == '__main__':
    print(socket.gethostbyname(socket.gethostname()))
    master = Tk()
    # quit

    button_quit = Button(master, text='Quit', command=master.quit)
    button_quit.grid(row=0, column=0, sticky=W, pady=4)
    
    # IPv4 adress
    
    nazov_print_IPv4 = Label(master, text='Tvoja Ip adresa : ' + socket.gethostbyname(socket.gethostname()))
    nazov_print_IPv4.grid(row=0, column=1, sticky=W, pady=4)
    
    
    # Connect

    nazov_ip = Label(master, text='Ip Serveru: ')
    nazov_ip.grid(row=1, column=0, sticky=W, pady=4)
    entry_ip = Entry(master)
    entry_ip.grid(row=1, column=1, sticky=W, pady=4)
    nazov_port = Label(master, text='Port: ')
    nazov_port.grid(row=2, column=0, sticky=W, pady=4)
    entry_port = Entry(master)
    entry_port.grid(row=2, column=1, sticky=W, pady=4)
    button_start = Button(master, text='Start Server', command=startserver)
    button_start.grid(row=3, column=0, sticky=W, pady=4)
    button_connect = Button(master, text='Connect to Server', command=connecttoserver)
    button_connect.grid(row=3, column=1, sticky=W, pady=4)

    mainloop( )
    tApp().run()
