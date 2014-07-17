# coding=utf-8
# Project Interpreter Version: 2.7.6
from Tkinter import *
import socket
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def getCurrentTime(name):
    return name + ':' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n  '


def sendmessage():
    # 在聊天内容上方加一行 显示发送人及发送时间
    text_msglist.insert(END, getCurrentTime('ME'), 'green')
    msgSend = text_msg.get('0.0', END)
    text_msglist.insert(END, msgSend)
    text_msg.delete('0.0', END)
    clientSocket.send(msgSend)
    msgReceive = clientSocket.recv(1024)
    text_msglist.insert(END, getCurrentTime('Server'), 'green')
    text_msglist.insert(END, msgReceive)


app = Tk()
app.title("Do not stop talking")

frame_left_top = Frame(width=380, height=270, bg='white')
frame_left_center = Frame(width=380, height=100, bg='white')
frame_left_bottom = Frame(width=380, height=20)
frame_right = Frame(width=170, height=400, bg='white')

text_msglist = Text(frame_left_top)
text_msg = Text(frame_left_center)
button_sendmsg = Button(frame_left_bottom, text='发送', command=sendmessage)

# 创建一个绿色的tag
text_msglist.tag_config('green', foreground='#008B00')
# 使用grid设置各个容器位置
frame_left_top.grid(row=0, column=0, padx=2, pady=5)
frame_left_center.grid(row=1, column=0, padx=2, pady=5)
frame_left_bottom.grid(row=2, column=0)
frame_right.grid(row=0, column=1, rowspan=3, padx=4, pady=5)
frame_left_top.grid_propagate(0)
frame_left_center.grid_propagate(0)
frame_left_bottom.grid_propagate(0)
# 把元素填充进frame
text_msglist.grid()
text_msg.grid()
button_sendmsg.grid(sticky=E)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("localhost", 5778))

app.mainloop()



