from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

try:
    con = mysql.connector.connect(host='localhost', user='root', passwd='1234', database='student')
    cur = con.cursor()
except mysql.connector.Error as a:
    print(a)


class SMS:

    def Add(self):
        if self.entryID.index("end")==0 or self.entryFname.index("end")==0 or self.entryLname.index("end")==0 or self.entryAge.index("end")==0 or self.entryAddress.index("end")==0 or self.entryDegree.index("end")==0 or self.entryContact.index("end")==0:
            messagebox.showinfo("Error","Invalid Entry")
        elif not self.entryID.get().isdigit():
            messagebox.showinfo("Error","Invalid ID")
        elif not self.entryFname.get().isalpha():
            messagebox.showinfo("Error","Invalid First name")
        elif not self.entryLname.get().isalpha():
            messagebox.showinfo("Error","Invalid Last Name")
        elif not self.entryAge.get().isdigit():
            messagebox.showinfo("Error", "Invalid Age")
        elif not self.entryAddress.get().isalpha():
            messagebox.showinfo("Error", "Invalid Address")
        elif not self.entryContact.get().isdigit():
            messagebox.showinfo("Error", "Invalid Contact")
        else:
            print("Added")
            ID = int(self.entryID.get())
            Fname = self.entryFname.get()
            Lname = self.entryLname.get()
            Age = self.entryAge.get()
            Address = self.entryAddress.get()
            Degree = self.entryDegree.get()
            Contact= float(self.entryContact.get())

            query = 'insert into stud values(%s,%s,%s,%s,%s,%s,%s)'
            values = (ID, Fname, Lname, Age, Address, Degree,Contact)
            cur.execute(query, values)
            con.commit()
            self.show()

    def show(self):
        query = 'select * from stud'
        cur.execute(query)
        rows = cur.fetchall()
        if len(rows) != None:
            self.student_table.delete(*self.student_table.get_children())
        for row in rows:
            self.student_table.insert('', END, values=row)

    def pointer(self, event):
        point = self.student_table.focus()
        content = self.student_table.item(point)
        self.row = content['values']
        self.clear()
        self.entryID.insert(0, self.row[0])
        self.entryFname.insert(0, self.row[1])
        self.entryLname.insert(0, self.row[2])
        self.entryAge.insert(0, self.row[3])
        self.entryAddress.insert(0, self.row[4])
        self.entryDegree.insert(0, self.row[5])
        self.entryContact.insert(0,self.row[6])

    def update(self):
        if self.entryID.index("end")==0 or self.entryFname.index("end")==0 or self.entryLname.index("end")==0 or self.entryAge.index("end")==0 or self.entryAddress.index("end")==0 or self.entryDegree.index("end")==0 or self.entryContact.index("end")==0:
            messagebox.showinfo("Error","Invalid Entry")
        elif not self.entryID.get().isdigit():
            messagebox.showinfo("Error","Invalid ID")
        elif not self.entryFname.get().isalpha():
            messagebox.showinfo("Error","Invalid First name")
        elif not self.entryLname.get().isalpha():
            messagebox.showinfo("Error","Invalid Last Name")
        elif not self.entryAge.get().isdigit():
            messagebox.showinfo("Error", "Invalid Age")
        elif not self.entryAddress.get().isalpha():
            messagebox.showinfo("Error", "Invalid Address")
        elif not self.entryContact.get().isdigit():
            messagebox.showinfo("Error", "Invalid Contact")
        else:
            a = self.entryFname.get()
            b = self.entryLname.get()
            c = self.entryAge.get()
            d = self.entryAddress.get()
            e = self.entryDegree.get()
            f = self.entryID.get()
            query = f'update stud set FirstName=%s,LastName=%s,Age=%s,Address=%s,Degree=%s where ID="{f}"'
            values = (a, b, c, d, e)
            cur.execute(query, values)
            con.commit()
            self.show()
            messagebox.showinfo("Entry box", "Updated")

    def delete(self):
        e = self.entryID.get()
        query = f'delete from stud where ID="{e}"'
        cur.execute(query)
        con.commit()
        self.show()
        messagebox.showinfo("EntryBox", "Deleted")

    def clear(self):
        self.entryID.delete(0, END)
        self.entryFname.delete(0, END)
        self.entryLname.delete(0, END)
        self.entryAge.delete(0, END)
        self.entryAddress.delete(0, END)
        self.entryDegree.delete(0, END)
        print("Cleared")
        self.searchbyCB.delete(0,END)
        self.entrysearch.delete(0,END)
        self.entryContact.delete(0,END)

    def search(self):
        querys = 'select * from stud'
        cur.execute(querys)
        student = cur.fetchall()
        rows = self.search_item(student)

        if len(student) != 0:
            self.student_table.delete(*self.student_table.get_children())
        for row in rows:
            self.student_table.insert('', END, values=row)

    def search_item(self, list):
        a2 = self.searchbyCB.get()
        a3 = self.entrysearch.get()

        if a2 == 'ID':
            fieldId = 0
            a3 = int(self.entrysearch.get())
        elif a2 == 'FirstName':
            fieldId = 1
        elif a2 == 'LastName':
            fieldId = 2
        elif a2 == 'Age':
            a3 = int(self.entrysearch.get())
            fieldId = 3
        elif a2 == 'Address':
            fieldId = 4
        elif a2 == 'Degree':
            fieldId = 5
        else:
            a3= int(self.entryContact.get())
            fieldId=6

        found = []
        for xyz in list:
            if a3 == xyz[fieldId]:
                found.append(xyz)
        return found

    def bubble_sort(self, array):
        x = len(array)
        a = self.searchbyCB.get()
        if a == 'ID':
            fieldID = 0
        elif a == 'FirstName':
            fieldID = 1
        elif a == 'LastName':
            fieldID = 2
        elif a == 'Age':
            fieldID = 3
        elif a == 'Address':
            fieldID = 4
        elif a=='Contact':
            fieldID = 5
        else:
            fieldID = 6
        order=self.sortord.get()
        if order=="ASC":
            for i in range(x):
                for j in range(0, x - i - 1):
                    if array[j][fieldID] > array[j + 1][fieldID]:
                        array[j], array[j + 1] = array[j + 1], array[j]
            return array
        elif order=="DSC":
            for i in range(x-1,0,-1):
                for j in range(i):
                    if array[j][fieldID] < array[j + 1][fieldID]:
                        array[j], array[j + 1] = array[j + 1], array[j]
            return array
        else:
            messagebox.showinfo("Error","Maybe the field order is empty")
    def sorting(self):
        querys = 'select * from stud'
        cur.execute(querys)
        student = cur.fetchall()
        con.commit()
        rows1 = self.bubble_sort(student)
        if len(rows1) != 0:
            self.student_table.delete(*self.student_table.get_children())
        for row in rows1:
            self.student_table.insert('', END, values=row)
        messagebox.showinfo("Sort box", "Sorted")


    def __init__(self, root):
        # Labels
        self.lblID = Label(root, text="ID", font=("Times New Roman", 8), bg="dark slate grey", fg="White")
        self.lblID.place(x=35, y=60)
        self.lblFname = Label(root, text="First Name", font=("Times New Roman", 10), bg="dark slate grey", fg="White")
        self.lblFname.place(x=35, y=100)
        self.lblLname = Label(root, text="Last Name", font=("Times New Roman", 10), bg="dark slate grey", fg="White")
        self.lblLname.place(x=180, y=100)
        self.lblAge = Label(root, text="Age", font=("Times New Roman", 10), bg="dark slate grey", fg="White")
        self.lblAge.place(x=35, y=140)
        self.lblAddress = Label(root, text="Address", font=("Times New Roman", 10), bg="dark slate grey", fg="White")
        self.lblAddress.place(x=183, y=140)
        self.lblDegree = Label(root, text="Degree", font=("Times New Roman", 10), bg="dark slate grey", fg="White")
        self.lblDegree.place(x=183, y=180)
        self.lblContact=Label(root, text="Contact",font=("Times New Roman", 10), bg="dark slate grey", fg="White")
        self.lblContact.place(x=35,y=180)
        # Entries
        self.entryID = Entry(root)
        self.entryID.place(x=38, y=80)
        self.entryFname = Entry(root)
        self.entryFname.place(x=38, y=120)
        self.entryLname = Entry(root)
        self.entryLname.place(x=183, y=120)

        self.entryAge = Entry(root)
        self.entryAge.place(x=38, y=160)
        self.entryAddress = Entry(root)
        self.entryAddress.place(x=183, y=160)
        self.entryDegree = Entry(root,width=30)
        self.entryDegree.place(x=183, y=200)
        self.entryContact=Entry(root)
        self.entryContact.place(x=38,y=200)

        self.table_frame = Frame(root, bd=4, relief=RIDGE)
        self.table_frame.place(x=20, y=350, width=600, height=300)
        # Buttons
        self.buttonAdd = ttk.Button(root, text="Add", command=self.Add)
        self.buttonAdd.place(x=38, y=250)
        self.buttonUpdate = ttk.Button(root, text="Update", command=self.update)
        self.buttonUpdate.place(x=118, y=250)
        self.buttonDelete = ttk.Button(root, text="Delete", command=self.delete)
        self.buttonDelete.place(x=198, y=250)
        self.buttonClear = ttk.Button(root, text="Reset", command=lambda:[self.show(),self.clear()])
        self.buttonClear.place(x=278, y=250)

        # Scrollbar
        self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        # Table
        self.student_table = ttk.Treeview(self.table_frame,
                                          columns=('ID', 'Fname', 'Lname', 'Age', 'Address', 'Degree','Contact'),
                                          xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.student_table.heading('ID', text="ID")
        self.student_table.heading('Fname', text="First Name")
        self.student_table.heading('Lname', text="Last Name")
        self.student_table.heading('Age', text="Age")
        self.student_table.heading('Address', text="Address")
        self.student_table.heading('Degree', text="Degree")
        self.student_table.heading('Contact', text="Contact")
        self.student_table['show'] = 'headings'

        # Increasing width of the table
        self.student_table.column('ID', width=60)
        self.student_table.column('Fname', width=105)
        self.student_table.column('Lname', width=105)
        self.student_table.column('Age', width=60)
        self.student_table.column('Address', width=110)
        self.student_table.column('Degree', width=140)
        self.student_table.column('Contact',width=60)

        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)

        self.show()

        self.student_table.bind('<ButtonRelease-1>', self.pointer)

        self.student_table.pack(fill=BOTH, expand=True)

        # Making search and sort button
        self.sasbylbl = Label(root, text="Search or sort by", font=("Times New Roman", 10), bg="dark slate grey",
                              fg="White")
        self.sasbylbl.place(x=380, y=100)
        self.searchbyCB = ttk.Combobox(root, values=["ID", "FirstName", "LastName", "Age", "Address", "Degree","Contact"])
        self.searchbyCB.place(x=380, y=120)
        self.searchlbl = Label(root, text="Search", font=("Times New Roman", 10), bg="dark slate grey", fg="White")
        self.entrysearch = Entry(root)
        self.searchlbl.place(x=380, y=150)
        self.entrysearch.place(x=380, y=170)

        self.searchbtn = ttk.Button(root, text="Search", command=self.search)
        self.searchbtn.place(x=380, y=250)

        self.sortbtn = ttk.Button(root, text="Sort", command=self.sorting)
        self.sortbtn.place(x=460, y=250)

        self.sortordlbl=Label(root,text="Order", font=("Times New Roman", 10), bg="dark slate grey", fg="White")
        self.sortordlbl.place(x=530,y=100)
        self.sortord=ttk.Combobox(root,values=["ASC","DSC"],width=5)
        self.sortord.place(x=530,y=120)

root = Tk()
root.title("Searching and Sorting Student informartion")
root.geometry("630x700")

label_0 = Label(root, text="Searching and Sorting Student information", width=40, font=("Times New Roman", 25),
                bg="dark slate gray", fg="White").pack()
b = SMS(root)
root.configure(background="dark slate gray")
root.mainloop()
