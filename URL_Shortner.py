from tkinter import *
import tkinter as tk
from datetime import datetime
from tkinter import messagebox #Displaying messages
import pyshorteners # shorten url functionalities


class UrlShortener:
    def create_short_url(self):
        if self.url_entry.get() == "":
            messagebox.showerror("Error","Please Paste the URL")
        else:
            long_url = self.url_entry.get()
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(long_url)

            self.output_entry = Entry(self.root, font=("Times New Roman",10, 'bold'), fg="navy blue", width=30, relief="groove", borderwidth=2)
            self.output_entry.insert(END, short_url)
            self.output_entry.place(x=100,y=240)


    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x300')
        self.root.title('URL Shortener ✂️')
        self.root['bg'] = 'white'

        self.title_label = Label(self.root, text="URL Shortener", font=("garamond", 15,'bold'), bg="white", fg="purple")
        self.title_label.place(x=180,y=25)

        self.date_label = Label(self.root, text=datetime.now().date(), fg="purple", font=('Times New Roman', 11, 'bold'))
        self.date_label.place(x=410,y=5)

        Label(self.root, text="Paste Your URL Here....", font=('Times New Roman', 12, 'bold'), fg="purple").place(x=80,y=70)

        self.url_entry = Entry(self.root, width=50,font=('Times New Roman', 9, 'bold'), bg="lightgray", relief="groove", borderwidth=2, fg="navy blue")
        self.url_entry.place(x=80,y=110)

        self.create_button = Button(self.root, relief="groove", text="Create", font=("Verdana",10,"bold"),bg="purple",fg="white", command=self.create_short_url)
        self.create_button.place(x=200,y=150)

        Label(self.root, text="URL Shortener : ", font=('Times New Roman', 12, 'bold'), fg="purple").place(x=85,y=200)

        self.root.mainloop()

if __name__ == '__main__':
    UrlShortener()
