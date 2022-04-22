from tkinter import *
from tkinter import ttk
import sqlite3

# global window

login_window = Tk()
login_window.title("Library Management System")
login_window.geometry("600x600")
login_window.configure(bg='black')


Title_Lms = Label(login_window,text='LIBRARY MANAGEMENT SYSTEM',bg='orange',font=("Cambria",25),pady=3,padx=58,relief=GROOVE)
Title_Lms.grid(row=0,column=0,columnspan=2,ipady=15)

# conn = sqlite3.connect('lms.db')

# c = conn.cursor()

# c.execute("""
#     CREATE TABLE BOOK(
#     book_id INT NOT NULL PRIMARY KEY,
#     title VARCHAR(200),
#     author VARCHAR(200),
#     genre VARCHAR(200),
#     price FLOAT,
#     availability INT,
#     publisher_id INT,
#     FOREIGN KEY(publisher_id) REFERENCES PUBLISHER(publisher_id) ON DELETE CASCADE
#     );
# """)

# c.execute("""
#     CREATE TABLE BOOK_MEMBER(
#     id INT NOT NULL PRIMARY KEY,
#     member_id INT,
#     book_id INT,
#     issue_date DATE,
#     due_date DATE,
#     return_date DATE,
#     fine FLOAT,
#     FOREIGN KEY(member_id) REFERENCES PUBLISHER(publisher_id) ON DELETE CASCADE,
#     FOREIGN KEY(book_id) REFERENCES BOOK(book_id) ON DELETE CASCADE
#     );
# """)

# c.execute("""
#     CREATE TABLE MEMBER(
#     member_id INT NOT NULL PRIMARY KEY,
#     name VARCHAR(200),
#     contact_no VARCHAR(15),
#     email_id VARCHAR(200),
#     address VARCHAR(200)
#     );
# """)

# c.execute("""
#     CREATE TABLE PUBLISHER (
#     publisher_id INT NOT NULL PRIMARY KEY,
#     name VARCHAR(200),
#     address VARCHAR(200)
#     );
# """)

# conn.commit()

# conn.close()

def LoginPage(user_id,password):
    print(user_id,password)

    def Book_Table():
        def Add_Book_Record():
            def Add_Book():
                conn = sqlite3.connect('lms.db')

                c = conn.cursor()

                try:
                    c.execute("INSERT INTO BOOK VALUES (:book_id, :title, :author, :genre, :price, :availability, :publisher_id)", 
                    {
                        'book_id' : book_id.get(),
                        'title' : title.get(),
                        'author' : author.get(),
                        'genre' : genre.get(),
                        'price' : price.get(),
                        'availability' : availability.get(),
                        'publisher_id' : publisher_id.get(),
                    })

                    conn.commit()

                    conn.close()

                    # CLEARING TEXT_BOXES
                    book_id.delete(0, END)
                    title.delete(0, END)
                    author.delete(0, END)
                    genre.delete(0, END)
                    price.delete(0, END)
                    availability.delete(0, END)
                    publisher_id.delete(0, END)

                    ADD_BOOK.destroy()
                except:
                    error_label = Label(ADD_BOOK, text="Error Occured while Inserting Data",font=("Cambria",15))
                    error_label.grid(row=9, column=0, columnspan=2, pady=(5,0), padx=10)

                

            ADD_BOOK = Toplevel(BOOK_TABLE)
            ADD_BOOK.geometry("600x600")

            add_record_title = Label(ADD_BOOK,text='ADD RECORD TO BOOK TABLE',bg='#4CED69',font=("Cambria",25),pady=3,padx=43,relief=GROOVE)
            add_record_title.grid(row=0, column=0, columnspan=2, pady=(0,10),ipadx=35)

            book_id = Entry(ADD_BOOK,width=30,font=("Cambria",15))
            book_id.grid(row=1, column=1, padx=25, ipadx=10, pady=(5,0))

            title = Entry(ADD_BOOK, width=30,font=("Cambria",15))
            title.grid(row=2, column=1, padx=25, ipadx=10, pady=(5,0))

            author = Entry(ADD_BOOK, width=30,font=("Cambria",15))
            author.grid(row=3, column=1, padx=25, ipadx=10, pady=(5,0))

            genre = Entry(ADD_BOOK, width=30,font=("Cambria",15))
            genre.grid(row=4, column=1, padx=25, ipadx=10, pady=(5,0))

            price = Entry(ADD_BOOK, width=30,font=("Cambria",15))
            price.grid(row=5, column=1, padx=25, ipadx=10, pady=(5,0))

            availability = Entry(ADD_BOOK, width=30,font=("Cambria",15))
            availability.grid(row=6, column=1, padx=25, ipadx=10, pady=(5,0))

            publisher_id = Entry(ADD_BOOK, width=30,font=("Cambria",15))
            publisher_id.grid(row=7, column=1, padx=25, ipadx=10, pady=(5,0))


            # LABELS
            book_id_label = Label(ADD_BOOK, text="Book id : ",font=("Cambria",15))
            book_id_label.grid(row=1, column=0, pady=(5,0), padx=10)

            title_label = Label(ADD_BOOK, text="Title : ",font=("Cambria",15))
            title_label.grid(row=2, column=0, pady=(5,0), padx=10)

            author_label = Label(ADD_BOOK, text="Author : ",font=("Cambria",15))
            author_label.grid(row=3, column=0, pady=(5,0), padx=10)

            genre_label = Label(ADD_BOOK, text="Genre : ",font=("Cambria",15))
            genre_label.grid(row=4, column=0, pady=(5,0), padx=10)

            price_label = Label(ADD_BOOK, text="Price : ",font=("Cambria",15))
            price_label.grid(row=5, column=0, pady=(5,0), padx=10)

            availability_label = Label(ADD_BOOK, text="Availability : ",font=("Cambria",15))
            availability_label.grid(row=6, column=0, pady=(5,0), padx=10)

            publisher_id_label = Label(ADD_BOOK, text="Publisher_id : ",font=("Cambria",15))
            publisher_id_label.grid(row=7, column=0, pady=(5,0), padx=10)


            Add_Book_Btn = Button(ADD_BOOK, text="Add Book", command=Add_Book,font=("Cambria",15))
            Add_Book_Btn.grid(row=8, column=0, columnspan=2,padx=20, pady=10)

        def Delete_Book_Record():

            def Delete_Book():
                conn = sqlite3.connect('lms.db')

                c = conn.cursor()

                c.execute("SELECT * FROM BOOK")
                records = c.fetchall()
                # print(records)

                PlaceHolder = delete_book_id.get()
                
                found = False
                for rec in records:
                    if str(rec[0])==PlaceHolder:
                        found = True

                if found:
                    c.execute("DELETE FROM BOOK WHERE book_id = " + PlaceHolder)
                    conn.commit()
                    conn.close()
                    delete_book_id.delete(0, END)
                    DELETE_BOOK.destroy()
                else:
                    error_label = Label(DELETE_BOOK, text="Record not found in the table",font=("Cambria",15))
                    error_label.grid(row=3, column=0, columnspan=2, pady=(5,0), padx=10)

            DELETE_BOOK = Toplevel(BOOK_TABLE)
            DELETE_BOOK.geometry("600x300")

            delete_record_title = Label(DELETE_BOOK,text='BOOK TABLE DELETE RECORD',bg='#4CED69',font=("Cambria",25),pady=3,padx=44,relief=GROOVE)
            delete_record_title.grid(row=0, column=0, columnspan=2, pady=(0,10),ipadx=35)

            

            delete_record_book_id_label = Label(DELETE_BOOK, text="Book id : ",font=("Cambria",15))
            delete_record_book_id_label.grid(row=1, column=0, pady=(5,0), padx=10)

            delete_book_id = Entry(DELETE_BOOK,width=30,font=("Cambria",15))
            delete_book_id.grid(row=1, column=1, padx=25, ipadx=10, pady=(5,0))

            delete_Book_record_Btn = Button(DELETE_BOOK, text="Delete Book", command=Delete_Book,font=("Cambria",15))
            delete_Book_record_Btn.grid(row=2, column=0, columnspan=2,padx=20, pady=10)
        
        def Query_Book_Record():
            QUERY_BOOK = Toplevel(BOOK_TABLE)
            QUERY_BOOK.geometry("1000x600")

            query_record_title = Label(QUERY_BOOK,text='BOOK TABLE QUERY RESULTS',bg='#4CED69',font=("Cambria",25),pady=3,padx=44,relief=GROOVE)
            query_record_title.grid(row=0, column=0, columnspan=2, pady=(0,10),ipadx=35)

            conn = sqlite3.connect('lms.db')

            c = conn.cursor()

            my_tree = ttk.Treeview(QUERY_BOOK)

            c.execute("SELECT * FROM BOOK")
            records = c.fetchall()
            # print(records)

            my_tree['columns'] = ('book_id', 'title', 'author', 'genre', 'price', 'availability', 'publisher_id')

            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("book_id", width=80, anchor=CENTER)
            my_tree.column("title", width=200, anchor=W)
            my_tree.column("author", width=200, anchor=W)
            my_tree.column("genre", width=140, anchor=W)
            my_tree.column("price", width=100, anchor=W)
            my_tree.column("availability", width=100, anchor=W)
            my_tree.column("publisher_id", width=80, anchor=W)

            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("book_id", text="book_id", anchor=CENTER)
            my_tree.heading("title", text="title", anchor=W)
            my_tree.heading("author", text="author", anchor=W)
            my_tree.heading("genre", text="genre", anchor=W)
            my_tree.heading("price", text="price", anchor=W)
            my_tree.heading("availability", text="availability", anchor=W)
            my_tree.heading("publisher_id", text="publisher_id", anchor=CENTER)

            count = 0
            for rec in records:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6]))
                count+=1

            my_tree.grid(row=1, column=0,padx=45)

            conn.commit()

            conn.close()


        BOOK_TABLE = Toplevel(window)
        BOOK_TABLE.geometry("600x600")
        BOOK_TABLE.configure(bg='#ffe5b4')

        book_table_title = Label(BOOK_TABLE,text='BOOK TABLE',bg='#800080',fg='white',font=("Cambria",25),pady=3,padx=168,relief=GROOVE)
        book_table_title.grid(row=0, column=0, pady=(0,10),ipadx=35)

        Add_Record_To_Book_Table = Button(BOOK_TABLE, text="Add Record To Book Table",bg='white', font=("Cambria",15), command=Add_Book_Record,relief=GROOVE,padx=10)
        Add_Record_To_Book_Table.grid(row=1, column=0, ipadx=40, pady=(25,0), ipady=10)

        Delete_Record_To_Book_Table = Button(BOOK_TABLE, text="Delete Record In Book Table",bg='white', font=("Cambria",15), command=Delete_Book_Record,relief=GROOVE)
        Delete_Record_To_Book_Table.grid(row=2, column=0, ipadx=40, pady=(25,0), ipady=10)

        Query_Record_To_Book_Table = Button(BOOK_TABLE, text="Query Book Table",bg='white', font=("Cambria",15), command=Query_Book_Record,relief=GROOVE,padx=45)
        Query_Record_To_Book_Table.grid(row=3, column=0, ipadx=40, pady=(25,0), ipady=10)

    def Publisher_Table():
        def Add_Publisher_Record():
            def Add_Publisher():
                conn = sqlite3.connect('lms.db')

                c = conn.cursor()

                try:
                    c.execute("INSERT INTO PUBLISHER VALUES (:publisher_id, :name, :address)", 
                    {
                        'publisher_id' : publisher_id.get(),
                        'name' : name.get(),
                        'address' : address.get(),
                    })

                    conn.commit()

                    conn.close()

                    # CLEARING TEXT_BOXES
                    publisher_id.delete(0, END)
                    name.delete(0, END)
                    address.delete(0, END)

                    ADD_PUBLISHER.destroy()
                except:
                    error_label = Label(ADD_PUBLISHER, text="Error Occured while Inserting Data",font=("Cambria",15))
                    error_label.grid(row=5, column=0, columnspan=2, pady=(5,0), padx=10)


            ADD_PUBLISHER = Toplevel(PUBLISHER_TABLE)
            ADD_PUBLISHER.geometry("600x600")

            publisher_table_title = Label(ADD_PUBLISHER,text='ADD RECORD TO PUBLISHER TABLE',bg='#4CED69',font=("Cambria",25),pady=3,padx=0,relief=GROOVE)
            publisher_table_title.grid(row=0, column=0, columnspan=2, pady=(0,10),ipadx=35)

            publisher_id = Entry(ADD_PUBLISHER,width=30,font=("Cambria",15))
            publisher_id.grid(row=1, column=1,padx=20, ipadx=10, pady=(5,0))

            name = Entry(ADD_PUBLISHER,width=30,font=("Cambria",15))
            name.grid(row=2, column=1, padx=20, ipadx=10, pady=(5,0))

            address = Entry(ADD_PUBLISHER,width=30,font=("Cambria",15))
            address.grid(row=3, column=1, padx=20, ipadx=10, pady=(5,0))


            publisher_id_label = Label(ADD_PUBLISHER, text="Publisher id : ",font=("Cambria",15))
            publisher_id_label.grid(row=1, column=0, pady=(5,0), padx=10)

            name_label = Label(ADD_PUBLISHER, text="Name : ",font=("Cambria",15))
            name_label.grid(row=2, column=0, pady=(5,0), padx=10)

            address_label = Label(ADD_PUBLISHER, text="Address : ",font=("Cambria",15))
            address_label.grid(row=3, column=0, pady=(5,0), padx=10)

            Add_Publisher_Btn = Button(ADD_PUBLISHER, text="Add Publisher", command=Add_Publisher,font=("Cambria",15))
            Add_Publisher_Btn.grid(row=4, column=0, columnspan=2,padx=20, pady=10)

        def Delete_Publisher_Record():

            def Delete_Publisher():
                conn = sqlite3.connect('lms.db')

                c = conn.cursor()

                c.execute("SELECT * FROM PUBLISHER")
                records = c.fetchall()

                PlaceHolder = delete_publisher_id.get()

                found = False
                for rec in records:
                    if str(rec[0])==PlaceHolder:
                        found = True
                
                if found:
                    c.execute("DELETE FROM PUBLISHER WHERE publisher_id = " + PlaceHolder)
                    conn.commit()
                    conn.close()
                    delete_publisher_id.delete(0, END)
                    DELETE_PUBLISHER.destroy()
                else:
                    error_label = Label(DELETE_PUBLISHER, text="Record not found in the table",font=("Cambria",15))
                    error_label.grid(row=3, column=0, columnspan=2, pady=(5,0), padx=10)
                    

            DELETE_PUBLISHER = Toplevel(PUBLISHER_TABLE)
            DELETE_PUBLISHER.geometry("600x300")

            delete_record_title = Label(DELETE_PUBLISHER,text='PUBLISHER TABLE DELETE RECORD',bg='#4CED69',font=("Cambria",25),pady=3,padx=0,relief=GROOVE)
            delete_record_title.grid(row=0, column=0, columnspan=2, pady=(0,10),ipadx=34)

            delete_record_publisher_id_label = Label(DELETE_PUBLISHER, text="Publisher id : ",font=("Cambria",15))
            delete_record_publisher_id_label.grid(row=1, column=0, pady=(5,0), padx=10)

            delete_publisher_id = Entry(DELETE_PUBLISHER,width=30,font=("Cambria",15))
            delete_publisher_id.grid(row=1, column=1, padx=25, ipadx=10, pady=(5,0))

            delete_Publisher_record_Btn = Button(DELETE_PUBLISHER, text="Delete Publisher", command=Delete_Publisher,font=("Cambria",15))
            delete_Publisher_record_Btn.grid(row=2, column=0, columnspan=2,padx=20, pady=10)  

        def Query_Publisher_Record():
            QUERY_PUBLISHER = Toplevel(PUBLISHER_TABLE)
            QUERY_PUBLISHER.geometry("700x600")

            query_record_title = Label(QUERY_PUBLISHER,text='PUBLISHER TABLE QUERY RESULTS',bg='#4CED69',font=("Cambria",25),pady=3,padx=3,relief=GROOVE)
            query_record_title.grid(row=0, column=0, columnspan=2, pady=(0,10),ipadx=35)

            conn = sqlite3.connect('lms.db')

            c = conn.cursor()

            my_tree = ttk.Treeview(QUERY_PUBLISHER)

            c.execute("SELECT * FROM PUBLISHER")
            records = c.fetchall()
            # print(records)

            my_tree['columns'] = ('publisher_id', 'name', 'address')

            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("publisher_id", width=120, anchor=CENTER)
            my_tree.column("name", width=265, anchor=W)
            my_tree.column("address", width=265, anchor=W)

            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("publisher_id", text="publisher_id", anchor=CENTER)
            my_tree.heading("name", text="name", anchor=W)
            my_tree.heading("address", text="address", anchor=W)
            
            count = 0
            for rec in records:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(rec[0],rec[1],rec[2]))
                count+=1

            my_tree.grid(row=1, column=0, padx=20)

            conn.commit()

            conn.close()


        PUBLISHER_TABLE = Toplevel(window)
        PUBLISHER_TABLE.geometry("600x600")
        PUBLISHER_TABLE.configure(bg='#ffe5b4')
        publisher_table_title = Label(PUBLISHER_TABLE,text='PUBLISHER TABLE',bg='#800080',fg='white',font=("Cambria",25),pady=3,padx=126,relief=GROOVE)
        publisher_table_title.grid(row=0, column=0, pady=(0,10),ipadx=35)

        Add_Record_To_Publisher_Table = Button(PUBLISHER_TABLE, text="Add Record To Publisher Table",bg='white', font=("Cambria",15), command=Add_Publisher_Record,relief=GROOVE,padx=10)
        Add_Record_To_Publisher_Table.grid(row=1, column=0, ipadx=20, pady=(25,0), ipady=10)

        Delete_Record_To_Publisher_Table = Button(PUBLISHER_TABLE, text="Delete Record In Publisher Table",bg='white', font=("Cambria",15), command=Delete_Publisher_Record,relief=GROOVE)
        Delete_Record_To_Publisher_Table.grid(row=2, column=0, ipadx=20, pady=(25,0), ipady=10)

        Query_Record_To_Publisher_Table = Button(PUBLISHER_TABLE, text="Query Publisher Table",bg='white', font=("Cambria",15), command=Query_Publisher_Record,relief=GROOVE,padx=45)
        Query_Record_To_Publisher_Table.grid(row=3, column=0, ipadx=20, pady=(25,0), ipady=10)

    def Member_Table():
        def Add_Member_Record():
            def Add_Member():
                conn = sqlite3.connect('lms.db')

                c = conn.cursor()

                try:
                    c.execute("INSERT INTO MEMBER VALUES (:member_id, :name, :contact_no, :email_id, :address)", 
                    {
                        'member_id' : member_id.get(),
                        'name' : name.get(),
                        'contact_no' : contact_no.get(),
                        'email_id' : email_id.get(),
                        'address' : address.get(),
                    })

                    conn.commit()

                    conn.close()

                    # CLEARING TEXT_BOXES
                    member_id.delete(0, END)
                    name.delete(0, END)
                    contact_no.delete(0, END)
                    email_id.delete(0, END)
                    address.delete(0, END)

                    ADD_MEMBER.destroy()
                except:
                    error_label = Label(ADD_MEMBER, text="Error Occured while Inserting Data",font=("Cambria",15))
                    error_label.grid(row=7, column=0, columnspan=2, pady=(5,0), padx=10)


            ADD_MEMBER = Toplevel(MEMBER_TABLE)
            ADD_MEMBER.geometry("600x600")

            member_table_title = Label(ADD_MEMBER,text='MEMBER TABLE',bg='#4CED69',font=("Cambria",25),pady=3,padx=144,relief=GROOVE)
            member_table_title.grid(row=0, column=0, columnspan=2, pady=(0,10),ipadx=35)

            member_id = Entry(ADD_MEMBER,width=30,font=("Cambria",15))
            member_id.grid(row=1, column=1, padx=25, ipadx=10, pady=(5,0))

            name = Entry(ADD_MEMBER,width=30,font=("Cambria",15))
            name.grid(row=2, column=1, padx=25, ipadx=10, pady=(5,0))

            contact_no = Entry(ADD_MEMBER,width=30,font=("Cambria",15))
            contact_no.grid(row=3, column=1, padx=25, ipadx=10, pady=(5,0))

            email_id = Entry(ADD_MEMBER,width=30,font=("Cambria",15))
            email_id.grid(row=4, column=1, padx=25, ipadx=10, pady=(5,0))

            address = Entry(ADD_MEMBER,width=30,font=("Cambria",15))
            address.grid(row=5, column=1, padx=25, ipadx=10, pady=(5,0))



            member_id_label = Label(ADD_MEMBER, text="Member id : ",font=("Cambria",15))
            member_id_label.grid(row=1, column=0, pady=(5,0), padx=10)

            name_label = Label(ADD_MEMBER, text="Name : ",font=("Cambria",15))
            name_label.grid(row=2, column=0, pady=(5,0), padx=10)

            contact_no_label = Label(ADD_MEMBER, text="Contact Number : ",font=("Cambria",15))
            contact_no_label.grid(row=3, column=0, pady=(5,0), padx=10)

            email_id_label = Label(ADD_MEMBER, text="Email Id : ",font=("Cambria",15))
            email_id_label.grid(row=4, column=0, pady=(5,0), padx=10)

            address_label = Label(ADD_MEMBER, text="Address : ",font=("Cambria",15))
            address_label.grid(row=5, column=0, pady=(5,0), padx=10)


            Add_Member_Btn = Button(ADD_MEMBER, text="Add Member", command=Add_Member,font=("Cambria",15))
            Add_Member_Btn.grid(row=6, column=0, columnspan=2, padx=20, pady=10)

        def Delete_Member_Record():

            def Delete_Memberr():
                conn = sqlite3.connect('lms.db')

                c = conn.cursor()

                c.execute("SELECT * FROM MEMBER")
                records = c.fetchall()

                PlaceHolder = delete_member_id.get()

                found = False
                for rec in records:
                    if str(rec[0])==PlaceHolder:
                        found = True

                if found:
                    c.execute("DELETE FROM MEMBER WHERE member_id = " + PlaceHolder)
                    conn.commit()
                    conn.close()
                    delete_member_id.delete(0, END)
                    DELETE_MEMBER.destroy()
                else:
                    error_label = Label(DELETE_MEMBER, text="Record not found in the table",font=("Cambria",15))
                    error_label.grid(row=3, column=0, columnspan=2, pady=(5,0), padx=10)

            DELETE_MEMBER = Toplevel(MEMBER_TABLE)
            DELETE_MEMBER.geometry("600x300")

            delete_record_title = Label(DELETE_MEMBER,text='MEMBER TABLE DELETE RECORD',bg='#4CED69',font=("Cambria",25),pady=3,padx=18,relief=GROOVE)
            delete_record_title.grid(row=0, column=0, columnspan=2, pady=(0,10),ipadx=34)

            delete_record_member_id_label = Label(DELETE_MEMBER, text="Member id : ",font=("Cambria",15))
            delete_record_member_id_label.grid(row=1, column=0, pady=(5,0), padx=10)

            delete_member_id = Entry(DELETE_MEMBER,width=30,font=("Cambria",15))
            delete_member_id.grid(row=1, column=1, padx=25, ipadx=10, pady=(5,0))

            delete_member_record_Btn = Button(DELETE_MEMBER, text="Delete Member", command=Delete_Memberr,font=("Cambria",15))
            delete_member_record_Btn.grid(row=2, column=0, columnspan=2,padx=20, pady=10)

        def Query_Member_Record():
            QUERY_MEMBER = Toplevel(MEMBER_TABLE)
            QUERY_MEMBER.geometry("1000x600")

            query_record_title = Label(QUERY_MEMBER,text='MEMBER TABLE QUERY RESULTS',bg='#4CED69',font=("Cambria",25),pady=3,padx=3,relief=GROOVE)
            query_record_title.grid(row=0, column=0, columnspan=2, pady=(0,10),ipadx=35)

            conn = sqlite3.connect('lms.db')

            c = conn.cursor()

            my_tree = ttk.Treeview(QUERY_MEMBER)

            c.execute("SELECT * FROM MEMBER")
            records = c.fetchall()
            # print(records)

            my_tree['columns'] = ('member_id', 'name', 'contact_no', 'email_id', 'address')

            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("member_id", width=80, anchor=CENTER)
            my_tree.column("name", width=200, anchor=W)
            my_tree.column("contact_no", width=150, anchor=W)
            my_tree.column("email_id", width=200, anchor=W)
            my_tree.column("address", width=280, anchor=W)

            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("member_id", text="member_id", anchor=CENTER)
            my_tree.heading("name", text="name", anchor=W)
            my_tree.heading("contact_no", text="contact_no", anchor=W)
            my_tree.heading("email_id", text="email_id", anchor=W)
            my_tree.heading("address", text="address", anchor=W)

            count = 0
            for rec in records:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(rec[0],rec[1],rec[2],rec[3],rec[4]))
                count+=1

            my_tree.grid(row=1, column=0,padx=40)

            conn.commit()

            conn.close()



        MEMBER_TABLE = Toplevel(window)
        MEMBER_TABLE.geometry("600x600")
        MEMBER_TABLE.configure(bg='#ffe5b4')

        member_table_title = Label(MEMBER_TABLE,text='MEMBER TABLE',bg='#800080',fg='white',font=("Cambria",25),pady=3,padx=144,relief=GROOVE)
        member_table_title.grid(row=0, column=0, pady=(0,10),ipadx=35)

        Add_Record_To_Member_Table = Button(MEMBER_TABLE, text="Add Record To Member Table",bg='white', font=("Cambria",15), command=Add_Member_Record,relief=GROOVE,padx=10)
        Add_Record_To_Member_Table.grid(row=1, column=0, ipadx=25, pady=(25,0), ipady=10)

        Delete_Record_To_Member_Table = Button(MEMBER_TABLE, text="Delete Record In Member Table",bg='white', font=("Cambria",15), command=Delete_Member_Record,relief=GROOVE)
        Delete_Record_To_Member_Table.grid(row=2, column=0, ipadx=25, pady=(25,0), ipady=10)

        Query_Record_To_Member_Table = Button(MEMBER_TABLE, text="Query Member Table", font=("Cambria",15),bg='white', command=Query_Member_Record,relief=GROOVE,padx=45)
        Query_Record_To_Member_Table.grid(row=3, column=0, ipadx=25, pady=(25,0), ipady=10)

    def Book_Member_Table():
        def Add_Book_Member_Record():

            def Add_Book_Member():
                conn = sqlite3.connect('lms.db')

                c = conn.cursor()

                try :
                    c.execute("INSERT INTO BOOK_MEMBER VALUES (:id, :member_id, :book_id, :issue_date, :due_date, :return_date, :fine)", 
                    {
                        'id' : Id.get(),
                        'member_id' : member_id.get(),
                        'book_id' : book_id.get(),
                        'issue_date' : issue_date.get(),
                        'due_date' : due_date.get(),
                        'return_date' : return_date.get(),
                        'fine' : fine.get() 
                    })

                    conn.commit()

                    conn.close()

                    # CLEARING TEXT_BOXES
                    Id.delete(0, END)
                    member_id.delete(0, END)
                    book_id.delete(0, END)
                    issue_date.delete(0, END)
                    due_date.delete(0, END)
                    return_date.delete(0, END)
                    fine.delete(0,END)

                    ADD_BOOK_MEMBER.destroy()
                except : 
                    error_label = Label(ADD_BOOK_MEMBER, text="Error Occured while Inserting Data",font=("Cambria",15))
                    error_label.grid(row=9, column=0, columnspan=2, pady=(5,0), padx=10)

            ADD_BOOK_MEMBER = Toplevel(BOOK_MEMBER_TABLE)
            ADD_BOOK_MEMBER.geometry("600x600")

            book_member_table_title = Label(ADD_BOOK_MEMBER,text='ISSUE TABLE',bg='#4CED69',font=("Cambria",25),pady=3,padx=169,relief=GROOVE)
            book_member_table_title.grid(row=0, column=0, columnspan=2, pady=(0,10),ipadx=35)

            Id = Entry(ADD_BOOK_MEMBER,width=30,font=("Cambria",15))
            Id.grid(row=1, column=1, padx=25, ipadx=10, pady=(5,0))

            member_id = Entry(ADD_BOOK_MEMBER,width=30,font=("Cambria",15))
            member_id.grid(row=2, column=1, padx=25, ipadx=10, pady=(5,0))

            book_id = Entry(ADD_BOOK_MEMBER,width=30,font=("Cambria",15))
            book_id.grid(row=3, column=1, padx=25, ipadx=10, pady=(5,0))

            issue_date = Entry(ADD_BOOK_MEMBER,width=30,font=("Cambria",15))
            issue_date.grid(row=4, column=1, padx=25, ipadx=10, pady=(5,0))

            due_date = Entry(ADD_BOOK_MEMBER,width=30,font=("Cambria",15))
            due_date.grid(row=5, column=1, padx=25, ipadx=10, pady=(5,0))

            return_date = Entry(ADD_BOOK_MEMBER,width=30,font=("Cambria",15))
            return_date.grid(row=6, column=1, padx=25, ipadx=10, pady=(5,0))

            fine = Entry(ADD_BOOK_MEMBER,width=30,font=("Cambria",15))
            fine.grid(row=7, column=1, padx=25, ipadx=10, pady=(5,0))


            Id_label = Label(ADD_BOOK_MEMBER, text="Id : ",font=("Cambria",15))
            Id_label.grid(row=1, column=0, pady=(5,0), padx=10)

            member_id_label = Label(ADD_BOOK_MEMBER, text="Member id : ",font=("Cambria",15))
            member_id_label.grid(row=2, column=0, pady=(5,0), padx=10)

            book_id_label = Label(ADD_BOOK_MEMBER, text="Book id : ",font=("Cambria",15))
            book_id_label.grid(row=3, column=0, pady=(5,0), padx=10)

            issue_date_label = Label(ADD_BOOK_MEMBER, text="Issue Date : ",font=("Cambria",15))
            issue_date_label.grid(row=4, column=0, pady=(5,0), padx=10)

            due_date_label = Label(ADD_BOOK_MEMBER, text="Due Date : ",font=("Cambria",15))
            due_date_label.grid(row=5, column=0, pady=(5,0), padx=10)

            return_date_label = Label(ADD_BOOK_MEMBER, text="Return Date : ",font=("Cambria",15))
            return_date_label.grid(row=6, column=0, pady=(5,0), padx=10)

            fine_label = Label(ADD_BOOK_MEMBER, text="Fine : ",font=("Cambria",15))
            fine_label.grid(row=7, column=0)


            Add_Book_Member_Btn = Button(ADD_BOOK_MEMBER, text="Add Issue Record", command=Add_Book_Member, font=("Cambria",15))
            Add_Book_Member_Btn.grid(row=8, column=0, columnspan=2, padx=20, pady=10)

        # def Delete_Book_Member_Record():

        #     def Delete_Book_Member():
        #         conn = sqlite3.connect('lms.db')

        #         c = conn.cursor()

        #         c.execute("SELECT * FROM MEMBER")
        #         records = c.fetchall()

        #         ph1 = delete_book_id.get()
        #         ph2 = delete_member_id.get()

        #         found = False
        #         for rec in records:
        #             if str(rec[0])==ph2 and str(rec[1])==ph1:
        #                 found = True

        #         if found:
        #             c.execute("DELETE FROM BOOK_MEMBER WHERE book_id = ? AND member_id = ?", (str(ph1), str(ph2)))
        #             conn.commit()
        #             conn.close()
        #             delete_book_id.delete(0, END)
        #             DELETE_BOOK_MEMBER.destroy()
        #         else:
        #             error_label = Label(DELETE_BOOK_MEMBER, text="Record not found in the table",font=("Cambria",15))
        #             error_label.grid(row=3, column=0, columnspan=2, pady=(5,0), padx=10)

        #     DELETE_BOOK_MEMBER = Toplevel(BOOK_MEMBER_TABLE)
        #     DELETE_BOOK_MEMBER.geometry("600x300")

        #     delete_record_title = Label(DELETE_BOOK_MEMBER,text='ISSUE TABLE DELETE RECORD',bg='#4CED69',font=("Cambria",25),pady=3,relief=GROOVE)
        #     delete_record_title.grid(row=0, column=0, columnspan=2, pady=(0,10),ipadx=5)

        #     delete_record_book_id_label = Label(DELETE_BOOK_MEMBER, text="Book id : ",font=("Cambria",15))
        #     delete_record_book_id_label.grid(row=1, column=0, pady=(5,0), padx=10)

        #     delete_book_id = Entry(DELETE_BOOK_MEMBER,width=30,font=("Cambria",15))
        #     delete_book_id.grid(row=1, column=1, padx=25, ipadx=10, pady=(5,0))

        #     delete_record_book_id_label = Label(DELETE_BOOK_MEMBER, text="Member id : ",font=("Cambria",15))
        #     delete_record_book_id_label.grid(row=2, column=0, pady=(5,0), padx=10)

        #     delete_member_id = Entry(DELETE_BOOK_MEMBER,width=30,font=("Cambria",15))
        #     delete_member_id.grid(row=2, column=1, padx=25, ipadx=10, pady=(5,0))

        #     delete_Book_record_Btn = Button(DELETE_BOOK_MEMBER, text="Delete Issue", command=Delete_Book_Member,font=("Cambria",15))
        #     delete_Book_record_Btn.grid(row=3, column=0, columnspan=2,padx=20, pady=10)

        def Query_Book_Member_Record():
            QUERY_BOOK_MEMBER = Toplevel(BOOK_MEMBER_TABLE)
            QUERY_BOOK_MEMBER.geometry("800x600")

            query_record_title = Label(QUERY_BOOK_MEMBER,text='ISSUE TABLE QUERY RESULTS',bg='#4CED69',font=("Cambria",25),pady=3,padx=0,relief=GROOVE)
            query_record_title.grid(row=0, column=0, columnspan=2, pady=(0,10),ipadx=10)

            conn = sqlite3.connect('lms.db')

            c = conn.cursor()


            my_tree = ttk.Treeview(QUERY_BOOK_MEMBER)

            c.execute("SELECT * FROM BOOK_MEMBER")
            records = c.fetchall()
            # print(records)

            my_tree['columns'] = ('id', 'member_id', 'book_id', 'issue_date', 'due_date', 'return_date', 'fine')

            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("id", width=70, anchor=CENTER)
            my_tree.column("member_id", width=90, anchor=CENTER)
            my_tree.column("book_id", width=90, anchor=CENTER)
            my_tree.column("issue_date", width=130, anchor=W)
            my_tree.column("due_date", width=130, anchor=W)
            my_tree.column("return_date", width=130, anchor=W)
            my_tree.column("fine", width=100, anchor=W)

            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("id", text="id", anchor=CENTER)
            my_tree.heading("member_id", text="member_id", anchor=CENTER)
            my_tree.heading("book_id", text="book_id", anchor=CENTER)
            my_tree.heading("issue_date", text="issue_date", anchor=W)
            my_tree.heading("due_date", text="due_date", anchor=W)
            my_tree.heading("return_date", text="return_date", anchor=W)
            my_tree.heading("fine", text="fine", anchor=W)
            

            count = 0
            for rec in records:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6]))
                count+=1

            my_tree.grid(row=1, column=0, padx=30)

            conn.commit()

            conn.close()


        BOOK_MEMBER_TABLE = Toplevel(window)
        BOOK_MEMBER_TABLE.geometry("600x600")
        BOOK_MEMBER_TABLE.configure(bg='#ffe5b4')

        book_member_table_title = Label(BOOK_MEMBER_TABLE,text='ISSUE TABLE',bg='#800080',fg='white',font=("Cambria",25),pady=3,padx=170,relief=GROOVE)
        book_member_table_title.grid(row=0, column=0, pady=(0,10),ipadx=35)

        Add_Record_To_Book_Member_Table = Button(BOOK_MEMBER_TABLE, text="Add Record To Issue Table",bg='white', font=("Cambria",15), command=Add_Book_Member_Record,relief=GROOVE,padx=10)
        Add_Record_To_Book_Member_Table.grid(row=1, column=0, ipadx=1, pady=(25,0), ipady=10)

        # Delete_Record_To_Book_Member_Table = Button(BOOK_MEMBER_TABLE, text="Delete Record In ISSUE Table", font=("Cambria",15), command=Delete_Book_Member_Record,relief=GROOVE)
        # Delete_Record_To_Book_Member_Table.grid(row=2, column=0, ipadx=1, pady=(25,0), ipady=10)

        Query_Record_To_Book_Member_Table = Button(BOOK_MEMBER_TABLE, text="Query Issue Table",bg='white', font=("Cambria",15), command=Query_Book_Member_Record,relief=GROOVE,padx=45)
        Query_Record_To_Book_Member_Table.grid(row=2, column=0, ipadx=1, pady=(25,0), ipady=10)

    if user_id=='admin' and password=='Admin':
        window = Tk()
        window.geometry("600x600")
        window.configure(bg='black')

        Title_Lms = Label(window,text='LIBRARY MANAGEMENT SYSTEM',bg='orange',font=("Cambria",25),pady=3,padx=58,relief=GROOVE)
        Title_Lms.grid(row=0,column=0,ipady=15)

        book_Table = Button(window, text="Book Table", font=("Cambria",15), command=Book_Table, padx=70,relief=GROOVE)
        book_Table.grid(row=1, column=0, ipadx=40, pady=(25,0), ipady=10)

        publisher_Table = Button(window, text="Publisher Table", font=("Cambria",15), command=Publisher_Table,padx=50,relief=GROOVE)
        publisher_Table.grid(row=2, column=0, ipadx=40, pady=(25,0), ipady=10)

        member_Table = Button(window, text="Member Table", font=("Cambria",15), command=Member_Table,padx=55,relief=GROOVE)
        member_Table.grid(row=3, column=0, ipadx=40, pady=(25,0), ipady=10)

        book_Member_Table = Button(window, text="Issue Table", font=("Cambria",15), command=Book_Member_Table,padx=70,relief=GROOVE)
        book_Member_Table.grid(row=4, column=0, ipadx=40, pady=(25,0), ipady=10)

        login_window.destroy()
    else:
        wrongCredentials = Label(login_window,text='Wrong Credentials',bg='yellow',font=("Cambria",25),pady=3,padx=58)
        wrongCredentials.grid(row=5,column=0,columnspan=2,pady=15)


Login = Label(login_window,text='LOGIN PAGE',bg='yellow',font=("Cambria",25),pady=3,padx=58,relief=GROOVE)
Login.grid(row=1,column=0,columnspan=2,pady=(20,80))

user_id = Entry(login_window,width=30,font=("Cambria",15))
user_id.grid(row=2, column=1, padx=25, ipadx=10, pady=(5,0))

password = StringVar()
password1 = Entry(login_window,textvariable=password, show='*', width=30,font=("Cambria",15))
password1.grid(row=3, column=1, padx=25, ipadx=10, pady=(5,0))

user_id_label = Label(login_window, text="USER ID : ",bg='black',fg='white',font=("Cambria",15))
user_id_label.grid(row=2, column=0, pady=(5,0), padx=10)

password_label = Label(login_window, text="PASSWORD : ",fg='white',bg='black',font=("Cambria",15))
password_label.grid(row=3, column=0, pady=(5,0), padx=10)

Login_Btn = Button(login_window, text="Log In", font=("Cambria",15),bg='white', command=lambda: LoginPage(user_id.get(),password1.get()),relief=GROOVE)
Login_Btn.grid(row=4, column=0, columnspan=2,ipadx=40, pady=(25,0))

login_window.mainloop()