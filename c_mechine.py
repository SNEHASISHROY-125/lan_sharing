'''

'''

import client as c
import bus as bs
import drive as dr

ip_ = str(input('PLEASE ENTER IP ADDRESS TO CONNECT : '))

c.client(ip=ip_)

# send request for dir list
bs.send_(s=c.client_socket,payload='req-dir-list',debug='client')

# recieve directories
dirs = bs.recv_metadata(socket=c.client_socket)

# # create directories
dr.create_directory_ALL(dirs['dirs'])

bs.send_(s=c.client_socket,payload='req-file-send',debug='client')

# # recieve files
for file in dirs['files']:
    bs.send_(s=c.client_socket,payload='file-send-ok',debug='client')
    c.recieve_file(drive=dirs['dirs'][0][0])
    

# print(dirs['dirs'])
# print(dirs['files'])
# c.client_socket.close()
print('client ends here ....')