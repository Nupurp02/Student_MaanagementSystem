import tkinter as tk
import mysql.connector

def add():
        mydb = mysql.connector.connect(
                        user ='root',
                        password= 'Nupur@2000',
                        host = 'localhost',
                        database = 'students')
        mydbcursor = mydb.cursor()
        return mydb

def connect():
	roll1 = roll.get()
	name1 = name.get()
	mark1 = mark.get()
	mydb = mysql.connector.connect('records.db')
	
	mycursor.execute("INSERT INTO records VALUES (%s, %s, %s)",(roll.get(), name.get(), mark.get()))
	print("added")
	mycursor.close()
	mydb.commit()
	mydb.close()

def NewAdd():
    root = tk.Toplevel(tab)
    root.grab_set()
    root.title("Add Student Record")
    root.geometry("500x400")
    root['bg']='light blue'
    frame1 = tk.Frame(root, bg='light blue')
    frame2 = tk.Frame(root, bg='light blue')
    frame3 = tk.Frame(root, bg='light blue')
    frame4 = tk.Frame(root, bg='light blue')
    frame5 = tk.Frame(root, bg='light blue')



    l1 = tk.Label(frame1, text = "Enter Rno:", bg='light blue', font = "30").pack(expand = 1)
    E1 = tk.Entry(frame1, bd =5, font = "35", textvariable = roll).pack(expand = 1)

    l2 = tk.Label(frame2, text = "Enter Name:", bg='light blue', font = "30").pack(expand = 1)
    E2 = tk.Entry(frame2, bd =5, font = "35", textvariable = name).pack(expand = 1)

    l3 = tk.Label(frame3, text = "Enter Marks:", bg='light blue', font = "30").pack(expand = 1)
    E3 = tk.Entry(frame3, bd =5, font = "35", textvariable = mark).pack(expand = 1)

    savebutton = tk.Button(frame4, text = "Save", font = "30", width = "13" , command = connect).pack(expand = 1)
    B2 = tk.Button(frame5, text = "Back", font = "30", width = "13", command = root.destroy).pack(expand = 1)
    frame1.pack(padx=1,pady=1)
    frame2.pack(padx=10,pady=10)
    frame3.pack(padx=1,pady=20)
    frame4.pack(padx=5,pady=2)
    frame5.pack(padx=5,pady=1)
    root.mainloop()

   def NewView():

    win = tk.Toplevel(tab)
    win.geometry("500x400")
    win['bg']='lavender'
    win.title("View Student")
    listbox = tk.Listbox(win, bg = "lavender")
    listbox.pack(side = tk.LEFT, fill = tk.BOTH)
    scrollbar = tk.Scrollbar(win)
    scrollbar.pack(side = tk.RIGHT, fill = tk.BOTH)
    for values in range(100):
        listbox.insert(tk.END, values)
    listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)

def NewUpdate():
    up = tk.Toplevel(tab)
    up.geometry("500x400")
    up['bg']='beige'
    up.title("Update Student Record")
    frame1 = tk.Frame(up, bg='beige')
    frame2 = tk.Frame(up, bg='beige')
    frame3 = tk.Frame(up, bg='beige')
    frame4 = tk.Frame(up, bg='beige')
    frame5 = tk.Frame(up, bg='beige')
    l1 = tk.Label(frame1, text = "Enter Rno:", bg='beige', font = "35").pack(expand = 1)
    E1 = tk.Entry(frame1, bd =5,  font = "35").pack(expand = 1)

    l2 = tk.Label(frame2, text = "Enter Name:", bg='beige',  font = "35").pack(expand = 1)
    E2 = tk.Entry(frame2, bd =5,  font = "35").pack(expand = 1)

    l3 = tk.Label(frame3, text = "Enter Marks:", bg='beige',  font = "35").pack(expand = 1)
    E3 = tk.Entry(frame3, bd =5,  font = "35").pack(expand = 1)

    B1 = tk.Button(frame4, text = "Save", font = "30", width = "13").pack(expand = 1)
    B2 = tk.Button(frame5, text = "Back", font = "30", width = "13", command = up.destroy).pack(expand = 1)
    frame1.pack(padx=1,pady=1)
    frame2.pack(padx=10,pady=10)
    frame3.pack(padx=1,pady=20)
    frame4.pack(padx=5,pady=2)
    frame5.pack(padx=5,pady=1)



def NewDelete():
    Dele = tk.Toplevel(tab)
    Dele.geometry("500x400")
    Dele['bg']='light green'
    Dele.title("Deleete Student")
    frame1 = tk.Frame(Dele)
    frame2 = tk.Frame(Dele)
    frame3 = tk.Frame(Dele, bg = 'light green')

    def save():
            pass
    l1 = tk.Label(frame3, text = "Enter Rno:", bg='light green', font = "27").pack(expand = 1)
    E1 = tk.Entry(frame3, bd =5).pack(expand = 1)

    B1 = tk.Button(frame1, text = "Save", font = "30", width = "13").pack(expand = 0.5)
    B2 = tk.Button(frame2, text = "Back", font = "30", width = "13", command = Dele.destroy).pack(expand = 0.5)
    frame3.pack(padx=1,pady=20)
    frame1.pack(padx=1,pady=1)
    frame2.pack(padx=5,pady=3)





tab = tk.Tk()
tab.geometry("500x400")
tab['bg']='light yellow'
tab.title("S.M.S")
frame1 = tk.Frame(tab, bg='beige')
frame2 = tk.Frame(tab, bg='beige')
frame3 = tk.Frame(tab, bg='beige')
frame4 = tk.Frame(tab, bg='beige')
frame5 = tk.Frame(tab, bg='beige')


B1 = tk.Button(frame1, text = "Add", font = "30", width = "13", command = NewAdd )
B1.pack(expand = 1)
#B1.bind("<Button>",lambda e: NewAdd(root))

B2 = tk.Button(frame2, text = "View", font = "30", width = "13", command = NewView)
B2.pack(expand = 1)

B3 = tk.Button(frame3, text = "Update", font = "30", width = "13", command = NewUpdate)
B3.pack(expand = 1)

B4 = tk.Button(frame4, text = "Delete", font = "30", width = "13", command = NewDelete)
B4.pack(expand = 1)

B5 = tk.Button(frame5, text = "Charts", font = "30", width = "13")
B5.pack(expand = 1)

frame1.pack(padx=1,pady=10)
frame2.pack(padx=1,pady=10)
frame3.pack(padx=1,pady=10)
frame4.pack(padx=1,pady=10)
frame5.pack(padx=1,pady=10)

roll = tk.StringVar()
name = tk.StringVar()
mark = tk.StringVar()




tab.mainloop()
