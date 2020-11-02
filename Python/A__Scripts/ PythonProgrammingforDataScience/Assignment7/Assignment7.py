import tkinter as tk
import sqlalchemy as sql
import sqlite3

def problem1():
    """1. Create a student application using tkinter, PyQt5, or Kivy. Following functionalities should be
    present in the application. You need to create your Dabase file using SQLite.
    i. The application should accept First Name, Last Name, Street, City, State, Email,
    Telephone to insert this record in the database.
    ii. It should also list all the students in the database.
    iii. Delete a student

    Queries:
    ‐‐Display list of students
    select FirstName+' '+LastName+'('+ cast(StudentId as varchar)+')'  from Students
    ‐‐Insert student record
    insert into Students (FirstName,LastName,Street,City,State,Email,Telephone)
    values('','','','','','','')
    ‐‐Delete student record
    delete from Students where StudentId=0"""


    window = Window()
    

    return



class Window():
    def __init__(self):
        self.window = tk.Tk()
        self.currentSearch = []
        self.firstNameLabel = tk.Label(text="First Name")
        self.firstNameLabel.pack()
        self.firstNameEntry = tk.Entry(fg="black", bg="white", width=50)
        self.firstNameEntry.pack()

        self.LastNameLabel = tk.Label(text="Last Name")
        self.LastNameLabel.pack()
        self.lastNameEntry = tk.Entry(fg="black", bg="white", width=50)
        self.lastNameEntry.pack()

        self.streetLabel = tk.Label(text="street")
        self.streetLabel.pack()
        self.streetEntry = tk.Entry(fg="black", bg="white", width=50)
        self.streetEntry.pack()

        self.cityLabel = tk.Label(text="city")
        self.cityLabel.pack()
        self.cityEntry = tk.Entry(fg="black", bg="white", width=50)
        self.cityEntry.pack()

        self.stateLabel = tk.Label(text="state")
        self.stateLabel.pack()
        self.stateEntry = tk.Entry(fg="black", bg="white", width=50)
        self.stateEntry.pack()

        self.emailLabel = tk.Label(text="email")
        self.emailLabel.pack()
        self.emailEntry = tk.Entry(fg="black", bg="white", width=50)
        self.emailEntry.pack()

        self.telephoneLabel = tk.Label(text="telephone")
        self.telephoneLabel.pack()
        self.telephoneEntry = tk.Entry(fg="black", bg="white", width=50)
        self.telephoneEntry.pack()

        self.button = tk.Button(
            text="submit!",
            width=25,
            height=5,
            bg="white",
            fg="black",
            command = self.submit,
        )
        self.connect = sqlite3.connect('student.db')
        self.cursor = self.connect.cursor()
        try:
            self.cursor.execute("""CREATE TABLE student (
                            first text,
                            last text,
                            street text,
                            city text,
                            state text,
                            email text,
                            telephone text)""")
            self.connect.commit()
        except:
            "do nothing"

        self.button.pack()

        self.listbox = tk.Listbox(self.window, width = 75)
        self.listbox.pack(pady=15)
        self.fetchAll()

        self.delButton = tk.Button(
            text="delete",
            width=25,
            height=5,
            bg="white",
            fg="black",
            command = self.deleteItem,
        )
        self.delButton.pack()

        self.window.mainloop()
        self.connect.close()

    def deleteItem(self):
        #print("Trying to delete baby")
        self.selectedItem = self.listbox.get('active')
        #print(self.selectedItem)
        #print(self.selectedItem[0])
        self.cursor.execute("DELETE FROM student WHERE first = ? AND last = ?",
                            (self.selectedItem[0], self.selectedItem[1]))
        self.connect.commit()
        self.listbox.delete('active')
        self.fetchAll()

    def fetchAll(self):
        self.listbox.delete(0, 'end')
        self.cursor.execute("SELECT * FROM STUDENT")
        self.currentSearch = self.cursor.fetchall()
        for item in self.currentSearch:
            self.listbox.insert('end', item)

    def submit(self):
        self.student = Student(self.firstNameEntry.get(), self.lastNameEntry.get(), self.streetEntry.get(), self.cityEntry.get(),
                          self.stateEntry.get(), self.emailEntry.get(), self.telephoneEntry.get())

        self.cursor.execute("INSERT INTO student VALUES (?,?,?,?,?,?,?)", (self.firstNameEntry.get(),
                                                                           self.lastNameEntry.get(),
                                                                           self.streetEntry.get(),
                                                                           self.cityEntry.get(),
                                                                           self.stateEntry.get(),
                                                                           self.emailEntry.get(),
                                                                           self.telephoneEntry.get()))

        """
        self.cursor.execute("INSERT INTO student VALUES ('Bobby', 'Fisher', 'Bayberry lane', 'Bridgeport', 'CT', "
                            "'bobbyFisher@bridgeport.edu', '8675309')")"""
        self.connect.commit()
        self.fetchAll()

        """
        self.firstNameEntry.delete()
        self.lastNameEntry.delete()
        self.streetEntry.delete()
        self.cityEntry.delete()
        self.stateEntry.delete()
        self.emailEntry.delete()
        self.telephoneEntry.delete()
        self.cursor.execute("SELECT * FROM STUDENT")
        for item in self.cursor.fetchall():
            print(item)
        #print(self.student.firstName)
        """

class Student:
    def __init__(self, firstName = "", lastName ="", street="", city="", state="", email="", telephone=""):
        self.firstName = firstName
        self.lastName = lastName
        self.street = street
        self.city = city
        self.state = state
        self.email = email
        self.telephone = telephone
        self.fullName = firstName + " " + lastName

problem1()