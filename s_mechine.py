'''

'''
import bus , server as s
import drive as dr 
DRIVE = str(input('PLEASE ENTER DRIVE NAME [CAPITAL]: like C:\\xampp :  ' ))
DESTINATION = str(input('PLEASE ENTER DESTINATION PATH: like D:\\drive_c\\ :  '))

# get all directories and files as list
_ = dr.replicate_tree(DRIVE,DESTINATION)
print(_)
# loop :
s.server()

# wait for client request
# recieve request
# send directories to client
bus.recv_(s=s.client,debug='server',e=['req-dir-list'],e_=str)

# send directories to client    -- c_mechine.py recives directories list
re_ = bus.send_metadata(
    socket=s.client,
    meta= {'dirs':_[0],'files':_[1]},
    )
# dr.create_directory(_[0])     -- c_mechine.py creates directories

bus.recv_(s=s.client,debug='server',e=['req-file-send'],e_=str)

# send files to client
# server()
for file in _[1]:
    bus.recv_(s=s.client,debug='server',e=['file-send-ok'],e_=str)
    s.callback(file_path=file)

# s.s_socket.close()
print('server ends here ....', re_)