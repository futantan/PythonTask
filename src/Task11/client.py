# _*_ coding:utf-8 _*_
# Filename:ClientUI.py

from Tkinter import *
import Tkinter
import socket
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class Client():
    title = 'Do not stop talking'
    host = 'localhost'
    port = 5778
    flag = False

    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.title(self.title)
        self.clientSocket = None

        # 4 Frame to arrange the layout
        self.frame = [Tkinter.Frame(), Tkinter.Frame(), Tkinter.Frame(), Tkinter.Frame()]

        # ScrollBar
        self.chatTextScrollBar = Tkinter.Scrollbar(self.frame[0])
        self.chatTextScrollBar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

        # Bind the ScrollBar with Text Area
        self.chatText = Tkinter.Listbox(self.frame[0], width=70, height=18)
        self.chatText['yscrollcommand'] = self.chatTextScrollBar.set
        self.chatText.pack(expand=1, fill=Tkinter.BOTH)
        self.chatTextScrollBar['command'] = self.chatText.yview
        self.frame[0].pack(expand=1, fill=Tkinter.BOTH)

        label = Tkinter.Label(self.frame[1], height=2)
        label.pack(fill=Tkinter.BOTH)
        self.frame[1].pack(expand=1, fill=Tkinter.BOTH)

        # ScrollBar
        self.inputTextScrollBar = Tkinter.Scrollbar(self.frame[2])
        self.inputTextScrollBar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

        # Bind the ScrollBar with Input Text Area
        self.inputText = Tkinter.Text(self.frame[2], width=70, height=8)
        self.inputText['yscrollcommand'] = self.inputTextScrollBar.set
        self.inputText.pack(expand=1, fill=Tkinter.BOTH)
        self.inputTextScrollBar['command'] = self.chatText.yview()
        self.frame[2].pack(expand=1, fill=Tkinter.BOTH)

        # send message button
        self.sendButton = Tkinter.Button(self.frame[3], text='Send', width=10, command=self.sendMessage)
        self.sendButton.pack(expand=1, side=Tkinter.BOTTOM and Tkinter.RIGHT, padx=15, pady=8)

        # close button
        self.closeButton = Tkinter.Button(self.frame[3], text='Close', width=10, command=self.close)
        self.closeButton.pack(expand=1, side=Tkinter.RIGHT, padx=15, pady=8)
        self.frame[3].pack(expand=1, fill=Tkinter.BOTH)

    def getCurrentTime(self, name):
        return name + ':'
        # + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n  '

    # send message and receive from server
    def sendMessage(self):
        self.chatText.insert(END, self.getCurrentTime('======ME======:'))
        msgSend = self.inputText.get('0.0', END)
        self.chatText.insert(END, msgSend)
        self.inputText.delete('0.0', END)
        self.clientSocket.send(msgSend)
        msgReceive = self.clientSocket.recv(1024)
        self.chatText.insert(END, self.getCurrentTime('=====Server====='))
        self.chatText.insert(END, msgReceive)

    def close(self):
        sys.exit()

    def connectWithServer(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((self.host, self.port))
        msgReceive = self.clientSocket.recv(1024)
        self.chatText.insert(END, self.getCurrentTime('=====Server====='))
        self.chatText.insert(END, msgReceive)


def main():
    client = Client()
    client.connectWithServer()
    client.root.mainloop()


if __name__ == '__main__':
    main()
