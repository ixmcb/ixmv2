from tkinter import *
from tkinter import messagebox

window=Tk()
window.title('Login to contunue')
window.geometry('400x150')

l1=Label(window,text='Username:',font=(14))
l2=Label(window,text='Api password:',font=(14))
l1.grid(row=0,column=0,padx=5,pady=5)
l2.grid(row=1,column=0,padx=5,pady=5)

Username=StringVar()
Password=StringVar()
t1=Entry(window,textvariable=Username,font=(14))
t2=Entry(window,textvariable=Password,font=(14),show='*')
t1.grid(row=0,column=1)
t2.grid(row=1,column=1)

def Login():
    if Username.get()=='ixmcb' and Password.get()=='almighty':
        messagebox.showinfo(title='Login succes',message="Welcome to ixmcb pfp changer bot")
        window=Tk()
        window.title('Enter Username')
        window.geometry('450x150')

        l1=Label(window,text='Usernamee',font=(14))
        l2=Label(window,text='Conform username',font=(14))
        l1.grid(row=0,column=0,padx=5,pady=5)
        l2.grid(row=1,column=0,padx=5,pady=5)

        Usernamee=StringVar()
        Conformusername=StringVar()
        t1=Entry(window,textvariable=Usernamee,font=(14))
        t2=Entry(window,textvariable=Conformusername,font=(14),show='*')
        t1.grid(row=0,column=1)
        t2.grid(row=1,column=1)

        b1=Button(window,command=Change,text='Change',font=(14))
        b1.grid(row=2,column=1,sticky=W)
    else:
        messagebox.showerror(title='Login error',message="Try again later Incoreect pass or user")

def Cancel():
    status=messagebox.askyesno(title='Conform',message="Are you sure to close ")
    if status==True:
        window.destroy()
    else:
        messagebox.showwarning(title='Warning',message="Please login again")

def Change():
    messagebox.showinfo(title='Succes',message="succes change , ")

b1=Button(window,command=Login,text='Login',font=(14))
b2=Button(window,command=Cancel,text='Cancel',font=(14))
b1.grid(row=2,column=1,sticky=W)
b2.grid(row=2,column=1,sticky=E)


window.mainloop()