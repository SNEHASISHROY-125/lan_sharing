'''

'''
import bus , server as s
import drive as dr 
import sys
import os
import datetime

class Tee:
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()  # Ensure the output is written immediately

    def flush(self):
        for f in self.files:
            f.flush()

# Create the log file path
file_path = f'.\\logs\\S\\{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_console_output.txt'
directory = os.path.dirname(file_path)

# Create the directory structure if it doesn't exist
os.makedirs(directory, exist_ok=True)


# Open the log file
with open(file_path, 'w') as f:
    # Redirect stdout to both the console and the file
    original_stdout = sys.stdout
    sys.stdout = Tee(sys.stdout, f)

    try:

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
            meta= {
                'files':_[1],
                'drive':DESTINATION
            }
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

    except Exception as e: 
        print(e)

    finally:
        # Restore stdout to its original state
        sys.stdout = original_stdout