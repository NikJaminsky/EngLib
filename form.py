from tkinter import *
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)       
        self.pack()
        self.create_widgets()  
            
    def click(self):
        inputLetter = self.enter.get()       
        #if self.show.winfo_exists() == 0: 
        #    self.show.destroy()
        self.show = tk.Label(self)
        self.show["text"] = searchLib(inputLetter)
        self.show.pack()

    def create_widgets(self):
        self.note = tk.Label(self)
        self.note["text"] = "Enter letter"
        self.note.pack()
        
        self.enter = tk.Entry(self)
        self.enter.pack()
        
        self.search = tk.Button(self)
        self.search["text"] = "Search"
        self.search["command"] = self.click
        self.search.pack()


def searchLib(letter):
    from libraryLetters import libr
    if letter in libr:
        return (libr[letter])
    else:
        return ("Not found")
        
def main():
    root = tk.Tk()
    root.geometry("400x300+300+250")
    #ent = tk.Entry(root,width=20,bd=3)
    app = Application(master=root)
    #ent.pack()
    app.mainloop()
    root.destroy()

if __name__ == '__main__':
    main()