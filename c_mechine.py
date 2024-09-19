'''

'''

import client as c
import bus as bs
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
file_path = f'.\\logs\\C\\{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_console_output.txt'
directory = os.path.dirname(file_path)

# Create the directory structure if it doesn't exist
os.makedirs(directory, exist_ok=True)

# Open the log file
with open(file_path, 'w') as f:
    # Redirect stdout to both the console and the file
    original_stdout = sys.stdout
    sys.stdout = Tee(sys.stdout, f)

    try:
        ip_ = str(input('PLEASE ENTER IP ADDRESS TO CONNECT : '))

        c.client(ip=ip_)

        # send request for dir list
        bs.send_(s=c.client_socket,payload='req-dir-list',debug='client')

        # recieve directories
        dirs = bs.recv_metadata(socket=c.client_socket)

        # # create directories
        # dr.create_directory_ALL(dirs['dirs'])     --- obsolete

        bs.send_(s=c.client_socket,payload='req-file-send',debug='client')

        # # recieve files
        for file in dirs['files']:
            bs.send_(s=c.client_socket,payload='file-send-ok',debug='client')
            c.recieve_file(drive=dirs['drive'])
            

        # print(dirs['dirs'])
        # print(dirs['files'])
        # c.client_socket.close()
        print('client ends here ....')
    
    except Exception as e:
        print(e)
    finally:
    # Restore stdout to its original state
        sys.stdout = original_stdout