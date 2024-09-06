# Login Application
import tkinter as tk
import mysql.connector as mysql
import tkinter.messagebox as msg
w = tk.Tk()
w.title("Login")
w.geometry("500x300+200+200")
w.config(bg='cyan')
cn = mysql.connect(database='dtest3',user='root',password='root')

def login():
    user = e1.get()
    password = e2.get()
    c = cn.cursor()
    try:
        c.execute("SELECT password FROM login WHERE username = %s", (user,))
        result = c.fetchone()
        if result:
            stored_password = result[0]
            if password == stored_password:
                msg.showinfo(title="Info", message="Login Successful")
            else:
                msg.showinfo(title="Info", message="Invalid password")
        else:
            msg.showinfo(title="Info", message="User does not exist")
        e1.delete(0,tk.END)
        e2.delete(0,tk.END)
    except mysql.Error as e:
        msg.showinfo(title="Error", message=f"Error in database: {e}")

def register():
    rw=tk.Tk()
    rw.title("Register")
    rw.geometry("500x300+200+200")
    rw.config(bg='cyan')
    def login2():
        c = cn.cursor()
        user = re1.get()
        pwd = re2.get()
        email = re3.get()
        try:
            c.execute("select email from login where username = %s",params=(user,))
            mail = c.fetchall()
            if mail:
                mail1 = mail[0]
                if mail1 == mail:
                    msg.showinfo(title="Info",message="User already exists")
                else:
                    msg.showinfo(title="Info",message="Username already taken")
            else:
                c.execute("Insert into login values(%s,%s,%s)",params=(user,pwd,email,))
                msg.showinfo(title="Login",message="Login registration Successful,go back and Login")
            re1.delete(0,tk.END)
            re2.delete(0,tk.END)
            re3.delete(0,tk.END)
            cn.commit()
        except mysql.Error as e:
            msg.showinfo(title='Error',message=f"Error : {e}")
    rl1 = tk.Label(rw,text="Username : ",font=('Arial',14),bg='cyan',fg='red')
    rl2 = tk.Label(rw,text="Password : ",font=('Arial',14),bg='cyan',fg='red')
    rl3 = tk.Label(rw,text="Email : ",font=('Arial',14),bg='cyan',fg='red')
    re1 = tk.Entry(rw,font=('Arial',14),bg='yellow',fg='blue')
    re2 = tk.Entry(rw,font=('Arial',14),bg='yellow',fg='blue',show="*")
    re3 = tk.Entry(rw,font=('Arial',14),bg='yellow',fg='blue')
    rb1 = tk.Button(rw,text='Register',font=('Arial',14),bg='yellow',fg='blue',command=login2)
    rb2 = tk.Button(rw,text='Exit',font=('Arial',14),bg='yellow',fg='blue',command=lambda:rw.destroy())
    rl1.place(x=100,y=50)
    rl2.place(x=100,y=100)
    rl3.place(x=100,y=150)
    re1.place(x=200,y=50)
    re2.place(x=200,y=100)
    re3.place(x=200,y=150)
    rb1.place(x=150,y=200)
    rb2.place(x=260,y=200)
l1=tk.Label(w,text="Username : ",font=('Arial',14),bg='cyan',fg='red')
l2=tk.Label(w,text="Password : ",font=('Arial',14),bg='cyan',fg='red')
e1=tk.Entry(w,font=('Arial',14),bg='yellow',fg='blue')
e2=tk.Entry(w,font=('Arial',14),bg='yellow',fg='blue',show="*")
b1=tk.Button(w,text="Login",font=('Arial',14),bg='yellow',fg='blue',command=login)
b2=tk.Button(w,text="Register",font=('Arial',14),bg='yellow',fg='blue',command=register)
b3=tk.Button(w,text="Exit",font=('Arial',14),bg='yellow',fg='blue',command=lambda:w.destroy())
l1.place(x=100,y=50)
l2.place(x=100,y=100)
e1.place(x=200,y=50)
e2.place(x=200,y=100)
b1.place(x=120,y=200)
b2.place(x=210,y=200)
b3.place(x=330,y=200)
