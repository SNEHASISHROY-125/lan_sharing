
import socket, threading , time

def get_wifi_ip_address() -> str:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    if ip_address == '172.29.160.1': return 'LOCAL_HOST'
    else:return ip_address

# print('from test.py',get_wifi_ip_address())

# str_ = 'hello'
# def prinT():
#     while True:
#         time.sleep(2)
#         print(str_)

# th1 = threading.Thread(target=prinT)
# th1.start()

# while True:
#     str_ = input('Enter: ')

# prinT()
# th1.
# import server as s


# # def call_func(f='file'):
# #     print('called call_back_func! {}'.format(f))

# # s.memry_dict['callback_func'] = call_func
# s.start_server()

'''
import threading
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class ScreenOne(Screen):
    def __init__(self, **kwargs):
        super(ScreenOne, self).__init__(**kwargs)
        self.add_widget(Label(text='Screen One'))
        self.add_widget(Button(text='Go to Screen Two', on_press=self.change_screen))

    def change_screen(self, instance):
        self.manager.current = 'screen_two'

class ScreenTwo(Screen):
    def __init__(self, **kwargs):
        super(ScreenTwo, self).__init__(**kwargs)
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text='Screen Two'))
        box.add_widget(Button(text='Go to Screen One', on_press=self.change_screen))
        self.add_widget(box)

    def change_screen(self, instance):
        self.manager.current = 'screen_one'

class MainApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(ScreenOne(name='screen_one'))
        self.sm.add_widget(ScreenTwo(name='screen_two'))
        return self.sm

    def update_label(self, text):
        self.sm.get_screen('screen_two').children[0].children[1].text = text

    def run_console_input_loop(self):
        while True:
            text = input("Enter text: ")
            Clock.schedule_once(lambda dt: self.update_label(text))

# if __name__ == "__main__":
#     app = MainApp()
#     threading.Thread(target=app.run_console_input_loop).start()
#     app.run()
            
import threading, socket

# def client():
#     while True:
#         client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         client.connect(('localhost', 12340))
#         message = input('Client: ')
#         client.send(message.encode('utf-8'))
#         # print(client.recv(1024).decode('utf-8'))
#     client.close()

# print(get_wifi_ip_address())
# client()
'''


print(
    [['D:\\D_copy\\.', 'D:\\D_copy\\WI',],][0][0][0]
)