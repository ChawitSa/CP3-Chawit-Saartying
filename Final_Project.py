#==========Zone of DataBase==========
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('C:/Users/Chawi/Downloads/GitWorkplace/CP3-Chawit-Saartying/firebase_key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://completepython3-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

#===========Zone of Class===========
from datetime import date
from tkinter import ttk

class Person:
    __name = "N/A"
    __phoneNumber = "N/A"
    __contact = "N/A"

    def __init__(self, n:str, p:str, c:str):
        self.__name = n
        self.__phoneNumber = p
        self.__contact = c
        db.reference('').child('Person').update({
                self.__name: {
                    "PhoneNumber": self.__phoneNumber,
                    "Contact": self.__contact
                }
        })

    def updatePerson(self, n:str, p:str, c:str):
        self.__name = n
        self.__phoneNumber = p
        self.__contact = c
        db.reference('').child('Person').update({
                self.__name: {
                    "PhoneNumber": self.__phoneNumber,
                    "Contact": self.__contact
                }
        })
    def getName(self):
        return self.__name
    def getPhone(self):
        return self.__phoneNumber
    def getContact(self):
        return self.__contact

class Book:
    __name = "N/A"
    __author = "N/A"
    __category = "0000"
    __status = "N/A"
    __borrowedBy = []
    __borrowedDate = []
    __returnedDate = []

    def __init__(self):
        self.__name = n
        self.__no = no
        self.__author = a
        self.__category = c
        self.statusUnavailable()
        self.database()
    def __init__(self, n:str, no:str, a:str, c:str):
        self.__name = n
        self.__no = no
        self.__author = a
        self.__category = c
        self.statusUnavailable()
        self.database()

    def database(self):
        db.reference('Book/'+self.__name).child(self.__no).update({
                    "Author": self.__author,
                    "Category": self.__category,
                    "Status": self.__status,
                    "Borrowed By": self.__borrowedBy,
                    "Borrowed Date": self.__borrowedDate,
                    "Returned Date": self.__returnedDate
        })
    def updateBook(self, n:str, no:str, a:str, c:str):
        self.__name = n
        self.__no = no
        self.__author = a
        self.__category = c
        self.statusUnavailable()
        self.database()
    def statusAvailable(self):
        self.__status = "Available"
    def statusUnavailable(self):
        self.__status = "Unavailable"

    def borrowBook(self, d:int, m:int, y:int, person:Person):
        self.__borrowedDate.append(date(y, m, d))
        self.__borrowedBy.append(person)
        self.statusUnavailable()
        self.database()
    def returnBook(self, d:int, m:int, y:int):
        self.__returnedDate.append(date(y, m, d))
        self.statusAvailable
        self.database()
    def getStatus(self):
        return self.__status
    def deleteBook(self):
        db.reference('Book/'+self.__name).child(self.__no).delete()
        del self


class Shelf:
    __no:int
    __row:int
    __book:Book

    def __init__(self, no:int, y:int, r:int):
        self.__no = no
        self.__row = r
        self.database()

    def database(self):
        db.reference('Shelf/'+str(self.__no)).child(str(self.__row)).update({
                    self.__row:{"Book": self.__book}
        })
    def takeBookIn(self, book:Book):
        self.__book = book
        self.database()
        #book.returnBook() อย่าลืมเพิ่ม
    def takeBookOut(self):
        self.__book = Book()
        self.database()
        #book.borrowBook() อย่าลืมเพิ่ม
    def deleteShelf(self):
        db.reference('Shelf/'+str(self.__no)).child(str(self.__row)).delete()
        del self
        


#===========Zone of GUI's Function===========
from tkinter import *

LARGEFONT = ("Verdana", 35)




#===========Zone of GUI's Page Controller===========
class TkApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Page1,Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NESW")
        
        self.showFrame(Page1)

    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


    

#================Zone of GUI's Page1================
class Page1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.winfo_toplevel().title("Library Service System")
        self.winfo_toplevel().geometry("900x600")
        self.winfo_toplevel().resizable(width=False, height=False)
        label = ttk.Label(self, text="Welcome to Library Service System", font=LARGEFONT)
        label.grid(row=0, column=1, padx=25, pady=50)

        button1 = Button(self, text="Data Manager", height=5, width=50, font=50, command=lambda:controller.showFrame(Page2))
        button1.grid(row=2, column=1, padx=100, pady=10)

        button2 = Button(self, text="Borrow", height=5, width=50, font=50, command=lambda:controller.showFrame(Page1))
        button2.grid(row=3, column=1, padx=100, pady=10)

        button3 = Button(self, text="Return", height=5, width=50, font=50, command=lambda:controller.showFrame(Page1))
        button3.grid(row=4, column=1, padx=100, pady=10)

#================Zone of GUI's Page2================
class Page2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.winfo_toplevel().title("Library Service System")
        self.winfo_toplevel().geometry("900x600")
        self.winfo_toplevel().resizable(width=False, height=False)
        label = ttk.Label(self, text="Add Shelf", font=LARGEFONT)
        label.grid(row=0, column=0, padx=335, pady=50)

        label1 = Label(self, text="Welcome to Library Service System", height=1, width=50, font=50)
        label1.grid(row=1, column=0, padx=25)
        box1 = Entry(self, )
        box1.grid(row=2, column=0, padx=100)

        button2 = Button(self, text="Borrow", height=5, width=50, font=50, command=lambda:controller.showFrame(Page1))
        button2.grid(row=3, column=0, padx=100, pady=10)

        button3 = Button(self, text="Return", height=5, width=50, font=50, command=lambda:controller.showFrame(Page1))
        button3.grid(row=4, column=0, padx=100, pady=10)

#===========Zone of GUI's Display===========
app = TkApp()
app.mainloop()