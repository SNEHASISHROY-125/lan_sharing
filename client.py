'''

'''
import socket, os, bus as bs
from Btools import Tools as T

# ip_ = str(input("connect IP:"))
# server_ip = ip_

# # server_ip = '192.168.1.2'  # Replace with the server's IP address
# server_port = 25200  # Replace with the server's port number
# main-loop:
c = T()
c._debug = 'c-main-loop'
SAVE_DIR = ''

# ONE-TIME-USE | CLIENT INITIALIZATION
def client(ip:str,port:int=25200):

    '''
    ``dont call this function more than once or directly, if you want to embed in gui use start_client()``
    '''
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    '''File_Transfer ,PORT 25200'''
    client_socket.connect((ip, port))

def recieve_file(drive:str):
    '''
    - recv-file from server
    '''

    msgg = bs.recv_(s=client_socket,debug='client',e=['req-file-path','close-ok','file-path'],e_=str)    # prepare for recv-file
    print('[FROM:lin 57] llop',msgg)

    if msgg == 'file-path':
        # print(os.getcwd())
        bs.send_(s=client_socket,payload='file-path-ok',debug='client',)    # all resources prepared, ready to recv-file!
        # for file in msgg:
        c.print_((bs.receive_file(client_socket=client_socket,drive_=drive),),s='client',)

# client(ip='192.168.1.5',)
# recieve_file('D')