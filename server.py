'''

'''
import bus as bs
from Btools import Tools as T
import os ,socket

# server:
global port
port = 25200
global client
client = None
# main-loop:
l = T()
l._debug = '(main-loop)'

SPEED_10 = 10485760   # 10MBPS
SPEED_50 = 52428800   # 50MBPS
CURRENT_SPEED = SPEED_10

Q_DICT = {
        'supported_speed'    :   [SPEED_10, SPEED_50],
        'current_speed'    :        CURRENT_SPEED ,
    }

# RETURNS: IP-Address of the WIFI | INTERNAL USE {MULTI-USE}
def get_wifi_ip_address() -> str:
    '''
    Both INTERNAL and EXTERNAL UseCase
    '''
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# INTERNAL USE | SERVER INITIALIZATION
def server():
    
    '''
    DONT CALL THIS FUNCTION MORE THAN ONCE OR DIRECTLY, IF YOU WANT TO EMBED IN GUI USE ```start_server()```
    '''
    global s_socket
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    '''
    Server-Socket, PORT 25200
    '''
    s_socket.bind(
        (get_wifi_ip_address(), port)
        )
    s_socket.listen(5)
    print('SERVER RUNNING AT: ',get_wifi_ip_address(), 'PORT: ',port)

    global client
    client, _ = s_socket.accept()
    '''File_Transfer ,PORT 25200'''


def callback(file_path:str) -> None:

    # for file in _:
    bs.send_(s=client,payload='file-path',debug='server')

    msgg = bs.recv_(s=client,debug='server',e=['file-path-ok'],e_=str,)

    l.print_((bs.send_file(file_path=file_path,client=client, speed_=Q_DICT['current_speed']),)) 
    # l.print_((os.path.basename(file),'done!',))
    l.print_(('sync-end',))

##
# server()
# callback(file_path='C:\\Python312\\tcl\\tclooConfig.sh')

# s_socket.close()