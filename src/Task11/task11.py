from Tkinter import *

app = Tk()
app.title("My title")
app.geometry('200x100+200+100')

sendButton = Button(app, text="send", width=10)
sendButton.pack(side='right', padx=10, pady=10)

app.mainloop()